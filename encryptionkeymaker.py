from cryptography.fernet import Fernet

def generate_key(key_path="key.key"):
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    print(f"Encryption saved in {key_path}")

# Generates the key (generate this once, and store your key safely)
generate_key()