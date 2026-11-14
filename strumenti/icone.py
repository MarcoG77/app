"""Disegna le icone delle app (schermata Home dell'iPhone, Dock del Mac, scheda del browser).

Uso:  ../Software contabilità (Claude)/.venv/bin/python strumenti/icone.py
Ogni icona: il colore principale dell'app, un cerchio chiaro e l'emoji dell'app (Noto Emoji di Google,
licenza Apache 2.0, in strumenti/emoji/). L'iPhone arrotonda gli angoli da solo: qui l'immagine è quadrata.
"""
from pathlib import Path

from PIL import Image, ImageDraw

RADICE = Path(__file__).resolve().parent.parent
APP = {
    # cartella: (colore principale, emoji)
    "biblioteca": ("#c2410c", "1f4da"),
    "scadenzario": ("#0f766e", "1f5d3"),
    "contabilita": ("#3d5a80", "1f3e0"),
}
LATO = 1024  # si disegna grande e poi si riduce, così i bordi sono morbidi


def colore(esadecimale, schiarisci=0.0):
    r, g, b = (int(esadecimale[i:i + 2], 16) for i in (1, 3, 5))
    return tuple(round(c + (255 - c) * schiarisci) for c in (r, g, b))


def icona(principale, emoji):
    img = Image.new("RGB", (LATO, LATO), colore(principale))
    # leggera sfumatura: più chiaro in alto
    sfumatura = Image.new("RGB", (LATO, LATO), colore(principale, 0.18))
    maschera = Image.linear_gradient("L").resize((LATO, LATO)).point(lambda v: 255 - v)
    img = Image.composite(sfumatura, img, maschera)
    d = ImageDraw.Draw(img)
    r = LATO * 0.38
    c = LATO / 2
    d.ellipse((c - r, c - r, c + r, c + r), fill=(253, 251, 247))
    e = Image.open(RADICE / "strumenti" / "emoji" / f"{emoji}.png").convert("RGBA")
    lato_e = round(LATO * 0.50)
    e = e.resize((lato_e, lato_e), Image.LANCZOS)
    img.paste(e, (round(c - lato_e / 2), round(c - lato_e / 2)), e)
    return img


for cartella, (principale, emoji) in APP.items():
    grande = icona(principale, emoji)
    dest = RADICE / cartella
    dest.mkdir(exist_ok=True)
    for lato, nome in ((180, "icona-180.png"), (512, "icona-512.png"), (64, "icona-64.png")):
        grande.resize((lato, lato), Image.LANCZOS).save(dest / nome, optimize=True)
    print("ok", cartella)
