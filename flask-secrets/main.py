from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class Form(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Length(min=8), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, max=24)])
    login = SubmitField(label="Login")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = Form()
    if form.validate_on_submit():
        if form.email.data == "chuthimai3723@gmail.com" and form.password.data == "12345678":
            return success()
        else:
            return denied()
    return render_template('login.html', form=form)


@app.route("/success")
def success():
    return render_template('success.html')


@app.route("/denied")
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)