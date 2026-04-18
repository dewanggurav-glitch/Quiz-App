# 🧠 Online Quiz System (Flask + MySQL)

## 📌 Project Description

This is a full-stack web-based quiz application developed using **Python Flask, MySQL, HTML, CSS, and JavaScript**.

The system allows users to register, log in, select quiz categories, and attempt quizzes with dynamically loaded questions. It also includes an admin panel for managing quiz content.

---

## 🚀 Features

### 👤 User Features

* User Signup & Login Authentication
* Category-based Quiz Selection
* Select Number of Questions (5, 10, 20, 30)
* Random Question Generation
* Answer Validation (Correct/Wrong Highlight)
* Quiz Result with Score & Percentage
* Logout Functionality

---

### 🛠️ Admin Features

* Admin Login
* Add New Questions
* Update Existing Questions
* Delete Questions
* Filter Questions by Category
* Manage Quiz Settings (Time Limit, Question Count)

---

### ⚙️ Technical Features

* Flask Blueprint Architecture
* MySQL Database Integration
* Session Management
* REST API for Questions
* Clean UI using Bootstrap

---

## 🧩 Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript, Bootstrap
* **Database:** MySQL
* **Tools:** VS Code, Git

---

## 📂 Project Structure

```
QUIZ/
│── routes/
│   ├── auth_routes.py
│   ├── quiz_routes.py
│   ├── admin_routes.py
│
│── templates/
│   ├── login.html
│   ├── category.html
│   ├── quiz-page.html
│   ├── result.html
│   ├── admin-dashboard.html
│
│── static/
│   ├── css/
│   ├── images/
│
│── models/
│   └── db.py
│
│── db_scripts/
│   ├── setup_db.py
│   ├── queries.py
│
│── app.py
│── config.py
│── requirements.txt
```

---

## 🛠️ Setup Instructions

1. Clone the repository:

```
git clone <your-repo-link>
cd quiz-app
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Setup database:

```
python -m db_scripts.setup_db
```

5. Run the application:

```
python app.py
```

6. Open browser:

```
http://127.0.0.1:5000
```

---

## 🎯 Future Improvements

* Timer-based quiz system
* Leaderboard
* Save user scores
* Responsive UI improvements

---

## 👨‍💻 Author

**Dewang Gurav**

---

## ⭐ Conclusion

This project demonstrates full-stack development skills including backend logic, database integration, and frontend UI design using Flask and MySQL.
