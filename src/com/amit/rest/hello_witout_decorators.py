from flask import Flask

def hello_world():
    return "Hello, World!"

app = Flask(__name__)

app.add_url_rule('/hello', 'hello', hello_world)

if __name__ == "__main__":
    app.run()
