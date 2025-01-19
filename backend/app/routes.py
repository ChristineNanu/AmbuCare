from flask import Blueprint
from app import db
from app.models import User, Profile

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Welcome to AmbuCare!"

# Add some routes for testing
@main.route('/test-users')
def test_users():
    users = User.query.all()
    return "<br>".join([f"User: {user.username}, Email: {user.email}" for user in users])
