from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/gen_url')
def gen_url():
    param = request.args.get('param', '')
    url = f'/next?data={param}'
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)
