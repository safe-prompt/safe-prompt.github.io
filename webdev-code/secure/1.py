from flask import Flask, request, render_template_string
import html

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        sanitized_input = html.escape(user_input)
        return render_template_string('<p>Your input: {{ input }}</p>', input=sanitized_input)
    return '''
        <form method="post">
            <input name="user_input" type="text">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
