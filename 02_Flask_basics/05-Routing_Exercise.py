# Set up your imports here!
# import ...
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('') # Fill this in!
def index():
    # Welcome Page
    return "<h1>Go to puppy_name/name to see the result!"
    # Create a generic welcome page.

    pass

@app.route('/puppy_name/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    pupname = ''

    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        puppylatin = name + 'y'
    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    pass

if __name__ == '__main__':
    # Fill me in!
    pass 

