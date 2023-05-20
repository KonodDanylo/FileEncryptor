import sys
import os
import logging
from cryptography.fernet import Fernet
from getpass import getpass

logging.basicConfig(filename='app.log', level=logging.INFO)


def generate_key():
    key = Fernet.generate_key()
    return key


def encrypt_file(filename, key):
    cipher = Fernet(key)
    try:
        with open(filename, 'rb') as file:
            file_data = file.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(filename, 'wb') as file:
            file.write(encrypted_data)
        logging.info(f"File '{filename}' encrypted successfully.")
        print("File encrypted successfully!\n")
    except FileNotFoundError:
        logging.error(f"Error: File '{filename}' not found.")
        print("Error: File does not exist. Please check if you typed the name correctly.\n")


def decrypt_file(filename, key):
    cipher = Fernet(key)
    try:
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(filename, 'wb') as file:
            file.write(decrypted_data)
        logging.info(f"File '{filename}' decrypted successfully.")
        print("File decrypted successfully!\n")
    except FileNotFoundError:
        logging.error(f"Error: File '{filename}' not found.")
        print("Error: File does not exist. Please check if you typed the name correctly.\n")
    except ValueError:
        logging.error(
            f"Error: Invalid key or file '{filename}' has been modified.")
        print("Error: Invalid key or file has been modified. Please ensure the correct key is used.\n")


def set_password():
    while True:
        password = getpass("Set a password: ")
        confirm_password = getpass("Confirm password: ")

        if password == confirm_password:
            return password
        else:
            print("Passwords do not match. Please try too set the password again.\n")


def perform_encryption(password):
    filename = input("Enter the filename to encrypt: ")

    if not os.path.exists(filename):
        print("Error: File not found.\n")
        return

    key = generate_key()
    encrypt_file(filename, key)
    # Save the key and password for decryption
    with open(filename + '.key', 'wb') as key_file:
        key_file.write(key)
    with open(filename + '.pwd', 'w') as pwd_file:
        pwd_file.write(password)


def perform_decryption():
    filename = input("Enter the filename to decrypt: ")
    password = getpass("Enter the password: \n")
    key_filename = filename + '.key'
    pwd_filename = filename + '.pwd'

    if not os.path.exists(key_filename) or not os.path.exists(pwd_filename):
        print("Error: Key file or password file not found.\n")
        return

    with open(key_filename, 'rb') as key_file:
        key = key_file.read()

    with open(pwd_filename, 'r') as pwd_file:
        saved_password = pwd_file.read().strip()

    if password != saved_password:
        print("Incorrect password. Decryption aborted.\n")
        return

    decrypt_file(filename, key)
    # Delete the key and password files
    os.remove(key_filename)
    os.remove(pwd_filename)


while True:
    print("╔═══════════════════════════╗")
    print("║     File_Encryptor_App    ║")
    print("╠═══════════════════════════╣")
    print("║ Choose an option:          ║")
    print("║ 1) Encrypt data            ║")
    print("║ 2) Decrypt data            ║")
    print("║ 3) Exit                    ║")
    print("╚═══════════════════════════╝")

    choice = input("Enter your choice: ")

    if choice == "1":
        password = set_password()
        perform_encryption(password)

    elif choice == "2":
        perform_decryption()

    elif choice == "3":
        print("Exiting the program.\n")
        sys.exit(0)

    else:
        print("Error: Invalid choice. Please try again.\n")
