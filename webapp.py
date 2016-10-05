from flask import Flask
from random import randrange
app = Flask(__name__)

@app.route("/")
def hello():
    return str(randrange(1,7))

if __name__ == "__main__":
    app.run()