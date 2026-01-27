from flask import Flask,render_template
# it creates an instance of flask class,which will be your wsgi application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><H6>Welcome to this best flask course.you will love it</H6></html>"

@app.route("/index")
def index():
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)  #use debug=true->for dynamic changes .Onclicking refresh,you will see the changes 
