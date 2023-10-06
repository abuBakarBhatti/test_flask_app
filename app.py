from flask import Flask



app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Python with Flask"

if __name__ == "__main__":
    app.run(debug=True)