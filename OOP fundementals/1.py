# task 1
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated: Vehicle {self.registration_number} now owned by {self.owner}")

# Creating instances of Vehicle
vehicle1 = Vehicle("ABC123", "Sedan", "Alice")
vehicle2 = Vehicle("XYZ789", "SUV", "Bob")

# Printing initial details
print(f"Vehicle 1: Reg. No. {vehicle1.registration_number}, Type {vehicle1.type}, Owner {vehicle1.owner}")
print(f"Vehicle 2: Reg. No. {vehicle2.registration_number}, Type {vehicle2.type}, Owner {vehicle2.owner}")

# Updating owner of vehicle1
vehicle1.update_owner("Carol")

# Printing updated details
print(f"After owner update:")
print(f"Vehicle 1: Reg. No. {vehicle1.registration_number}, Type {vehicle1.type}, Owner {vehicle1.owner}")
print(f"Vehicle 2: Reg. No. {vehicle2.registration_number}, Type {vehicle2.type}, Owner {vehicle2.owner}")

# task 2

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count
    
    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added to event {self.name}. Current participant count: {self.participant_count}")
    
    def get_participant_count(self):
        return self.participant_count

# Creating an instance of Event
event1 = Event("Python Conference", "2024-07-01")

# Adding participants to event1
event1.add_participant()
event1.add_participant()
event1.add_participant()

# Getting participant count
print(f"Participant count for event {event1.name}: {event1.get_participant_count()}")
