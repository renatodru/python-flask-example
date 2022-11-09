from flask import Flask
import os

app = Flask(__name__)

porta = os.environ.get("APP_PORT")

cont = 0 

@app.route("/")
def hello_world():
    return "Renato Regis"

@app.route("/health")
def health():
    return """<h1>Working!!!</h1>\n<h2>Renato Regis</h2>"""

@app.route("/counter")
def counter():
    global cont
    cont += 1
    return str(cont)

#app-flask:2.0.0
@app.route("/version")
def counter_route():
    return '2.0.0'

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=porta, debug=True)