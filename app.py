from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/")
def home():
    name = input("Enter your name: ")
    data = {"name": name}
    return render_template("home.html", data = {"name": name})

@app.route("/about", methods=['GET', 'POST'])
def about():

    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['numb2'])
        result = num1 + num2
        
        return render_template("about.html", dicti={'result': result})
    else:
        return render_template("about.html", dicti={'result': 'result'})

if __name__ == "__main__":
    app.run(debug=True)