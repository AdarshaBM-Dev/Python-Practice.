''''Studet Management System
run data Analyisi on student marks
find highest score in a subjectt
hihest marks

input;- list of student marks with names
outputs;- Print higest mrks in each subject by whom

sample input;- Math -20 science-45 scial-98
name;- Tanmay, Dheeraj, sooraj
output;- Highest marks in mahs is by sooraj '''

Student_1 = {
    "Maths" : 45,
    "Social" : 75,
    "Social" : 96,
    "name" : "Tanmay"
}

Student_2 = {
    "Maths" : 74,
    "Social" : 83,
    "Social" : 100,
    "name" : "Dheeraj"
}

Student_3 = {
    "Maths" : 98,
    "Social" : 62,
    "Social" : 23,
    "name" : "Sooraj"
}

student_list = [Student_1, Student_2, Student_3]

highest_score_in_Maths = 0
highest_score_in_Maths_Name = ''
for student in student_list:
    if(student.get("Maths") > highest_score_in_Maths):
        highest_score_in_Maths = student.get("Maths")
        highest_score_in_Maths_Name = student.get("name")

print(f"The highest score in Maths is {highest_score_in_Maths} by {highest_score_in_Maths_Name}")