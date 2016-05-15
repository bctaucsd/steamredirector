import os
from flask import render_template, redirect
from app import app


#!flask/bin/python

# app.run(debug=True)
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)



# square = 5
@app.route('/')
@app.route('/index')
def index():
    print "hello world"
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
@app.route('/<game_name>/<int:square>')
def index2(square,game_name):
    print "----------------------------------------"
    print square
    print "----------------------------------------"
    return render_template("button.html", square=square,game_name=game_name)
@app.route('/<int:square>')
def index3(square):
    print "----------------------------------------"
    print square
    print "----------------------------------------"
    return render_template("button_alt.html", square=square)
@app.route('/<game_name>/<int:square>/<image_url>')
def index4(square,game_name,image_url):
    print "----------------------------------------"
    print square
    print "----------------------------------------"
    return render_template("button_alternate.html", square=square,game_name=game_name,image_url=image_url)

    # return redirect('steam://store/'+str(square),302)