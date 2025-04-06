# FILE: /vidlearn/vidlearn/proto.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/book-of-mormon', methods=['GET'])
def book_of_mormon():
    return render_template('book_of_mormon.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=False)