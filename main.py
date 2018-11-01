import Flask

from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


app.route('/', Method=['POST'])
def index():
    if request.method == "Post":
        

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_confirm = request.form['password_confirm']

        email_error = "Please enter a valid email address"
        username_error="Please enter a valid username (Between 3 and 20 characters with no spaces)"
        password_error="Please enter a password between 3 and 20 characters"
        conirm_error="Passwords do not match"

        def no_char(a):
            if a =='':
                return True
        
        if no_char(username) or len(username) not in range (3,20) or '' in username:
            print = username_error
        if no_char(email):
            if "@" not in email or "." not in email or len(email) not in range(3,20) or " " in email:
                return email_error
        if no_char (password):
            print = (password_error)
        elif len (password) not in range(3,20) or " " in password:
            return password_error
        elif password != password_confirm:
            return confirmation_error
        if not email_error and not username_error and not confirmation_error:
            return redirect ('/Welcome?username={username}'.format (username=username))
        else:
            return render_template('user_signup.html',
                username=username,
                email=email,
                username_error=username_error,
                email_error=email_error,
                password_error=password_error,
                confirmation_error=confirmation_error,
                ) 

@app.route("/Welcome")
def Welcome():
    username=request.args.get('username')
    return render_template('welcome.html',title="Welcome",username=username)   


'''template_dir = os.path.join(os.path.dirname(__file__), 'templates')
@app.route('validate_form', method = ['POST'])
def validate_id():
    id = request.form['id']
    password = request.form['password']
    userid_error = ""
    password_error = ""

app.run
'''