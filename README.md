# 🔗 URL Shortener Assignment

A lightweight URL shortening service built using Python and Flask. This project implements core backend functionality including URL shortening, redirection, click tracking, and analytics — all using in-memory storage without any database.

---

## ✅ Features

- Shortens any valid URL to a unique 6-character code
- Redirects to the original URL via short code
- Tracks number of times each short link is visited
- Returns stats (click count, original URL)
- In-memory storage (resets on server restart)
- Comprehensive error handling
- 5 unit tests for key functionalities

---

## 📦 API Endpoints

### 1. `POST /api/shorten`

Shortens a valid URL.

#### Request:
```json
{
  "url": "https://example.com"
}
Response:
json
Copy
Edit
{
  "short_code": "abc123",
  "short_url": "http://localhost:5000/abc123"
}
2. GET /<short_code>
Redirects to the original URL if the short code exists.

Example:
bash
Copy
Edit
GET http://localhost:5000/abc123
Behavior:
Redirects (HTTP 302) to https://example.com

Increments click count

3. GET /api/stats/<short_code>
Returns the original URL and number of times it has been accessed.

Response:
json
Copy
Edit
{
  "original_url": "https://example.com",
  "clicks": 3
}
🧪 Running the Tests
This project includes 5 tests located in tests/test_basic.py. These tests cover:

URL shortening

Invalid URL handling

Redirection

Click counting

Stats fetching

Run tests using:
bash

Copy

Edit

pytest

▶️ How to Run Locally

1. Clone the Repository
bash
Copy
Edit
git clone <repo-url>
cd url-shortener

2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Start the Server
bash
Copy
Edit
python app/main.py
Server will start at: http://localhost:5000

🧾 File Structure
bash
Copy
Edit
url-shortener/
├── app/
│   ├── main.py        # Entry point & route definitions
│   ├── utils.py       # URL validation logic
│   └── storage.py     # In-memory store & analytics
├── tests/
│   └── test_basic.py  # Pytest test cases
├── requirements.txt   # Flask, Pytest
└── README.md          # This file
🛠 Tech Stack
Backend: Python, Flask

Testing: Pytest

Storage: In-memory dictionaries

✍️ Author
Sujit Kumar
B.Tech CSE, IIT Patna