#This helps us to setup a blueprint file for all the URl/routes and we can create actual functions for routes in seperate files for functional programming

from flask import Blueprint,render_template

#create a blueprint, try to keep names/variables same as file for ease 
views=Blueprint('views',__name__)

#create a basic route with our decorator
@views.route('/')
def home():
    return render_template("home.html")
