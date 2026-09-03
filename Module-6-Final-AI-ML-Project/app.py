import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()
app = Flask(__name__)

key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=key) if key else None

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/analyze")
def analyze():
    data = request.get_json() or {}
    resume = data.get("resume", "").strip()
    job = data.get("job", "").strip()

    if not resume or not job:
        return jsonify({"error": "Please fill in both fields."}), 400
    if not client:
        return jsonify({"error": "GEMINI_API_KEY is missing. Add it to .env"}), 500

    prompt = f"""You are an AI Resume Analyzer.
Compare the candidate information with the job description.

CANDIDATE:
{resume}

JOB DESCRIPTION:
{job}

Give:
1. Match Score (0-100%)
2. Matching Skills
3. Missing Skills
4. 3-5 Resume Improvements
5. 5 Interview Questions
6. Short Career Advice

Do not invent qualifications."""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return jsonify({"result": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
