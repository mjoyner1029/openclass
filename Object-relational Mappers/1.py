from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:your_password@localhost/fitness_center_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save resources
db = SQLAlchemy(app)

# Define the Member model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    workout_sessions = db.relationship('WorkoutSession', backref='member', lazy=True)

# Define the WorkoutSession model
class WorkoutSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)

# Create all tables
with app.app_context():
    db.create_all()

from flask import request, jsonify

# Add a new member
@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    new_member = Member(name=data['name'], email=data['email'])
    try:
        db.session.add(new_member)
        db.session.commit()
        return jsonify({'message': 'Member added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Retrieve a member by ID
@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = Member.query.get(id)
    if member:
        return jsonify({'id': member.id, 'name': member.name, 'email': member.email}), 200
    return jsonify({'message': 'Member not found'}), 404

# Update a member by ID
@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    member = Member.query.get(id)
    if member:
        data = request.get_json()
        member.name = data.get('name', member.name)
        member.email = data.get('email', member.email)
        try:
            db.session.commit()
            return jsonify({'message': 'Member updated successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    return jsonify({'message': 'Member not found'}), 404

# Delete a member by ID
@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get(id)
    if member:
        try:
            db.session.delete(member)
            db.session.commit()
            return jsonify({'message': 'Member deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    return jsonify({'message': 'Member not found'}), 404


from datetime import date, time

# Schedule a new workout session
@app.route('/workout_sessions', methods=['POST'])
def add_workout_session():
    data = request.get_json()
    new_session = WorkoutSession(date=data['date'], time=data['time'], member_id=data['member_id'])
    try:
        db.session.add(new_session)
        db.session.commit()
        return jsonify({'message': 'Workout session scheduled successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Retrieve all workout sessions for a specific member
@app.route('/members/<int:member_id>/workout_sessions', methods=['GET'])
def get_workout_sessions(member_id):
    sessions = WorkoutSession.query.filter_by(member_id=member_id).all()
    if sessions:
        results = [
            {'id': session.id, 'date': session.date.strftime('%Y-%m-%d'), 'time': session.time.strftime('%H:%M:%S')}
            for session in sessions
        ]
        return jsonify(results), 200
    return jsonify({'message': 'No workout sessions found for this member'}), 404

# Update a workout session
@app.route('/workout_sessions/<int:id>', methods=['PUT'])
def update_workout_session(id):
    session = WorkoutSession.query.get(id)
    if session:
        data = request.get_json()
        session.date = data.get('date', session.date)
        session.time = data.get('time', session.time)
        try:
            db.session.commit()
            return jsonify({'message': 'Workout session updated successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    return jsonify({'message': 'Workout session not found'}), 404

# Delete a workout session
@app.route('/workout_sessions/<int:id>', methods=['DELETE'])
def delete_workout_session(id):
    session = WorkoutSession.query.get(id)
    if session:
        try:
            db.session.delete(session)
            db.session.commit()
            return jsonify({'message': 'Workout session deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    return jsonify({'message': 'Workout session not found'}), 404
