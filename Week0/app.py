from flask import Flask

app = Flask(__name__)

@app.route('/') ##http://www.google.com/ redirects to www.google.com
def home():
    return "Hello, world!"

"""
cmd line 1: python app.py  --> does not work (WHY?)

cmd line 2: set FLASK_APP = app.py
            flask run --> works but with warning:
                
                "Warning: Silently ignoring app.run() because the 
                application is run from the flask command line executable.
                Consider putting app.run() behind an if __name__ == "__main__" 
                guard to silence this warning."
"""

# now with the if statement there is no warning
if __name__ == "__main__":
    app.run(port = 5000)