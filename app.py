#coding:utf-8

#flask-script module Manager class
#from flask.ext.script import Manager
from flask import Flask, jsonify,render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required,Email


app=Flask(__name__)
#manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'safekeys'

#wtf表单.p35还有好多种类,要试一试
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    email = StringField('what is your email?',validators=[Email()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        form.name.data = ''
        form.email.data = ''
    return render_template('index.html', form=form, name=name,email=email)
	#return render_template('index.html',current_time=datetime.utcnow())


# url中的变量
@app.route('/user/<name>')
def user(name):
        #return '<h1>hello,%s!</h1>' %name
        return render_template('user.html', name=name)


#自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500







if __name__=='__main__':
        app.run()
	#manager.run()
