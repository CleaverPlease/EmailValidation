from flask import Flask, render_template, redirect, session, request, flash
from connect import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'cleaverPlease'
mysql = MySQLConnector(app, 'emails')
# print mysql_query_db('SELECT * FROM user')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():

    # if len(request.form['email']) < 1:
    #     flash('Must enter an email!')
    # elif not EMAIL_REGEX.match(request.form['email']):
    #     flash('Invalid email')
    # else:
        query = "INSERT INTO emails (email, created_at, update_at) VALUES ('{}', NOW(), NOW());".format(request.form['email'])
        # data = {'email': request.form['email']}
        session['email']=request.form['email']
        mysql.query_db(query)
        return redirect('/success')
    # return redirect('/')

@app.route('/success')
def success():
    query = 'SELECT * FROM emails'
    emails = mysql.query_db(query)
    print 'emails' + str(emails)
    return render_template('success.html', emails=emails)

app.run(debug=True)
