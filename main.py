from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello India"

@app.route("/Upper") 
def upper():
    args = request.args
    input = args.get("input") 
    return input.upper()

if __name__ == "__main__":
    app.run()
