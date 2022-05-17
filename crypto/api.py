from flask import Flask, request
from cryptography import rot13

app = Flask(__name__)


@app.route("/api/encryptions/rot13", methods=['POST'])
def hello_world():
    data = request.get_json()
    plaintext = data['plaintext']
    return {'ciphertext': rot13(plaintext)}
