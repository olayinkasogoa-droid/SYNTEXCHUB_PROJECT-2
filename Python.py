import json
import os
import base64
import hashlib
from cryptography.fernet import Fernet
from getpass import getpass

VAULT_FILE = "vault.json"

# ---------- KEY FROM MASTER PASSWORD ----------
def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# ---------- LOAD VAULT ----------
def load_vault(key):
    if not os.path.exists(VAULT_FILE):
        return {}

    with open(VAULT_FILE, "rb") as file:
        data = file.read()

    if not data:
        return {}

    try:
        f = Fernet(key)
        decrypted = f.decrypt(data)
        return json.loads(decrypted.decode())
    except:
        print(" Wrong master password or corrupted vault!")
        exit()

# ---------- SAVE VAULT ----------
def save_vault(data, key):
    f = Fernet(key)
    encrypted = f.encrypt(json.dumps(data).encode())

    with open(VAULT_FILE, "wb") as file:
        file.write(encrypted)

# ---------- MASTER PASSWORD ----------
master_password = getpass("Enter Master Password: ")
key = generate_key(master_password)

passwords = load_vault(key)

# ---------- MENU ----------
while True:
    print("\n=== SECURE PASSWORD MANAGER ===")
    print("1. Add Password")
    print("2. View Password")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        website = input("Website: ")
        username = input("Username: ")
        password = input("Password: ")

        passwords[website] = {
            "username": username,
            "password": password
        }

        save_vault(passwords, key)
        print(" Saved securely!")

    elif choice == "2":
        website = input("Enter website: ")

        if website in passwords:
            print("Username:", passwords[website]["username"])
            print("Password:", passwords[website]["password"])
        else:
            print("Not found")

    elif choice == "3":
        search = input("Search: ").lower()

        found = False
        for site in passwords:
            if search in site.lower():
                print("Found:", site)
                found = True

        if not found:
            print("No match found")

    elif choice == "4":
        website = input("Enter website to delete: ")

        if website in passwords:
            del passwords[website]
            save_vault(passwords, key)
            print("🗑 Deleted!")
        else:
            print("Not found")

    elif choice == "5":
        save_vault(passwords, key)
        print("Goodbye ")
        break

    else:
        print("Invalid option")
