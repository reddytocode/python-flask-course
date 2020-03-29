from flask import Flask

app = Flask(__name__)

@app.route("/project/Flask")
def hello():
    message = "Flask 1.1.1 Information"
    return "<h1 style='color: red;'>{}</h1>".format(message)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
    