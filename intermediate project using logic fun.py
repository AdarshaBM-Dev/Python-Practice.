def calculate_highest_in_Maths(student_list):
    highest_score_in_Maths = 0
    highest_score_in_Maths_Name = ''
    for student in student_list:
        if (student.get("Maths") > highest_score_in_Maths):
            highest_score_in_Maths = student.get("Maths")
            highest_score_in_Maths_Name = student.get("name")

    print(f"The highest score in Maths is {highest_score_in_Maths} by {highest_score_in_Maths_Name}")


Student_1 = {
    "Maths": 45,
    "Social": 75,
    "Science": 96,
    "name": "Tanmay"
}

Student_2 = {
    "Maths": 74,
    "Social": 83,
    "Science": 100,
    "name": "Dheeraj"
}

Student_3 = {
    "Maths": 98,
    "Social": 62,
    "Science": 23,
    "name": "Sooraj"
}

student_list = [Student_1, Student_2, Student_3]

calculate_highest_in_Maths(student_list)
