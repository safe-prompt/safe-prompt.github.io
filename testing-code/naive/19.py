import random

def test_encryption():
    random.seed(0)
    key = random.randint(1, 100)
    print(f"Encryption key: {key}")

# Example usage
test_encryption()
