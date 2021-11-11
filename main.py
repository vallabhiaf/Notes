from website import create_app
'Main file to run the web server for our Notes Web App '
app=create_app()

#This line states that we only need to run line 7 if this file is run independently and not imported from another file 
if __name__ == '__main__':
    #debug=True rerun after every change
    app.run(debug=True)