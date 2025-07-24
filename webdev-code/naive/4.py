from flask import Flask, request
app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_code():
    code = request.form['code']
    result = eval(code)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
