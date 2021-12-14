from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from . import db
#Hash does not have a inverse 
from werkzeug.security import generate_password_hash,check_password_hash
auth=Blueprint('auth',__name__)
#create a basic route with our decorator
#By Default it only allows get request
@auth.route('/login',methods=['GET','POST'])
def login():
    #request contains all the data that was sent to this route via the form (meta data and real data) and is shared as immutable multidict to the backend
    #data=request.form
    #print(data)
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')

        #query the databse

        user=User.query.filter_by(email=email).first()

        if user:
            #Hash the the incoming password and compare with stored result
            if check_password_hash(user.password,password):
                flash('Logged In Succefully',category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password',category='error')
        else:
            flash('User does not exist ',category='error')



    return render_template("login.html")

@auth.route('/logout')
def logout():
    return '<p>Logout<p>'

@auth.route('/sign-up',methods=['GET','POST'])
def signup():
    #rendering html page with jinga code
    #Jinga can do basic templating
    #we can also pass variables which can be used in jinga code 

    #basic checks for data from form

    if request.method == 'POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        #flash is used to show temporary messages along the help of jinga

        user=User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists',category='error')
        elif len(email)<4:
            flash('Email must be greater than 3 character',category='error')
        elif len(firstName)<2:
            flash('Name must be greater than 1 character',category='error')
        elif password1 != password2:
            flash('Name must be greater than 1 character',category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 character',category='error')
        else:
            new_user=User(email=email,first_name=firstName,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Success registration',category='success')
            #goes to blueprint and function name 
            return redirect(url_for('views.home'))


        
        
    return render_template("signup.html")
