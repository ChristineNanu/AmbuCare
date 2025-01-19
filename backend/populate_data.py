from app import create_app, db
from app.models import User, Profile
from faker import Faker
from werkzeug.security import generate_password_hash  # Add this for password hashing

app = create_app()
fake = Faker()

with app.app_context():
    for _ in range(10):  # Create 10 random users
        # Generate a hashed password
        password_hash = generate_password_hash(fake.password())
        
        # Create the user with the hashed password
        user = User(username=fake.user_name(), email=fake.email(), password=password_hash)
        db.session.add(user)

        # Commit the user to ensure the user.id is populated
        db.session.commit()

        # Create and associate the profile with the user
        profile = Profile(user_id=user.id, phone=fake.phone_number(), address=fake.address())
        db.session.add(profile)

    db.session.commit()

    print('10 random users added!')
