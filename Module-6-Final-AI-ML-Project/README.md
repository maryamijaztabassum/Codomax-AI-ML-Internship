# AI Resume Analyzer

Final AI & ML project using Flask and Google Gemini AI.

## Features
- Resume/job matching
- AI match score
- Matching and missing skills
- Resume improvement suggestions
- Interview questions
- Career advice
- Responsive web interface

## Run locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:
```env
GEMINI_API_KEY=your_actual_api_key
```

Run:
```bash
python app.py
```

Open `http://127.0.0.1:5000`.

Never upload `.env` to GitHub.
