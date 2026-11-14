"""Scrive le pagine di avvio: una per app (con la sua icona) e quella iniziale con tutte le app.

Uso:  python3 strumenti/pagine.py
Perché esistono: le app sono web app di Google Apps Script e vivono tutte su script.google.com, dove non si può
scegliere l'icona per la schermata Home. Una pagina di avvio ha la sua icona; aggiunta alla schermata Home (o al
Dock del Mac, o ai Preferiti) apre subito l'app vera.
Trucco: appena la pagina si apre, il suo indirizzo diventa «…/?apri». Quello che si aggiunge alla schermata Home è
quindi «…/?apri», e da lì la pagina passa subito all'app. Aperta senza «?apri» invece si ferma e mostra come fare.
Nelle pagine non ci sono dati: solo il nome dell'app, l'icona e l'indirizzo (le app si aprono solo con l'account
Google autorizzato).
"""
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
APP = [
    # cartella, nome, colore principale, colore scuro (tema scuro), emoji, indirizzo dell'app
    ("biblioteca", "Biblioteca", "#c2410c", "#ea6a2f", "📚",
     "https://script.google.com/macros/s/AKfycby9sT3AXxDnNp8L6LWZEAMh7lWpiHu5ROEZqx2uqfwCbHe1jBOn4217EIVWvc6jECqc/exec"),
    ("scadenzario", "Scadenzario", "#0f766e", "#2dd4bf", "🗓️",
     "https://script.google.com/macros/s/AKfycbxMgx_xTdtthyJe9KrdadNFj6Og7LTTerDSioZIp6JML3u_lRx8TLIRl2XHjDvf_mfB9w/exec"),
    ("contabilita", "Contabilità", "#3d5a80", "#8fb0d9", "🏠",
     "https://script.google.com/macros/s/AKfycbwAJio7woQirvidr26X9C37XtB7m9uU49J13WhWdP1Xv6lyC5-wXlOL8q0bdjclRB5o/exec"),
    ("visualfinance", "VisualFinance", "#4b5694", "#a4acdf", "🌍",
     "https://script.google.com/macros/s/AKfycbxRIxP-_Nq2EMBZPkCISCb7ZCnmBUdOyPvCQ6grkNSTTIFb5CEVgluct2GgN0CrDh2k/exec"),
]

STILE = """
  :root { --bg: #f6f5f2; --surface: #fff; --testo: #1f2328; --tenue: #5b6168; --bordo: #e3e0da; }
  @media (prefers-color-scheme: dark) {
    :root { --bg: #16181b; --surface: #1f2226; --testo: #eceae6; --tenue: #a3a8ae; --bordo: #33373c; }
  }
  * { box-sizing: border-box; }
  body { margin: 0; min-height: 100vh; background: var(--bg); color: var(--testo);
    font: 17px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    display: flex; align-items: center; justify-content: center; padding: 24px 16px; }
  main { width: 100%; max-width: 440px; text-align: center; }
  h1 { font-size: 28px; margin: 14px 0 4px; }
  .icona { width: 112px; height: 112px; border-radius: 26px; box-shadow: 0 6px 20px rgba(0,0,0,.15); }
  .btn { display: inline-block; margin: 18px 0 8px; padding: 13px 28px; border-radius: 12px; font-weight: 600;
    background: var(--accento); color: #fff; text-decoration: none; }
  .scheda { margin-top: 22px; text-align: left; background: var(--surface); border: 1px solid var(--bordo);
    border-radius: 14px; padding: 16px 18px; }
  .scheda h2 { font-size: 15px; margin: 0 0 6px; color: var(--accento); }
  .scheda p { margin: 0 0 12px; }
  .scheda p:last-child { margin-bottom: 0; }
  .tenue { color: var(--tenue); font-size: 14px; }
  a { color: var(--accento); }
"""


def pagina_app(cartella, nome, chiaro, scuro, emoji, indirizzo):
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{nome}</title>
<meta name="apple-mobile-web-app-title" content="{nome}">
<link rel="apple-touch-icon" href="icona-180.png">
<link rel="icon" type="image/png" sizes="64x64" href="icona-64.png">
<link rel="icon" type="image/png" sizes="512x512" href="icona-512.png">
<meta name="theme-color" content="{chiaro}">
<script>
  // Aggiunta alla schermata Home (indirizzo con «?apri»): si va subito all'app.
  var APP = '{indirizzo}';
  if (/[?&]apri\\b/.test(location.search)) location.replace(APP);
  else history.replaceState(null, '', location.pathname + '?apri');
</script>
<style>{STILE}
  :root {{ --accento: {chiaro}; }}
  @media (prefers-color-scheme: dark) {{ :root {{ --accento: {scuro}; }} .btn {{ color: #111; }} }}
</style>
</head>
<body>
<main>
  <img class="icona" src="icona-180.png" alt="">
  <h1>{nome}</h1>
  <a class="btn" href="{indirizzo}">Apri {nome}</a>
  <div class="scheda">
    <h2>Come app sull'iPhone</h2>
    <p>In Safari, da questa pagina: tasto <b>Condividi</b> (il quadrato con la freccia) →
      <b>Aggiungi alla schermata Home</b> → <b>Aggiungi</b>. Sulla schermata Home compare questa icona.</p>
    <h2>Come app sul Mac</h2>
    <p>In Safari, da questa pagina: menu <b>File</b> → <b>Aggiungi al Dock…</b> → <b>Aggiungi</b>.
      La prima volta può chiedere di entrare con l'account Google.</p>
    <p class="tenue">L'app si apre solo con l'account Google autorizzato. Questa pagina non contiene dati.</p>
  </div>
  <p class="tenue"><a href="../">Tutte le app</a></p>
</main>
</body>
</html>
"""


def pagina_iniziale():
    righe = "\n".join(
        f'    <a class="app" href="{c}/" style="--accento:{chiaro}"><img src="{c}/icona-180.png" alt=""><span>{n}</span></a>'
        for c, n, chiaro, _s, _e, _i in APP)
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>App di casa</title>
<style>{STILE}
  :root {{ --accento: #3d5a80; }}
  .elenco {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-top: 20px; }}
  .app {{ display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 16px 6px;
    background: var(--surface); border: 1px solid var(--bordo); border-radius: 16px; color: var(--testo);
    text-decoration: none; font-weight: 600; font-size: 15px; }}
  .app img {{ width: 64px; height: 64px; border-radius: 15px; }}
</style>
</head>
<body>
<main>
  <h1>App di casa</h1>
  <p class="tenue">Ogni app ha la sua pagina: da lì si aggiunge alla schermata Home dell'iPhone o al Dock del Mac,
    con la sua icona.</p>
  <div class="elenco">
{righe}
  </div>
</main>
</body>
</html>
"""


for app in APP:
    (RADICE / app[0]).mkdir(exist_ok=True)
    (RADICE / app[0] / "index.html").write_text(pagina_app(*app))
(RADICE / "index.html").write_text(pagina_iniziale())
print("ok")
