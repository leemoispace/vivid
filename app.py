#coding:utf-8

#flask-script module Manager class
#from flask.ext.script import Manager
from flask import Flask, jsonify,render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime

app=Flask(__name__)
#manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
	return render_template('index.html',current_time=datetime.utcnow())

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
