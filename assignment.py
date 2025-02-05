# Function to handle each test case
def process_test_case():
    n, q = int(input()), int(input())  # Read number of friends and queries
    friends = {}  # Dictionary to store friends' details

    # Input friends' details
    for _ in range(n):
        data = input().split()
        name = data[0]
        age = data[1]
        hobbies = data[2]
        favorite_chocolate = data[3]
        friends[name] = (age, hobbies, favorite_chocolate)

    # Process each query
    for _ in range(q):
        query_name = input().strip()
        details = friends[query_name]
        print(details[0], details[1], details[2])

# Main program
t = int(input())  # Number of test cases
for _ in range(t):
    process_test_case()
