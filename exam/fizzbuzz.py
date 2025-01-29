# # - Write a program that prints numbers from 1 to 100, but:
# # - Prints &quot;Fizz&quot; for multiples of 3.
# # - Prints &quot;Buzz&quot; for multiples of 5.
# # - Prints &quot;FizzBuzz&quot; for multiples of both 3 and 5.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(F"{i} FizzBuzz")
    elif i % 3 == 0:
        print(F"{i} Fizz")
    elif i % 5 == 0:
        print(f"{i} Buzz")
    else:
        print(i)
