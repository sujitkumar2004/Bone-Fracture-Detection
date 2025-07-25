# 🔗 URL Shortener Assignment

A lightweight URL shortening service built using Python and Flask. This backend-only project provides URL shortening, redirection, click tracking, and stats — all using in-memory storage without a database.

## ✅ Features

- 🔐 Shortens any valid URL to a unique 6-character code  
- 🔁 Redirects to the original URL using the short code  
- 📊 Tracks number of times each short link is visited  
- 📈 Returns analytics (original URL + click count)  
- 💾 In-memory storage (resets when server restarts)  
- ⚠️ Proper error handling and edge case coverage  
- 🧪 Includes 5 unit tests for core functionality  

## 📦 API Endpoints

### 1. POST /api/shorten

Shortens a valid URL.

Request:
{
  "url": "https://example.com"
}

Response:
{
  "short_code": "rXKW7P",
  "short_url": "http://localhost:5000/rXKW7P"
}

---

### 2. GET /<short_code>

Redirects to the original URL if the short code exists.

Example:
GET http://localhost:5000/rXKW7P

Behavior:
- Redirects (HTTP 302) to https://example.com
- Increments click count for analytics

---

### 3. GET /api/stats/<short_code>

Returns the original URL and total clicks.

Response:
{
  "original_url": "https://example.com",
  "clicks": 3,
  "created_at": "2025-07-24T10:35:12"
  
}

## ▶️ How to Run Locally

### 1. Clone the Repository
git clone <your-repo-url>
cd url-shortener

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Start the Server
python app/main.py

Server will run at: http://localhost:5000

## 🧪 Running the Tests

This project uses pytest with 5 unit tests for:

- URL shortening
- Invalid URL handling
- Redirection logic
- Click counting
- Stats fetching

Run all tests:
pytest

## 🗂️ Project Structure

url-shortener/
├── app/
│   ├── main.py        # Entry point & route definitions
│   ├── utils.py       # URL validation logic
│   └── storage.py     # In-memory store & analytics
├── tests/
│   └── test_basic.py  # Pytest test cases
├── requirements.txt   # Flask, Pytest
└── README.md          # This file

## 🛠 Tech Stack

- Backend: Python + Flask  
- Testing: Pytest  
- Storage: In-memory dictionaries (no DB)

## 👤 Author

Sujit Kumar  
B.Tech , IIT Patna

## 📝 Notes

- This project was developed as part of a backend development assignment.
- All data is reset on server restart (no persistence).
