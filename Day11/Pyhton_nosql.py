from pymongo import MongoClient
import urllib.parse

def connect_db():
    try:
        # Your credentials
        username = "varaprasad@587"
        password = "Vara@587"
        cluster = "clustervara"  # Make sure this matches your actual cluster name

        # Encode username and password
        encoded_username = urllib.parse.quote_plus(username)
        encoded_password = urllib.parse.quote_plus(password)

        # Correct connection string with encoded credentials
        uri = f"mongodb+srv://{encoded_username}:{encoded_password}@{cluster}.ujj2a.mongodb.net/?retryWrites=true&w=majority&appName=Clustervara"

        # Connect to MongoDB
        client = MongoClient(uri)
        db = client["Varaaa123"]  # Replace with your actual database name
        print("Connected to MongoDB Atlas successfully")
        return db
    except Exception as e:
        print("Error connecting to MongoDB:", e)
        return None

# Example usage
db = connect_db()
