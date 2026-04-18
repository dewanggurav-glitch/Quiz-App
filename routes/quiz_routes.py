from flask import Blueprint, render_template, request, session, redirect
from models.db import get_db_connection
import random

quiz = Blueprint("quiz", __name__)

@quiz.route("/")
def home():
    return render_template("index.html")


@quiz.route("/category")
def category_page():
    if "user" not in session:
        return redirect("/login")

    return render_template("category.html")


@quiz.route("/quiz")
def quiz_page():
    if "user" not in session:
        return redirect("/login")

    category = request.args.get("category")
    count = int(request.args.get("count", 5))   

    session["question_count"] = count           
    session.pop("questions", None)             

    return render_template("quiz-page.html", category=category)


@quiz.route("/quiz/question")
def get_question():
    category = request.args.get("category")
    index = int(request.args.get("index", 0))

    if "questions" not in session:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM questions WHERE category=%s",
            (category,)
        )
        questions = cursor.fetchall()

        conn.close()

        random.shuffle(questions)   
        session["questions"] = questions

    questions = session["questions"]

    limit = session.get("question_count", len(questions))
    questions = questions[:limit]

    if index >= len(questions):
        total = len(questions)
        session.pop("questions", None)
        return {"status": "end", "total": total}

    return {"question": questions[index]}


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
