from flask import Flask,session,render_template,request,redirect
from flask_session import Session


app = Flask(__name__)

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

books = {
    '0':"The Hitchhiker's Guide to the Galaxy",
    '1':"The Restaurant at the End of the Universe",
    '2':"Life, the Universe and Everything"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cart",methods=["POST","GET"])
def cart():
    if "cart" not in session:
        session["cart"] = []
    if request.method =="POST":
        id = request.form.get("title")
        if id:
            session["cart"].append(request.form.get("title"))
        return redirect("/cart")
    cart = []
    for j in session['cart']:
        cart.append(books[j])
    return render_template("cart.html",cart=cart )
