from flask import Blueprint,render_template

auth=render_template('auth',__name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return '<p>Logout<p>'

@auth.route('/sign-up')
def login():
    return render_template("sign_up.html")
