# Bank Loan Eligibility
# - Develop a program to check loan eligibility:
# - Input: Salary, age, and credit score.
# - Output: Loan approval or rejection with reasons.
salary=int(input("enter the salary: "))
age=int(input("enter the age: "))
credit_score=int(input("enter the credit_score: "))
if salary>=25000 and age>=21 and credit_score>=750:
    print("congratulations your loan has been approved")
if salary<25000:
    print("your loan has been rejected because you dont have minimum reuired salary.")
if age<21:
    print("your loan application got rejected because you are under age.")
else:
    print("your loan application rejected because you dont have proper civil history.")