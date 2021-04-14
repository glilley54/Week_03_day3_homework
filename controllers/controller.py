from app import app
from models.sum import calculator


@app.route("/")
def index():
    return "Hello and welcome to the best calulator website on planet earth!!!"

@app.route("/add/<index>/<index>")
def add(add):
    
    return 
