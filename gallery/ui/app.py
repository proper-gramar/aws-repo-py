from flask import Flask
from flask import request
from flask import render_template
import json
import psycopg2
import db as f
import re

app = Flask(__name__)

#################################
###db.py contents running here###
#################################

### establishes connection to postgreSQL database
db_host = "image-gallery.cs4qwvqazvut.us-west-1.rds.amazonaws.com"
db_name = "image_gallery"
db_user = "image_gallery"

password_file = "/home/ec2-user/.image_gallery_config"


def get_password():
    f = open(password_file, "r")
    result = f.readline()
    f.close()
    return result[:-1]


def get_host(secret):
    return secret['host']


def get_username(secret):
    return secret['username']


def get_dbname(secret):
    return secret['database_name']


def connect():
    global connection
    connection = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=get_password())
    connection.set_session(autocommit=True)


def execute(query, args=None):
    global connection
    cursor = connection.cursor()
    if not args:
        cursor.execute(query)
    else:
        cursor.execute(query, args)
        return cursor


####################
###class examples###
####################

@app.route('/')
def main_panel():
    return """
<!DOCTYPE html>
<html>
   <head>
      <title>Hello</title>
      <meta charset="utf-8" />
   </head>
   <body>
     <h1>Hello, Grant!</h1>
        <a href="/admin">Admin Panel</a>
        <a href="/upload">Upload Image</a>
        <a href="/view">View Images<a/>
   </body>
</html>
"""

@app.route('upload')
def upload():
    #need to upload to S3 bucket
    return 0

@app.route('/view')
def view():
    #needs to query S3, return images owned.
    return 0


@app.route('/goodbye')
def goodbye():
    return 'Goodbye'


@app.route('/greet/<name>')
def greet(name):
    return 'Nice to meet you ' + name


@app.route('/add/<int:x>/<int:y>')  # , methods = ['GET'])
def add(x, y):
    return 'The sum is ' + str(x + y)


@app.route('/mult', methods=['POST'])
def mult():
    x = request.form['x']
    y = request.form['y']
    return 'The product is ' + str(x * y)


@app.route('/calculator/<personsName>')
def calculator(personsName):
    return render_template('calculator.html', name=personsName)


####################
### M3 Functions ###
####################

###admin landing page, only accessible by admin###
@app.route('/admin')
def admin():
    return render_template('adminLanding.html')

#needs to be accessed by admin only
@app.route('/admin/users')
def users():
    return "hello"

### needs to parse data  from url ###
@app.route('/admin/addUsers')  # ,methods = ['POST'])
def addUser():
    # username = input('Username> ')
    # full_name = input('full name> ')
    # password = input('password> ')
    # insert = execute('INSERT username, full_name, password INTO users')
    # get_template(test_template)
    return render_template('addUserTemplate.html')


@app.route('/login')  # login landing page
def login():
    return render_template('loginLanding.html')


###submit user function###
def submitUser():
    connect()
    cursor = connection.cursor()
    cursor.execute('insert username, full_name, password into user')


###@app.route('/admin/listUsers') #, methods['GET'])###
def listUsers():
    res = execute('select username, full_name from users')
    for row in res:
        print(row[0] + "   " + row[1])
    print('')


###kinda busted... lists users as a string object. parse to string??###
@app.route('/admin/listUsers', methods=['GET'])
def userList():
    connect()
    cursor = connection.cursor()
    cursor.execute('select username, full_name from users')
    rows = cursor.fetchall()
    return (str(rows))


###delete method ###
@app.route('/admin/delete')  # , methods['DELETE'])
def delete():
    return ('returns delete link next to user')


### edit user ### needs to query sql and patch entry
@app.route('/admin/modifyUsers')  # , methods['PATCH'])
def modifyUsers():
    return ('modified user panel')
