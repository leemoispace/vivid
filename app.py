#coding:utf-8


from flask import Flask, jsonify,render_template

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

# url中的变量
@app.route('/user/<name>')
def user(name):
        return '<h1>hello,%s!</h1>' %name

if __name__=='__main__':
        app.run()
