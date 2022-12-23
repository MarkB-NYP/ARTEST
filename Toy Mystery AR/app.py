from flask import Flask, render_template
app = Flask(__name__, template_folder='./',static_url_path='', 
            static_folder='./')

@app.route('/')
def hello_world():
    return render_template('index.html')
