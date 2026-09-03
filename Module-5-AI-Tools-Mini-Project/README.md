# Module 5 — AI Tools & Mini Project

## AI Content Assistant

A simple AI-powered web application built as part of **Module 5: AI Tools & Mini Project**. The application uses Google Gemini to help users generate content, summarize text, and improve writing.

## Internship Requirements Covered

- Explored AI tools and their practical uses.
- Demonstrates how AI can assist with writing, productivity, and coding-related workflows.
- Built a simple AI-powered application.
- Uses an AI API to produce useful text results.
- Designed a responsive and beginner-friendly interface.

## Features

- Generate content from an idea
- Summarize text
- Improve grammar, clarity, and professionalism
- Copy the generated result
- Responsive web interface
- API key stored through an environment variable

## Technologies

- Python
- Flask
- Google Gemini API
- HTML5
- CSS3
- JavaScript

## Project Structure

```text
Module-5-AI-Tools-Mini-Project/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Run Locally

1. Install Python.
2. Create a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set the `GEMINI_API_KEY` environment variable.
5. Start the application:

```bash
python app.py
```

6. Open the local Flask address shown in the terminal.

## Important Security Note

Do **not** put a real Gemini API key inside `app.py`, JavaScript, or any file committed to GitHub. Use an environment variable instead.

## Learning Outcome

This mini project demonstrates how AI services can be integrated into a practical web application and used to improve productivity through text generation, summarization, and writing assistance.

## Internship Module

**Module 5 — AI Tools & Mini Project**
