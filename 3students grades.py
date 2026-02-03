for student in students:
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print("Name:", student["name"], "- Average Grade:", average)