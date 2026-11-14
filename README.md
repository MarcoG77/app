# Pagine di avvio delle app

Una paginetta per app (Biblioteca, Scadenzario, Contabilità), con la sua icona, pubblicata su GitHub Pages.
Le app sono web app di Google Apps Script e stanno tutte su script.google.com, dove l'icona per la schermata
Home non si può scegliere: aggiunta alla schermata Home dell'iPhone (o al Dock del Mac) dalla sua pagina di avvio,
ogni app ha la sua icona e si apre subito.

- `strumenti/icone.py` disegna le icone (colore dell'app + emoji Noto, licenza Apache 2.0);
  serve Pillow (`../Software contabilità (Claude)/.venv/bin/python strumenti/icone.py`).
- `strumenti/pagine.py` scrive le pagine (nomi, colori, indirizzi delle app).
- Appena aperta, la pagina cambia il suo indirizzo in `…/?apri`: è quello che finisce sulla schermata Home, e da lì
  si va subito all'app. Senza `?apri` mostra come aggiungerla.

Nessun dato: solo nomi, icone e indirizzi. Le app si aprono solo con l'account Google autorizzato.
