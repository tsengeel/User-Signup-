from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True



time_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>signup</h1>
    <form method='POST'>
   
        <label>email
            <input name="email" type="text" value='{email}' />
        </label>
        <p class="error">{email_error}</p>
        <input type="submit" value="Validate" />
    </form>
    """
@app.route("/")
def validate():
    return time_form.format( email='', email_error= '' ) 
@app.route("/")






@app.route("/", methods =['POST'])
def valid():

    email = request.form['email']
    email_error = ''

   
    if not is_email(email):
            email_error = "does not seem like an email address"          
            email = ''


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