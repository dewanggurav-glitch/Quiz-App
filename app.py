from flask import Flask
from config import Config

from routes.auth_routes import auth
from routes.quiz_routes import quiz
from routes.admin_routes import admin

app = Flask(__name__)
app.config.from_object(Config)

# 🔥 Needed for session
app.secret_key = Config.SECRET_KEY

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(quiz)
app.register_blueprint(admin)

if __name__ == "__main__":
    app.run(debug=True)