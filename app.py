from flask import Flask, request, jsonify, render_template
from chatbot_logic import answer_query

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = answer_query(user_input)
    return jsonify({'reply': response})

if _name_ == '_main_':
    app.run(debug=True)