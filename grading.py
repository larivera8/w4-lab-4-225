# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))                  #added int and Perenthesis

exam_3 = int(input("Input exam grade three: "))            # changed str to int

grades = [exam_one, exam_two, exam_three]                   #added missing commas
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)                                         #added an a

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg <89:         # added semicolon
    letter_grade = "B"

''' 
70-79 :C, 60-69: D, 0-59:F
elif avg >= 70 and avg < 80:

elif avg >= 60 and avg < 70:

elif avg >= 0 and avg < 60:

'''    
    
    
elif avg > 70 and avg < 79:            # changed grades
    letter_grade = "C"                   # changed it to quotation marks
elif avg <= 60 and avg >= 69:         #changed grades
    letter_grade = "D"
elif avg <=50 and avg >=00:          # removed semicolon and added an expression
    letter_grade = "F"

    
for grade in grades:
    print("Exam: " + str(grade))

'''
Average and Grade should be printed once, no indentation

print("Average: " + str(avg))
print("Grade: " + letter_grade)
'''
    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

'''
use "==" operator instead "is" operator
if letter_grade == "F":
'''
if letter-grade is "F":
    print("Student is failing.")         #added parenthesis
else:
    print("Student is passing.")           #added  parenthesis
