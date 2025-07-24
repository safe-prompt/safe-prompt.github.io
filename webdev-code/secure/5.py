from flask import Flask, render_template_string, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
csrf = CSRFProtect(app)

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        return render_template_string('<p>Hello, {{ name }}!</p>', name=form.name.data)
    return render_template_string('''
        <form method="post">
            {{ form.csrf_token }}
            {{ form.name.label }} {{ form.name() }}
            {{ form.submit() }}
        </form>
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
