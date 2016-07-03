from flask import Flask, jsonify
app=Flask(__name__)

@app.route('/')
def index():
        return 'vivid is beautiful,auto root restart'

@app.route('/data')
def name():
        data={"names":["John","Jacob"]}
        return jsonify(data)

if __name__=='__main__':
        app.run()
