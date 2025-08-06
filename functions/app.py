# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# from openai import OpenAI  # Import the new OpenAI client

# app = Flask(__name__, static_folder='../definitions')
# CORS(app)

# # Initialize the OpenAI client
# client = OpenAI(
#     api_key="your-api-key-here"  # Replace with your actual API key
# )

# @app.route('/api/chat', methods=['POST'])
# def chat():
#     user_message = request.json.get('message', '')

#     try:
#         # Call the OpenAI API using the new client
#         response = client.responses.create(
#             model="gpt-4o-mini",  # Use the appropriate model
#             input=user_message,
#             store=True
#         )
#         bot_response = response.output_text
#     except Exception as e:
#         bot_response = f"An error occurred: {str(e)}"

#     return jsonify({'reply': bot_response})

# @app.route('/')
# def serve_index():
#     return send_from_directory(app.static_folder, 'index.html')

# @app.route('/<path:path>')
# def serve_static(path):
#     return send_from_directory(app.static_folder, path)

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__, static_folder='../definitions')
CORS(app)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_response = response.choices[0].message.content.strip()
    except Exception as e:
        bot_response = f"An error occurred: {str(e)}"

    return jsonify({'reply': bot_response})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
