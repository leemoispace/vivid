from flask import Flask, jsonify
app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/data')
def name():
        data={"names":["John","Jacob"]}
        return jsonify(data)

if __name__=='__main__':
        app.run()
