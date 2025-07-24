from flask import Flask, render_template_string, request
import html

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    template_input = request.form.get('input', '')
    sanitized = html.escape(template_input)
    return render_template_string('<p>{{ input }}</p>', input=sanitized)

if __name__ == '__main__':
    app.run(debug=True)
