import sqlite3
#task 1
def add_member(id, name, age):
    try:
        conn = sqlite3.connect('gym_database.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO Members (id, name, age)
        VALUES (?, ?, ?)
        ''', (id, name, age))
        conn.commit()
        print(f"Member {name} added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Member ID {id} already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

#task 2
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        conn = sqlite3.connect('gym_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM Members WHERE id = ?', (member_id,))
        if cursor.fetchone() is None:
            print(f"Error: Member ID {member_id} does not exist.")
            return
        cursor.execute('''
        INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
        VALUES (?, ?, ?, ?)
        ''', (member_id, date, duration_minutes, calories_burned))
        conn.commit()
        print(f"Workout session for member ID {member_id} added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

#task3
def update_member_age(member_id, new_age):
    try:
        conn = sqlite3.connect('gym_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM Members WHERE id = ?', (member_id,))
        if cursor.fetchone() is None:
            print(f"Error: Member ID {member_id} does not exist.")
            return
        cursor.execute('''
        UPDATE Members
        SET age = ?
        WHERE id = ?
        ''', (new_age, member_id))
        conn.commit()
        print(f"Member ID {member_id} age updated to {new_age}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

#task 4
def delete_workout_session(session_id):
    try:
        conn = sqlite3.connect('gym_database.db')
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM WorkoutSessions
        WHERE session_id = ?
        ''', (session_id,))
        if cursor.rowcount == 0:
            print(f"Error: Session ID {session_id} does not exist.")
        else:
            conn.commit()
            print(f"Workout session ID {session_id} deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
