from flask import Flask, render_template, redirect

# create app
app = Flask(__name__)

# home page redirects to login page
@app.route('/')
def index():
    return redirect('/login', code=301)

# login page
@app.route('/login')
def login():
    return render_template('login.html')

# run app
if __name__ == '__main__':
    app.run()