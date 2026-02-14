from flask import Flask, render_template, request, redirect, session, jsonify, url_for
from models import db, Error, User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///errors.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "supersecretkey"

db.init_app(app)

with app.app_context():
    db.create_all()


# -------------------------
# LOGIN KONTROL DECORATOR
# -------------------------
def login_required(route_function):
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return route_function(*args, **kwargs)
    wrapper.__name__ = route_function.__name__
    return wrapper


# -------------------------
# AI ÇÖZÜM
# -------------------------
def generate_solution(description):
    description = description.lower()

    if "database" in description:
        return "Veritabanı bağlantısını kontrol edin."
    elif "timeout" in description:
        return "Sunucu timeout süresini artırın."
    elif "null" in description:
        return "Null kontrolü ekleyin."
    else:
        return "Logları inceleyip hatayı izole edin."


# -------------------------
# LOGIN
# -------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect("/")

    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            session["user_id"] = user.id
            return redirect("/")

        return render_template("login.html", error="Hatalı giriş!")

    return render_template("login.html")


# -------------------------
# REGISTER
# -------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing = User.query.filter_by(username=request.form["username"]).first()
        if existing:
            return render_template("register.html", error="Bu kullanıcı zaten var!")

        hashed_pw = generate_password_hash(request.form["password"])
        new_user = User(username=request.form["username"], password=hashed_pw)

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


# -------------------------
# LOGOUT
# -------------------------
@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/login")


# -------------------------
# DASHBOARD
# -------------------------
@app.route("/")
@login_required
def index():
    errors = Error.query.filter_by(user_id=session["user_id"]).all()

    kritik = Error.query.filter_by(level="Kritik", user_id=session["user_id"]).count()
    orta = Error.query.filter_by(level="Orta", user_id=session["user_id"]).count()
    dusuk = Error.query.filter_by(level="Düşük", user_id=session["user_id"]).count()

    return render_template("index.html", errors=errors,
                           kritik=kritik, orta=orta, dusuk=dusuk)


# -------------------------
# ADD
# -------------------------
@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":

        solution = request.form["solution"]
        if not solution:
            solution = generate_solution(request.form["description"])

        new_error = Error(
            title=request.form["title"],
            description=request.form["description"],
            level=request.form["level"],
            cause=request.form["cause"],
            solution=solution,
            user_id=session["user_id"]
        )

        db.session.add(new_error)
        db.session.commit()

        return redirect("/")

    return render_template("add.html")


# -------------------------
# DELETE
# -------------------------
@app.route("/delete/<int:id>")
@login_required
def delete(id):
    error = Error.query.get_or_404(id)
    db.session.delete(error)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5050)
