import random
def guessing_numbers():
    randomnumber=random.randint(1, 100)
    attempts = 0
    while True:
        myguess=int(input("Enter your guess: "))
        attempts=attempts+1
        if myguess<randomnumber:
            print("Too Low")
        elif myguess>randomnumber:
            print("Too High")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
if __name__=="__main__":
    guessing_numbers()