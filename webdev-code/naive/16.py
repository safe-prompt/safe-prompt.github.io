from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/render', methods=['POST'])
def render():
    template = request.form['template']
    return render_template_string(template, autoescape=False)

if __name__ == '__main__':
    app.run(debug=True)
