# Bill Splitter
# - Create a program to split a bill among a group of people:
# - Input: Total bill amount, number of people, and any tip percentage.
# - Output: Amount each person has to pay.
t=int(input("enter the total bill amount: "))
p=int(input("enter the number of people: "))
tip=int(input("enter the tip amount: "))
total_bill=t+tip
settlement_amount=total_bill/p
print(f"each person has to pay {settlement_amount}")