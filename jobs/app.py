from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    call = render_template("index.html")
    return call
