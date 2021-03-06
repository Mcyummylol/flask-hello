#--------------Flask Hello World-----------#
import os
#import the Flask class from flask module
from flask import Flask

#create the application object
app = Flask(__name__)

#use decorators to link the function to an url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello World!"
    
#Dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

#start the develepment server using the run() method
if __name__ == "__main__":
    app.run(host=os.environ['IP'],port=int(os.environ['PORT']))