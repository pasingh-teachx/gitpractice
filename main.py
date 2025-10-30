import json

# Read the JSON file
with open('customers.json', 'r') as file:
    people = json.load(file)

# Print first name, age, and phone number for each person
for person in people:
    print("--Person--")
    print(f"Name: {person['last_name']}, {person['first_name']}, Age: {person['age']}, Phone: {person['phone_number']}")
