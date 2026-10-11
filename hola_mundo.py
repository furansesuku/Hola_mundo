from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Hola mundo</h1>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8200)