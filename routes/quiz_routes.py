from flask import Blueprint, render_template, request, session, redirect
from models.db import get_db_connection
import random

quiz = Blueprint("quiz", __name__)

# 🏠 HOME
@quiz.route("/")
def home():
    return render_template("index.html")


# 📂 CATEGORY PAGE
@quiz.route("/category")
def category_page():
    if "user" not in session:
        return redirect("/login")

    return render_template("category.html")


# ❓ QUIZ PAGE
@quiz.route("/quiz")
def quiz_page():
    if "user" not in session:
        return redirect("/login")

    category = request.args.get("category")
    count = int(request.args.get("count", 5))   # 🔥 get question count

    session["question_count"] = count           # 🔥 store count
    session.pop("questions", None)              # reset old quiz

    return render_template("quiz-page.html", category=category)


# 📡 FETCH QUESTIONS API
@quiz.route("/quiz/question")
def get_question():
    category = request.args.get("category")
    index = int(request.args.get("index", 0))

    # 🔥 FIRST TIME LOAD → FETCH + SHUFFLE
    if "questions" not in session:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM questions WHERE category=%s",
            (category,)
        )
        questions = cursor.fetchall()

        conn.close()

        random.shuffle(questions)   # 🔥 shuffle once
        session["questions"] = questions

    questions = session["questions"]

    # 🔥 LIMIT QUESTIONS (IMPORTANT)
    limit = session.get("question_count", len(questions))
    questions = questions[:limit]

    # 🔥 END CONDITION
    if index >= len(questions):
        total = len(questions)
        session.pop("questions", None)
        return {"status": "end", "total": total}

    return {"question": questions[index]}


# 🎯 RESULT PAGE
@quiz.route("/result")
def result():
    score = int(request.args.get("score", 0))
    total = int(request.args.get("total", 0))

    percentage = (score / total * 100) if total > 0 else 0

    return render_template(
        "result.html",
        score=score,
        total=total,
        percentage=round(percentage, 2)
    )