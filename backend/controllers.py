from flask import Flask, render_template
from flask import current_app as app #Alias for current running app


@app.route("/") #it refers url 127.0.0.1:5000
def home():
    return '''<h2>Welcome to Kanban app</h2>
            <a href ="login">click here for login</a><br>
            <a href ="register">click here for Signup</a>
            '''

@app.route("/login") #it refers base url+/login
def user_login():
    return  render_template("login.html")

@app.route("/register") #it refers base url+/login
def user_signup():
    return  render_template("signup.html")