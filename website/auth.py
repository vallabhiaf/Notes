from flask import Blueprint,render_template,request

auth=Blueprint('auth',__name__)
#create a basic route with our decorator
#By Default it only allows get request
@auth.route('/login',methods=['GET','POST'])
def login():
    #request contains all the data that was sent to this route via the form (meta data and real data)
    data=request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return '<p>Logout<p>'

@auth.route('/sign-up',methods=['GET','POST'])
def signup():
    #rendering html page with jinga code
    #Jinga can do basic templating
    #we can also pass variables which can be used in jinga code 
    return render_template("signup.html")
