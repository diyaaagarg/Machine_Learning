from flask import Flask
# it creates an instance of flask class,which will be your wsgi application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "Welcome to this best flask course.you will love it "

@app.route("/index")
def index():
    return "Welcome to the index page"
if __name__=="__main__":
    app.run(debug=True)  #use debug=true->for dynamic changes .Onclicking refresh,you will see the changes 
