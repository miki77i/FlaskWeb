from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def slide1():
    return render_template("s1.html")

@app.route("/s2")
def slide2():
    return render_template("s2.html")

@app.route("/s3")
def slide3():
    return render_template("s3.html")

if __name__ == "__main__":
    app.run(debug=True)