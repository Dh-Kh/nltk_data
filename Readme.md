# Test Task FastAPI-NLTK

This project provides a simple RESTful API for performing basic natural language processing (NLP) tasks using the FastAPI framework and the NLTK library. It currently supports the following operations:

- **Tokenization:**  Split text into words or sentences.
- **Part-of-Speech (POS) Tagging:**  Identify the grammatical role of each word in a sentence.
- **Named Entity Recognition (NER):**  Identify named entities (people, organizations, locations, etc.) in text.

## Prerequisites

- Python 3.7 or higher
- Virtual environment (recommended)
- NLTK library and data

```bash

git clone https://github.com/Dh-Kh/nltk_data.git

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 main.py

```

# Access the interactive API documentation:

Open your web browser and navigate to http://127.0.0.1:8000/docs.
You'll find a user-friendly interface (Swagger UI) that allows you to test the API endpoints directly from your browser.

### Project Structure
```bash
.
├── main.py
├── Readme.md
└── requirements.txt
```