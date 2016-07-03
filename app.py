#coding:utf-8

#flask-script module Manager class
#from flask.ext.script import Manager
from flask import Flask, jsonify,render_template
from flask.ext.bootstrap import Bootstrap

app=Flask(__name__)
#manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

# url中的变量
@app.route('/user/<name>')
def user(name):
        return '<h1>hello,%s!</h1>' %name

if __name__=='__main__':
        app.run()
	#manager.run()
