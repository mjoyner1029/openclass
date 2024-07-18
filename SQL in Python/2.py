import sqlite3

def get_members_in_age_range(start_age, end_age):
    """
    Retrieve the details of members whose ages fall between start_age and end_age.
    """
    try:
        conn = sqlite3.connect('gym_database.db')
        cursor = conn.cursor()
        query = '''
        SELECT id, name, age
        FROM Members
        WHERE age BETWEEN ? AND ?
        '''
        cursor.execute(query, (start_age, end_age))
        members = cursor.fetchall()
        if not members:
            print(f"No members found in the age range {start_age} to {end_age}.")
        else:
            print(f"Members between ages {start_age} and {end_age}:")
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
        return members
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def count_members_by_age_group():
    """
    Count the number of members in different age groups.
    """
    age_groups = {
        '20-24': 0,
        '25-29': 0,
        '30-34': 0,
        '35-39': 0,
        '40+
