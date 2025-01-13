from app import db

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    profile = db.relationship('Profile', uselist=False, back_populates='user')
    bookings = db.relationship('Booking', back_populates='user')
    feedback = db.relationship('Feedback', back_populates='user')

    def __repr__(self):
        return f'<User {self.username}>'

# Profile Model
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    address = db.Column(db.String(200), nullable=True)

    user = db.relationship('User', back_populates='profile')

    def __repr__(self):
        return f'<Profile {self.user.username}>'

# Service Model
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)

    bookings = db.relationship('Booking', back_populates='service')
    feedback = db.relationship('Feedback', back_populates='service')

    def __repr__(self):
        return f'<Service {self.name}>'

# Booking Model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., pending, completed

    user = db.relationship('User', back_populates='bookings')
    service = db.relationship('Service', back_populates='bookings')
    payment = db.relationship('Payment', back_populates='booking', uselist=False)

    def __repr__(self):
        return f'<Booking {self.id} for {self.user.username}>'

# Payment Model
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., completed, failed

    booking = db.relationship('Booking', back_populates='payment')

    def __repr__(self):
        return f'<Payment {self.id} for Booking {self.booking.id}>'

# Feedback Model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    feedback_text = db.Column(db.String(255), nullable=True)
    rating = db.Column(db.Integer, nullable=False)  # Rating from 1 to 5

    user = db.relationship('User', back_populates='feedback')
    service = db.relationship('Service', back_populates='feedback')

    def __repr__(self):
        return f'<Feedback {self.id} for Service {self.service.name}>'
