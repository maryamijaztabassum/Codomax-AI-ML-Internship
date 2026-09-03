import os
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY) if API_KEY else None

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/generate")
def generate():
    if not client:
        return jsonify({
            "error": "GEMINI_API_KEY is not configured. Add your API key as an environment variable."
        }), 500

    data = request.get_json(silent=True) or {}
    task = data.get("task", "").strip()
    text = data.get("text", "").strip()

    if not task or not text:
        return jsonify({"error": "Please select a task and enter some text."}), 400

    prompts = {
        "generate": f"Create clear, useful content based on this idea:\n{text}",
        "summarize": f"Summarize the following text in concise bullet points:\n{text}",
        "improve": f"Improve the grammar, clarity, and professionalism of this text while preserving its meaning:\n{text}"
    }

    if task not in prompts:
        return jsonify({"error": "Invalid task selected."}), 400

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompts[task]
        )
        return jsonify({"result": response.text})
    except Exception as exc:
        return jsonify({"error": f"AI request failed: {exc}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
