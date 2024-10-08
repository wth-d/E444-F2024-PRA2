from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
# web forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string' # for wtf web form

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('Email address', validators=[Email()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    # name = None
    form = NameForm()
    if form.validate_on_submit(): # when form is submitted AND validated
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data # store it in session dict instead of in a plain Python variable;
        # form.name.data = ''
        
        if form.email.data.endswith('utoronto.ca'): # endswith instead of find() - mail.utoronto.ca@gmail.com
            session['email'] = form.email.data
        else:
            session['email'] = None
        return redirect(url_for('index'))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'), email=session.get('email'))

@app.route('/user/<name>')
def user(name):
    # return '<h1>Hello, {}!</h1>'.format(name)
    return render_template('user.html', name=name)

# print("app.config is", app.config)

if __name__ == "__main__":
    # app.run("127.0.0.1", port=5000, debug=True)
    app.run("0.0.0.0", port=5000, debug=True)
    # If not specifying --host=0.0.0.0 in Dockerfile's flask run, then have to specify it here instead of 127.0.0.1 ...
