from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
     return render_template('home.html',title='Home')


@app.route('/detail/<initial>')
def show_initial(initial):
    # show the user profile for that user
    # return f'Parameter dari url: {initial}'
      return render_template('test.html',title='Detail Page',initial = initial)
     

@app.errorhandler(404)
def page_not_found(error):
    return render_template('notfound.html',title='Notfound'), 404