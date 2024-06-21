# task 1
customer_name = input('what is your name? ')
issue_description = input('what issue are you dealing with? ')

def open_ticket(service_tickets, customer_name, issue_description):
    """
    Opens a new service ticket.
    """
    ticket_id = f"Ticket{len(service_tickets) + 1:03d}"
    service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
    print(f"Ticket {ticket_id} opened for {customer_name}.")

def update_ticket_status(service_tickets, ticket_id, new_status):
    """
    Updates the status of an existing ticket.
    """
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}.")
    else:
        print(f"Ticket {ticket_id} not found.")

def display_tickets(service_tickets, filter_status=None):
    """
    Displays all tickets or filters by status.
    """
    for ticket_id, ticket_info in service_tickets.items():
        if filter_status is None or ticket_info["Status"] == filter_status:
            print(f"{ticket_id}: {ticket_info}")

# Sample tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to add additional tickets interactively
def add_additional_tickets(service_tickets):
    while True:
        add_ticket = input("Would you like to add a new ticket? (yes/no): ").strip().lower()
        if add_ticket == "yes":
            customer_name = input("Enter customer name: ").strip()
            issue_description = input("Enter issue description: ").strip()
            open_ticket(service_tickets, customer_name, issue_description)
        elif add_ticket == "no":
            break
        else:
            print("Invalid input, please enter 'yes' or 'no'.")

# Initialize with sample tickets and allow for additional entries
add_additional_tickets(service_tickets)

# Example usage:
# Open a new ticket
open_ticket(service_tickets, "Charlie", "Unable to reset password")

# Update the status of an existing ticket
update_ticket_status(service_tickets, "Ticket001", "closed")

# Display all tickets
print("\nAll tickets:")
display_tickets(service_tickets)

# Display only open tickets
print("\nOpen tickets:")
display_tickets(service_tickets, filter_status="open")

