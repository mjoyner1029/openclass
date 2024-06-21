# task 1
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}
class Hotel:
    def __init__(self, total_rooms):
        self.total_rooms = total_rooms
        self.booked_rooms = dict()

    def is_available(self, room_number):
        if room_number in self.booked_rooms.keys(): 
            return False
        else:
            return True

    def book_room(self, room_number, user_name):
        if self.is_available(room_number):
            self.booked_rooms[room_number] = user_name
        else:
            print("Sorry, the room is already booked.")

    def display_booked_rooms(self):
        for room_number, user_name in self.booked_rooms.items():
            print(f"Room Number: {room_number},  Booked By: {user_name}")

    def display_user_bookings(self, user_name):
        user_rooms = [room for room, user in self.booked_rooms.items() if user == user_name]
        print(f"User {user_name} booked rooms {user_rooms}")