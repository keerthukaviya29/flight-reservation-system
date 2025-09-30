# Flight Reservation System with Passenger Accounts

flights = {
    "AI101": {"destination": "Delhi", "seats": 5, "fare": 5000},
    "AI102": {"destination": "Mumbai", "seats": 3, "fare": 4500},
    "AI103": {"destination": "Chennai", "seats": 4, "fare": 4000},
}

bookings = []
passenger_accounts = {}  # stores username:password

# ---------------- Passenger Functions ----------------
def passenger_menu():
    while True:
        print("\nPassenger Options:")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            username = log_in()
            if username:
                passenger_logged_in_menu(username)
        elif choice == "3":
            break
        else:
            print("Invalid option!")

def sign_up():
    username = input("Enter new username: ")
    if username in passenger_accounts:
        print("Username already exists!")
        return
    password = input("Enter password: ")
    passenger_accounts[username] = password
    print("Account created successfully!")

def log_in():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in passenger_accounts and passenger_accounts[username] == password:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Invalid username or password!")
        return None

def passenger_logged_in_menu(username):
    while True:
        print(f"\nPassenger Menu ({username})")
        print("1. Check Availability & Fare")
        print("2. Book Ticket")
        print("3. Log Out")
        choice = input("Choose an option: ")

        if choice == "1":
            check_availability()
        elif choice == "2":
            book_ticket(username)
        elif choice == "3":
            print(f"{username} logged out.")
            break
        else:
            print("Invalid option!")

def check_availability():
    print("\nAvailable Flights:")
    for code, info in flights.items():
        print(f"{code}: {info['destination']} - Seats: {info['seats']} - Fare: {info['fare']}")
    flight_code = input("Enter flight code to check details: ").upper()
    if flight_code in flights:
        flight = flights[flight_code]
        print(f"Flight {flight_code} to {flight['destination']} has {flight['seats']} seats. Fare: {flight['fare']}")
        return flight_code
    else:
        print("Invalid flight code!")
        return None

def book_ticket(passenger_name):
    flight_code = check_availability()
    if flight_code and flights[flight_code]["seats"] > 0:
        flights[flight_code]["seats"] -= 1
        booking = {"passenger": passenger_name, "flight": flight_code, "status": "Pending"}
        bookings.append(booking)
        print(f"Ticket booked successfully! Waiting for cashier approval.")
    else:
        print("Booking failed. No seats available.")

# ---------------- Cashier Functions ----------------
def cashier_menu():
    while True:
        print("\nCashier Menu:")
        print("1. Approve Ticket")
        print("2. Issue Ticket")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            approve_ticket()
        elif choice == "2":
            issue_ticket()
        elif choice == "3":
            break
        else:
            print("Invalid option!")

def approve_ticket():
    pending = [b for b in bookings if b["status"] == "Pending"]
    if not pending:
        print("No pending bookings.")
        return
    print("\nPending Bookings:")
    for i, b in enumerate(pending):
        print(f"{i+1}. Passenger: {b['passenger']} Flight: {b['flight']}")
    choice = int(input("Enter booking number to approve: ")) - 1
    if 0 <= choice < len(pending):
        pending[choice]["status"] = "Approved"
        print("Booking approved!")
    else:
        print("Invalid choice.")

def issue_ticket():
    approved = [b for b in bookings if b["status"] == "Approved"]
    if not approved:
        print("No approved bookings to issue.")
        return
    print("\nApproved Bookings:")
    for b in approved:
        print(f"Passenger: {b['passenger']} Flight: {b['flight']} - Status: {b['status']}")
    print("Tickets issued successfully!")
    for b in approved:
        b["status"] = "Issued"

# ---------------- Main Program ----------------
def main():
    while True:
        print("\n--- Flight Reservation System ---")
        print("1. Passenger")
        print("2. Cashier")
        print("3. Exit")
        user_type = input("Select user type: ")

        if user_type == "1":
            passenger_menu()
        elif user_type == "2":
            cashier_menu()
        elif user_type == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
