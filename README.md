# LLM Chatbot Web App (BlenderBot + Flask)

Questo progetto è una semplice **applicazione web** che espone un chatbot basato sul modello `facebook/blenderbot-400M-distill` di Hugging Face, utilizzando un backend Flask e una interfaccia web in HTML/JavaScript.

## Requisiti

- Python 3.9+ (consigliato)
- `pip` installato
- Connessione internet per scaricare il modello al primo avvio

## Installazione

Clona il repository e spostati nella cartella del progetto:

```bash
git clone <URL_DEL_TUO_REPO>.git
cd LLM_application_chatbot

\\crea ambiente virtuale

python -m venv .venv
source .venv/bin/activate      # macOS / Linux
# .venv\Scripts\activate      # Windows PowerShell

\\installa le dipendenze

pip install -r requirements.txt

\\esegui il server Flask

python app.py


\\ ATTENZIONE//
per default l'applicazione sara disponibile a http://127.0.0.1:5000 oppure http://localhost:5000

\\ STRUTTURA DEL PROGETTO //

LLM_application_chatbot/
  app.py              # Backend Flask, API /chatbot e route per la pagina
  static/             # File statici (JS, CSS, immagini)
    script.js
    ...
  templates/          # Template HTML (Flask/Jinja2)
    index.html
  requirements.txt    # Dipendenze Python
  README.md           # Documentazione del progetto


\\NOTA 
Flask utilizza la cartella templates/ per i file HTML (ad esempio index.html) e static/ per JavaScript, CSS e altri asset statici.

\\ Modello utilizzato
Il chatbot usa il modello BlenderBot 400M Distill:

Nome modello: facebook/blenderbot-400M-distill

Modello su Hugging Face: https://huggingface.co/facebook/blenderbot-400M-distill

Il modello viene scaricato automaticamente tramite la libreria transformers al primo avvio dell’applicazione.\\