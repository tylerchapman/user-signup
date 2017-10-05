from flask import Flask, render_template, request
app = Flask(__name__)

error_message = ""
username_error_message = "The username was not valid"
password_error_message = "The password is not valid"
matching_password_error_message = "Your passwords do not match"
username_error = False
password_error = False
matching_error = False

def valid_username(username):
    if len(username) >= 3 and len(username) <= 20:
        for letter in username:
            if letter == ' ':
                return False
        return True
    else:
        return False


def matching_passwords(password, verify_password):
    if password == verify_password:
        return True
    else:
        return False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    username = str(username)
    password = request.form['password']
    password = str(password)
    verify_password = request.form['verify-password']
    verify_password = str(verify_password)

    if valid_username(username) and matching_passwords(password, verify_password):
        return render_template('welcome.html', username=username)
    elif not valid_username(username):
        return render_template('index.html', username_error=True, username_error_message=username_error_message)
    elif not matching_passwords(password, verify_password):
        return render_template('index.html', matching_error=True, matching_password_error_message=matching_password_error_message, username=username)


app.run()
