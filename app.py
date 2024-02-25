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

# profile page
@app.route('/profile')
def profile():
    return render_template('profile.html')

# picture history page
@app.route('/history')
def history():
    return render_template('history.html')

# account creation page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# picture change page
@app.route('/change-pfp')
def signup():
    return render_template('change-pfp.html')

# account deletion page
@app.route('/delete-account')
def signup():
    return render_template('delete-account.html')

# run app
if __name__ == '__main__':
    app.run()