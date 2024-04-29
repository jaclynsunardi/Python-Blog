from flask import Flask, render_template, request, redirect, url_for
 
app = Flask(__name__)
 
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET'])

def signup():
    return render_template('signup.html')

@app.route('/login', methods=["GET"])

def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)