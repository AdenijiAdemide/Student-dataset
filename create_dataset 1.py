import csv

# Fictional student dataset
students = [
    ["STU001", "Computer Science", 100, 92, 85],
    ["STU002", "Cyber Security", 200, 88, 79],
    ["STU003", "Information Technology", 100, 95, 91],
    ["STU004", "Computer Science", 300, 76, 68],
    ["STU005", "Software Engineering", 200, 90, 88],
    ["STU006", "Cyber Security", 300, 82, 74],
    ["STU007", "Information Technology", 400, 97, 93],
    ["STU008", "Software Engineering", 100, 85, 81],
    ["STU009", "Computer Science", 400, 93, 89],
    ["STU010", "Cyber Security", 200, 79, 72]
]

headers = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score"
]

# Save the dataset as a CSV file
with open("student_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(students)

print("Student dataset created successfully.")
