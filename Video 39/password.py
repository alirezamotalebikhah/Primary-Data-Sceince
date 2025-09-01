import csv
import os
import random
import string

CSV_FILE = "passwords.csv"

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

def load_passwords():
    """Load existing accounts from CSV"""
    accounts = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            accounts = list(reader)
    return accounts

def save_passwords(accounts):
    """Save all accounts to CSV"""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["name", "username", "pass"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(accounts)

def show_accounts(accounts):
    """Show all saved accounts"""
    if not accounts:
        print("No accounts saved yet.")
        return
    print("\nSaved Accounts:")
    print("-" * 40)
    for i, acc in enumerate(accounts):
        print(f"{i+1}. Name: {acc['name']} | Username: {acc['username']} | Pass: {acc['pass']}")
    print("-" * 40)

def add_account(accounts):
    """Add a new account with password generation"""
    name = input("Enter account name (e.g. Gmail): ")
    username = input("Enter username/email: ")

    # Generate password until user accepts
    while True:
        length = int(input("Enter password length: "))
        new_pass = generate_password(length)
        print(f"Generated password: {new_pass}")
        ok = input("Do you accept this password? (y/n): ").lower()
        if ok == "y":
            break

    accounts.append({"name": name, "username": username, "pass": new_pass})
    print("✅ Account added successfully!")

def edit_account(accounts):
    """Edit an existing account's password"""
    show_accounts(accounts)
    if not accounts:
        return
    try:
        choice = int(input("Enter account number to edit: ")) - 1
        if choice < 0 or choice >= len(accounts):
            print("❌ Invalid choice.")
            return
    except ValueError:
        print("❌ Invalid input.")
        return

    acc = accounts[choice]
    print(f"Editing account: {acc['name']} ({acc['username']})")

    # Generate new password
    while True:
        length = int(input("Enter new password length: "))
        new_pass = generate_password(length)
        print(f"Generated new password: {new_pass}")
        ok = input("Do you accept this new password? (y/n): ").lower()
        if ok == "y":
            acc["pass"] = new_pass
            print("✅ Password updated!")
            break

def main():
    accounts = load_passwords()
    while True:
        print("\n==== Password Manager ====")
        print("1. Show Accounts")
        print("2. Add New Account")
        print("3. Edit Password for Account")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_accounts(accounts)
        elif choice == "2":
            add_account(accounts)
            save_passwords(accounts)
        elif choice == "3":
            edit_account(accounts)
            save_passwords(accounts)
        elif choice == "4":
            save_passwords(accounts)
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
