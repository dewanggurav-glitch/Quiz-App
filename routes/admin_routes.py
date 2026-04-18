from flask import Blueprint, render_template, request, redirect, session
from models.db import get_db_connection


admin = Blueprint("admin", __name__)

# ADMIN LOGIN
@admin.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            session["admin"] = True
            return redirect("/admin")

        return "Invalid admin credentials"

    return render_template("admin-login.html")


# ADMIN DASHBOARD
@admin.route("/admin")
def dashboard():
    if "admin" not in session:
        return redirect("/admin-login")
    return render_template("admin-dashboard.html")


@admin.route("/add-question", methods=["GET", "POST"])
def add_question():

    if request.method == "POST":
        question = request.form["question"]
        op1 = request.form["option1"]
        op2 = request.form["option2"]
        op3 = request.form["option3"]
        op4 = request.form["option4"]
        answer = request.form["correct_answer"]
        category = request.form["category"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO questions 
            (question, option1, option2, option3, option4, correct_answer, category)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (question, op1, op2, op3, op4, answer, category))

        conn.commit()
        conn.close()

        return redirect("/admin")   # go back to dashboard

    return render_template("add_question.html")

@admin.route("/update-question", methods=["GET", "POST"])
def update_question():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    selected_category = request.args.get("category")

    # ✅ UPDATE LOGIC
    if request.method == "POST":
        qid = request.form["id"]
        question = request.form["question"]
        op1 = request.form["option1"]
        op2 = request.form["option2"]
        op3 = request.form["option3"]
        op4 = request.form["option4"]
        answer = request.form["correct_answer"]
        category = request.form["category"]

        cursor.execute("""
            UPDATE questions 
            SET question=%s, option1=%s, option2=%s, option3=%s, option4=%s,
                correct_answer=%s, category=%s
            WHERE id=%s
        """, (question, op1, op2, op3, op4, answer, category, qid))

        conn.commit()

    # ✅ FILTER LOGIC (IMPORTANT)
    if selected_category:
        cursor.execute(
            "SELECT * FROM questions WHERE category=%s",
            (selected_category,)
        )
    else:
        cursor.execute("SELECT * FROM questions")

    questions = cursor.fetchall()
    conn.close()

    return render_template("update_question.html", questions=questions)

# ✅ SHOW DELETE PAGE
@admin.route("/delete-question")
def delete_question():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()

    conn.close()

    return render_template("delete_question.html", questions=questions)


# ✅ DELETE ACTION
@admin.route("/delete/<int:id>")
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM questions WHERE id=%s", (id,))

    conn.commit()
    conn.close()

    return redirect("/delete-question")