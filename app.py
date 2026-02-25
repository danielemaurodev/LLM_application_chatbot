from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import json

# Inizializza l'app Flask
app = Flask(__name__)
CORS(app)  # Abilita CORS per tutte le route

# Carica il modello BlenderBot da Hugging Face
model_name = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Memoria semplice della conversazione
conversation_history = []


@app.route("/")
def index():
    """Renderizza la pagina principale con l'interfaccia chatbot."""
    return render_template("index.html")


@app.route("/chatbot", methods=["POST"])
def handle_prompt():
    """Riceve il messaggio dell'utente e restituisce la risposta del modello."""
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data["prompt"]

    history = "\n".join(conversation_history)
    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=60)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    conversation_history.append(input_text)
    conversation_history.append(response)

    return response


if __name__ == "__main__":
    app.run()
