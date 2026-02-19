# building url dynamically
# variable rule
# jinja 2 template engine 

# jinja2 template engine:
''' {{}} expressions to print output in html
{%...%}conditions,for loops
{#...#} this is for comments 

'''

from flask import Flask,render_template,request
# it creates an instance of flask class,which will be your wsgi application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><H6>Welcome to this best flask course.you will love it</H6></html>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form2', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}"
    return render_template('form2.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}"
    return render_template('form2.html')

##Variable rule
@app.route('/success/<int:score>')  #here score is in string bydefault
def success(score):
    res=" "
    if score>50:
        res="pass"
    else:
        res="fail"
    return render_template('result.html',results=res)

##Variable rule
@app.route('/successres/<int:score>')  #here score is in string bydefault
def successres(score):
    res=" "
    if score>50:
        res="pass"
    else:
        res="fail"
    exp={'score':score,"res":res}
    return render_template('result1.html',results=exp)

##Variable rule(if condition in result.html)
@app.route('/successif/<int:score>')  #here score is in string bydefault
def successif(score):
    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')  #here score is in string bydefault
def fail(score):
    return render_template('result.html',results=score)
@app.route('/submit',methods=['POST','GET'])
def submit():


if __name__=="__main__":
    app.run(debug=True)  #use debug=true->for dynamic changes .Onclicking refresh,you will see the changes 
