# !* author: omoshirokunai

# --------------------
# ?? imports
# --------------------
from flask import Flask, render_template, send_from_directory, request
import os
# import json

# --------------------
# ?? env_vars
# --------------------

app = Flask(__name__)


# --------------------
# ?? pages
# --------------------
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/account")
def account():
    return render_template('account.html')

# --------------------
# ?? login/logout
# --------------------
@app.route("/signup")
def signup():
    return render_template('Signup.html')



# --------------------
# ?? errors
# --------------------
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):

    return render_template("500.html"), 500


# --------------------
# ?? favicon/robots.txt
# --------------------
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/robots.txt")
def robots():
    return send_from_directory(app.static_folder, request.path[1:])

#? take data from python to js
# data = "teststringjsklgkslf" 
# return render_template('index.html', data = json.dumps(data))

if __name__ =='__main__':
    app.run(debug=False)