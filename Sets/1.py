# Define the sets of flight destinations
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Find destinations that both airlines fly to
common_destinations = our_routes.intersection(competitor_routes)

# Find destinations unique to your airline
unique_destinations_ours = our_routes.difference(competitor_routes)

# Find destinations that neither airline shares
unique_destinations_competitor = competitor_routes.difference(our_routes)

# Display the results
print("Destinations both airlines fly to:", common_destinations)
print("Destinations unique to our airline:", unique_destinations_ours)
print("Destinations unique to competitor's airline:", unique_destinations_competitor)