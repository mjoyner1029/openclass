def format_itineraries(itineraries):
    format_itineraries = []
    for traveler_name, origin, destination in itineraries:
        format_itineraries.append(f"{traveler_name} is traveling from {origin} to {destination}")
        return "\n".join(format_itineraries)

# Input the number of itineraries
num_itineraries = int(input("Enter the number of itineraries: "))

# Input details for each itinerary
itineraries = []
for _ in range(num_itineraries):
    traveler_name = input("Enter traveler name: ")
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    itineraries.append((traveler_name, origin, destination))
# Format and print the output
output = format_itineraries(itineraries)
print(output)