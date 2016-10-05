from flask import Flask
from random import randrange
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return str(randrange(1,7))

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=port)
    