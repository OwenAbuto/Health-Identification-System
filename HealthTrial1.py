# OLYMPUS Health Identification System

# Create new record in database thats called health records.
health_records = {}

def add_health_record():
    """Add a health record to the system."""
    name = input("Enter the patient's name: ")
    age = int(input("Enter the patient's age: "))
    gender = input("Enter the patient's gender: ")
    condition = input("Enter the patient's health condition: ")
    BloodType = input("Enter the patient's Blood Group: ")
    Insurance = input("Enter the patient's Insurance provider: ")
    
    # Create a dictionary to store the health record.
    record = {
        'Name': name,
        'Age': age,
        'Gender': gender,
        'Condition': condition,
        'Blood Group': BloodType,
        'Insurance': Insurance,
    }
    
    # Give every record that's input in the database a unique ID.
    record_id = len(health_records) + 1
    
    # Add the record to the dictionary using the unique ID.
    health_records[record_id] = record
    print(f"Health record added with ID: {record_id}")

def retrieve_health_record(record_id):
    """Retrieve and display a health record by its ID."""
    record = health_records.get(record_id)
    if record:
        print(f"Health Record ID: {record_id}")
        for key, value in record.items():
            print(f"{key}: {value}")
    else:
        print("Health record not found.")

def main():
    while True:
        print("\nHealth Identification System")
        print("1. Add Health Record")
        print("2. Retrieve Health Record")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            add_health_record()
        elif choice == '2':
            record_id = int(input("Enter the Health Record ID: "))
            retrieve_health_record(record_id)
        elif choice == '3':
            print("Olympus, Your preferred choice!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == '__main__':
    main()

############################ New Code being tested from here and below
