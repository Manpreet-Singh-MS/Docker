import time
from flask import Flask

app = Flask(__name__)

START = time.time()

def elasped():
    running = time.time() - START
    minutes,seconds  = divmod(running,60)
    hours,minutes = divmod(running,60)
    return "%d:%02d:%02d" % (hours,minutes,seconds)

@app.route("/")

def root():
    return "Hello Python (uptime: %s)" %elasped()

if __name__ == "__main__":
    app.run(debug=True,host= "0.0.0.0",port=8070)
