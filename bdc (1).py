import csv

# Adds a donor with name, age, blood group, and initial blood amount to the CSV file.
def add_donor(name, age, group, amount):
    with open('bdc.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, group, amount])
    print('Donor Added!')

# Adds a specified amount of blood to an existing donor's record.
def add_blood(name, amount):
    with open('bdc.csv', 'r') as file:
        data = csv.reader(file)
        rows = list(data)  # Read all rows into a list for modification.
    with open('bdc.csv', 'w', newline='\n') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == name:  # Check if the donor name matches.
                row[1] = str(int(row[1]) + amount)  # Update the blood amount.
            writer.writerow(row)
    print('Blood Added!')

# Removes a donor's record from the CSV file based on their name.
def remove_donor(name):
    with open('bdc.csv', 'r') as file:
        data = csv.reader(file)
        rows = list(data)  # Read all rows for processing.
    with open('bdc.csv', 'w', newline='\n') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != name:  # Write back all records except the one to delete.
                writer.writerow(row)
    print('Donor Removed!')

# Displays all donors along with their blood amount and group.
def view_donors():
    with open('bdc.csv', 'r') as file:
        data = csv.reader(file)
        for row in data:
            print(row[0], " : ", row[1], ",", row[3], " : ", row[2])

# Searches for donors with a specific blood group and displays their details.
def search_donor(group):
    with open('bdc.csv', 'r') as file:
        data = csv.reader(file)
        found = False
        for row in data:
            if row[2] == group:  # Check if the blood group matches.
                print(row[0], " : ", row[1], ",", row[3], " : ", row[2])
                found = True
        if not found:
            print('No donors found with this blood group.')

# Deducts a specified amount of blood from the available stock for a particular group.
def use_blood(group, amount):
    with open('bdc.csv', 'r') as file:
        data = csv.reader(file)
        rows = list(data)  # Read all rows for processing.
    with open('bdc.csv', 'w', newline='\n') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[2] == group:  # Check if the blood group matches.
                if int(row[1]) >= amount:  # Verify if sufficient blood is available.
                    row[1] = str(int(row[1]) - amount)  # Deduct the blood amount.
                    writer.writerow(row)
                else:
                    print('Not enough blood available!')
            else:
                writer.writerow(row)
    print('Blood used!')

# Main program loop to handle menu-based user interactions.
while True:
    print("\n--- Blood Donation Camp Management ---")
    print("1. Add Donor")
    print("2. Remove Donor")
    print("3. View Donors")
    print("4. Search Donor by Blood Group")
    print("5. Use Blood")
    print("6. Add Blood")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        # Input for adding a new donor.
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        if age < 18:  # Validate donor age.
            print('Age must be greater than 18!')
            continue
        # Select blood group.
        group = int(input("Enter blood group\n1. A+\n2. A-\n3. B+\n4. B-,\n5. AB+\n6. AB-\n7. O+\n8. O-\n>>> "))
        blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        if 1 <= group <= 8:
            group = blood_groups[group - 1]
        else:
            print('Invalid choice!')
            continue
        amount = int(input("Enter amount: "))
        add_donor(name, age, group, amount)
    elif choice == "2":
        name = input("Enter name to remove: ")
        remove_donor(name)
    elif choice == "3":
        view_donors()
    elif choice == "4":
        group = int(input("Enter blood group\n1. A+\n2. A-\n3. B+\n4. B-,\n5. AB+\n6. AB-\n7. O+\n8. O-\n>>> "))
        if 1 <= group <= 8:
            group = blood_groups[group - 1]
        else:
            print('Invalid choice!')
            continue
        search_donor(group)
    elif choice == "5":
        group = int(input("Enter blood group\n1. A+\n2. A-\n3. B+\n4. B-,\n5. AB+\n6. AB-\n7. O+\n8. O-\n>>> "))
        if 1 <= group <= 8:
            group = blood_groups[group - 1]
        else:
            print('Invalid choice!')
            continue
        amount = int(input("Enter amount to use: "))
        use_blood(group, amount)
    elif choice == "6":
        name = input("Enter name to add blood: ")
        amount = int(input("Enter amount to add: "))
        add_blood(name, amount)
    elif choice == "7":
        print("Exiting. Thank you!")
        break
    else:
        print("Invalid choice. Try again.")