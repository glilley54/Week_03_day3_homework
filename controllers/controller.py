from app import app
from modules import calculator


@app.route("/")
def index():
    return "Hello and welcome to the best calulator website on planet earth!!!"

@app.route("/add/2/3")
def add():
    return add
