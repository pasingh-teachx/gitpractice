import json

# Read the JSON file
with open('customers.json', 'r') as file:
    people = json.load(file)

# Print first name, age, and phone number for each person
for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}, Age: {person['age']}, Phone: {person['phone_number']}")
