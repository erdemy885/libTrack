from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return request.form['username'] + " " + request.form['password']
    if request.method == 'GET':
        return render_template('credentials.html', title="Sign up", current_url=request.url)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)