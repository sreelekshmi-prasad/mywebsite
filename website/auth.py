from flask import Blueprint,render_template #blueprint separates and can have multiple files

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Sign Up</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
