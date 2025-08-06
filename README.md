# CHAT BOT

## How to Run

1. Open terminal and go to the backend folder:
   cd functions

2. Run the Flask server:
   python app.py

3. Open your browser:
   http://127.0.0.1:5000

4. Type a message like "HELLO" to test the chatbot.


## Prerequisites

- Python 3.7 or higher installed
- Install packages:
  pip install flask flask-cors python-dotenv openai

- api_key="your-api-key-here"  # Replace with your actual API key

- Create a .env file in the functions folder with:
  OPENAI_API_KEY=your-api-key


## Troubleshooting

- 404 error:
  → Check Flask server is running
  → Make sure fetch URL in index.html is:
     http://127.0.0.1:5000/api/chat

- CORS error:
  → Install and import flask-cors in app.py