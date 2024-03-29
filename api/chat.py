from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask import jsonify
from flask_cors import CORS
from urllib.parse import unquote


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def home():
    return "Flask Vercel Example - Hello World", 200

# Route to get a string as a response after taking input from the user
@app.route('/<message>', methods=['GET'])
@cross_origin()
def get_book(message: str):
    message = unquote(message)
    return jsonify({"message": "I received this message from you: " + message})

if __name__ == '__main__':
    app.run()
