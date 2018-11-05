from flask import Flask, request, redirect, render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def signup():
        return render_template('home-page.html')

@app.route('/welcome')
def welcome():
    name=request.args.get('name')
    template = jinja_env.get_template('base.html')
    return template.render()

        

@app.route('/', methods=['POST'])
def user_signup():

    
    password = request.form['password']
    passwordVer = request.form['verPass']
    userName = request.form['username']
    email = request.form['Email']
    
    password_error = ''
    passwordVerf_error = ''
    email_error = ''
    username_error = ''

    if len(email)==0:
        email_error = ''

    
    elif email.count('@')!=1 or email.count('.')!=1:
	
	#re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
       # email = email
   # else:
        email_error = "Email is invalid"

    if userName=='':
        username_error = 'You must enter a user Name'
    
    elif " " in userName:
        username_error = 'No spaces allowed in the User Name'
    elif  len(userName)<3 or len(userName)>20:
        username_error = 'Username must be between 3 and 20 characters'

    if password=='':
        password_error= 'You must enter a password!'

    elif " " in password:
        password_error = 'No spaces allowed in the password'   

    elif  len(password)<3 or len(password)>20:
        password_error = 'Password must be between 3 and 20 characters'    

    if password != passwordVer:
        password_error = 'The Verfication password must match your password'
    elif passwordVer=='':
        passwordVerf_error= 'You must enter a Verification password also!' 



    if not password_error and not username_error and not passwordVerf_error and not email_error:
        
        
        return render_template('welcome.html', name=userName)
    
    
	
    else:
        
        return render_template('home-page.html', password_error=password_error,
            email_error=email_error,username_error=username_error,passwordVerf_error=passwordVerf_error,
            username=userName,
            email=email)

app.run()