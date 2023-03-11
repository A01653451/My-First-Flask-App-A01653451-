from flask import Flask, request,render_template,redirect,url_for
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre= request.form["usuario"]
        contra= request.form["password"]
        
        if (nombre ==nombre.capitalize()) and (contra.isalnum()):
            return f"Hello {nombre}"
        return  redirect(url_for("index"))
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
