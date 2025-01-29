# Student Grading System
# - Write a program to calculate and display student grades.
# - Input: Student's name and marks for 5 subjects.
# - Output: Total marks, percentage, grade (A/B/C/Fail based on percentage).
stu_name=input("enter the name of the student:")
sub1=int(input("enter the marks of first subject:"))
sub2=int(input("enter the marks of second subject:"))
sub3=int(input("enter the marks of third subject:"))
sub4=int(input("enter the marks of fourth subject:"))
sub5=int(input("enter the marks of fifth subject:"))
max_marks=500
total_marks=sub1+sub2+sub3+sub4+sub5
percentage=total_marks/max_marks*100
print(f"total marks obtained by {stu_name}: {total_marks}")
print(f"percentage obtained by {stu_name}: {percentage}")
if(total_marks>=480):
    print("Grade:A")
elif(total_marks<480 and total_marks>=460):
    print("Grade:B")
elif(total_marks<460 and total_marks>=440):
    print("Grade:C")
elif(total_marks<440 and total_marks>=350):
    print("Average")
else:
    print("fail")
