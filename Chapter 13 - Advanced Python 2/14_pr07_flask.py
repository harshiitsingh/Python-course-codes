# Explore the flask module and create a web server using Flask and Python

# Flask module --> google it

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)  # this is the feature of flask

# you can add html also

# getbootstarp.com --> google it