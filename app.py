from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# create app
app = Flask(__name__)

# configure MongoDB connection
#app.config['MONGO_URI'] = ''  # Update with actual MongoDB URI
#mongo = PyMongo(app)

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
    # users = mongo.db.users
    # user_data = users.find_one({'username': username}) Example query, replace with dynamic username
    # return render_template('profile.html', user=user_data)

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
def change_pfp():
    return render_template('change-pfp.html')

# account deletion page
@app.route('/delete-account')
def delete_account():
    return render_template('delete-account.html')

# Error pages
@app.errorhandler(404)
@app.errorhandler(500)
def error_page(error):
    error_code = error.code
    if error_code == 404:
        error_description = "Page not found"
    else:
        error_description = "Internal server error"
    return render_template('error.html', error_code=error_code, error_description=error_description), error_code

# run app
if __name__ == '__main__':
    app.run()