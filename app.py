from flask import Flask, session, redirect, url_for
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/board')
def to_index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

app.config ['SECRET_KEY']='some string no one can guess'
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit=SubmitField('Submit')

@app.route('/show_form',methods=['GET','POST'])
def show_form():
    myform=NameForm()
    if myform.validate_on_submit():
        session['name']=myform.name.data
        return redirect(url_for('show_form'))
    return render_template('form.html',form=myform,name=session.get('name'))


if __name__ == '__main__':
    app.run()
