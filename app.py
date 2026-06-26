from flask import Flask, render_template
app = Flask(__name__)

# this code is good pankaj
@app.route('/')
def hello_world():
    return render_template('index.html')
if jnhhrnj:hjgg

@app.route('/health')
def health():
    return 'Server is up and running'
