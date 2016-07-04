#coding:utf-8
#已经拆分到app里面各个文件去了
import os

#flask-script module Manager class
from flask.ext.script import Manager, Shell
from flask import Flask, jsonify,render_template,session, redirect, url_for,flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required,Email
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SECRET_KEY'] = 'safekeys'
#数据库
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

#邮件 export MAIL_USERNAME=<Gmail username>
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_SUBJECT_PREFIX'] = '[leemoispace]'
app.config['MAIL_SENDER'] = 'Lrybus Admin <admin@leemoi.space>'


# #在app/__init__.py
# manager = Manager(app)
# bootstrap = Bootstrap(app)
# moment = Moment(app)
# migrate = Migrate(app, db)


# 在app/main/forms.py
#
# #wtf表单.p35还有好多种类,要试一试
# class NameForm(Form):
#     name = StringField('What is your name?', validators=[Required()])
#     email = StringField('What is your email?',validators=[Email()])
#     submit = SubmitField('Submit')

# 根目录的manage.py
# #自动导入对象,
# def make_shell_context():
#     return dict(app=app,db=db,User=User, Role=Role)
# #可以被flask-script调用
# manager.add_command("shell", Shell(make_context = make_shell_context))
# manager.add_command('db', MigrateCommand)
#



# 在app/main/views.py
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user = User(username=form.name.data)
#             db.session.add(user)
#             session['known'] = False
#         else:
#             session['known'] = True
#         session['name'] = form.name.data
#         return redirect(url_for('index'))
#     return render_template('index.html', form=form, name=session.get('name'),
#                            known=session.get('known', False))
    # #name = None
    # form = NameForm()
    # if form.validate_on_submit():
    #     old_name = session.get('name')
    #     if old_name is not None and old_name != form.name.data:
    #         #如果名字变了就闪现信息
    #         flash('Looks like you have changed your name!')
    #     session['name'] = form.name.data
    #     return redirect(url_for('index'))
    #     #name = form.name.data
    #     #form.name.data = ''
    # #重定向,解决刷新重复post
    # return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())
    # #return render_template('index.html', form=form, name=name,current_time=datetime.utcnow(), email=email)
	# #return render_template('index.html',current_time=datetime.utcnow())

# 在app/main/views.py
# # url中的变量
# @app.route('/user/<name>')
# def user(name):
#         #return '<h1>hello,%s!</h1>' %name
#         return render_template('user.html', name=name)
#



# app/main/errors.py
# #自定义错误页面
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'),404
#
# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500
#






if __name__=='__main__':
    #app.run()
	manager.run()
