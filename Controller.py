from flask import Flask, request, redirect, render_template, session, flash
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hiya Sammy!"
if __name__ == "__main__":
    app.run()

