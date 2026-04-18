from flask import Blueprint, render_template, request, redirect, session
from db_scripts.queries import get_user, insert_user

auth = Blueprint("auth", __name__)

# 🔐 LOGIN
@auth.route("/login", methods=["GET", "POST"])
def login():
    # If already logged in
    if "user" in session:
        return redirect("/category")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = get_user(username, password)

        if user:
            session["user"] = user["username"]
            return redirect("/category")

        return "Invalid username or password"

    return render_template("login.html")


# 📝 SIGNUP
@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if "user" in session:
        return redirect("/category")

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm = request.form["confirm_password"]

        if password != confirm:
            return "Passwords do not match"

        try:
            insert_user(username, email, password)
        except Exception as e:
            return f"Error: {str(e)}"

        return redirect("/login")

    return render_template("signup.html")


# 🚪 LOGOUT
@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/")

