import json

# Function to print student list
def print_students(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , "
              f"Email = {student['Email']}")

# Load JSON file
with open('student.json', 'r') as file:
    students = json.load(file)

print("\n--- Original Student List ---")
print_students(students)

# Add your information
new_student = {
    "F_Name": "Ashley",
    "L_Name": "Rowland",
    "Student_ID": 21435254,
    "Email": "arowland@my365.bellevue.edu"
}

students.append(new_student)

print("\n--- Updated Student List ---")
print_students(students)

# Write updated list back to file
with open('student.json', 'w') as file:
    json.dump(students, file, indent=4)

print("\nThe student.json file has been updated.")
