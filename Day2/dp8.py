def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def prime_numbers_in_range(start, end):
    primes = []
    while start <= end:
        if is_prime(start):
            primes.append(start)
        start += 1
    return primes
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Prime numbers between {start} and {end} are: {prime_numbers_in_range(start, end)}")