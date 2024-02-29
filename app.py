from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import flask_login
import os

load_dotenv()  # take environment variables from .env.

# create app
app = Flask(__name__)

# connect to the database
cxn = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = cxn[os.getenv("MONGO_DB")]  # store a reference to the database

#print(os.getenv("MONGO_DB"))
#print(os.getenv("MONGO_URI"))
#print(db.Users.find_one())
#print(db.Users.insert_one({"username": "Gez G"}))

try:
    # verify the connection works by pinging the database
    cxn.admin.command("ping")  # The ping command is cheap and does not require auth.
    print(" *", "Connected to MongoDB!")  # if we get here, the connection worked!
except Exception as e:
    # the ping command failed, so the connection is not available.
    print(" * MongoDB connection error:", e)  # debug

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

# run app
if __name__ == '__main__':
    app.run()