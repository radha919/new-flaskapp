from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.visits = 0
app.bg_color = "white"

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form.get("name")
        return redirect("/hello/" + name)
    else:
        return render_template("index.html", message="Hello World", visits=app.visits, bg_color=app.bg_color)

@app.route("/hello/<name>")
def greet(name):
    app.visits += 1
    return render_template("greet.html", name=name, visits=app.visits, bg_color=app.bg_color)

if __name__ == "__main__":
    app.run()
