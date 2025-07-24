from flask import Flask
app = Flask(__name__)

@app.route('/error')
def error():
    try:
        1 / 0
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
