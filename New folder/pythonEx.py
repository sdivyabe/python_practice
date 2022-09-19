from flask import Flask, render_template

app = Flask(__name__)       #create instance for Flask

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello/welcome")
def welcome():
    return "Welcome Home"

@app.route("/hello/<name>")
def hello(name):
    return "Hello World {}".format(name)

if __name__ == "__main__":          #condition for we r running from main file
    app.run(debug=True)# debug = true for changes reflect in web/url
