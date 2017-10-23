from flask import Flask, request, redirect
import cgi
import jinja2
import os
app = Flask(__name__)
app.config['DEBUG'] = True

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

form  = """
<!doctype html>
<html>
<style>
    .error {{
        color: red;
    }}
</style>
</head>
<body>
<h1>Signup</h1>
<form method="post">
    <table>
        <tr>
            
<form method="post">

<table>

<tr>

<td><label for="username">Username</label></td>

<td>

<input name="username" type="text" value="">

<span class="error">{username_error}</span>

</td>

</tr>

<tr>

<td><label for="password">Password</label></td>

<td>

<input name="password" type="password">

<span class="error">{password_error}</span>

</td>

</tr>

<tr>

<td><label for="verify">Verify Password</label></td>

<td>

<input name="verify" type="password">

<span class="error">{verify_error}</span>

</td>

</tr>

<tr>

<td><label for="email">Email (optional)</label></td>

<td>

<input name="email" value="">

<span class="error">{email_error}</span>

</td>

</tr>

</table>

<input type="submit">

</form>

</html>


"""



hello= "Welcome {username}" 
@app.route('/', methods=['GET', 'POST'])

def valuation():
    if request.method == 'POST':
        error_message=""
        username_error=""
        password_error=""
       
        verify_error=""
        email_error=""

        
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        if not username:
            username_error = "username can't be empty" 
        if not password:
            password_error = "password can't be empty"
        if not verify:
            verify_error = "verify password can't be empty"
        if password != verify :
            verify_error = verify_error + "password doesn't match"
       
        if not is_email(email):
            email_error = "does not seem like an email address"  

        error_message = username_error + password_error + verify_error + email_error
       
        if error_message:
            return form.format(username=username, email=email,password= password, verify = verify, username_error=username_error, email_error=email_error, password_error=password_error, verify_error=verify_error)
        else:
            return hello.format(username=username)
    else:
        #template = jinja_env.get_template('hello_form.html')
        return form.format(email='', email_error='', username= '',password ='', verify='', password_error='', username_error='', verify_error='')



def is_email(string):

    atsign_index = string.find('@')
    atsign_present = atsign_index >= 0
    if not atsign_present:
        return False
    else:
        domain_dot_index = string.find('.', atsign_index)
        domain_dot_present = domain_dot_index >= 0
        return domain_dot_present




app.run()