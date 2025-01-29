# - Write a program to check if a given year is a leap year.
# - Allow the user to check multiple years.
while True:
    year = int(input("Enter a year: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != "y":
        break