from flask import Flask, request
app = Flask(__name__)

comments = []

@app.route('/comment', methods=['POST'])
def comment():
    text = request.form['text']
    comments.append(text)
    return f'<div>{text}</div>'

if __name__ == '__main__':
    app.run(debug=True)
