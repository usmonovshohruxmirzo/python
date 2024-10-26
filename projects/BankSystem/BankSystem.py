import os
import random
import shutil
import hashlib

class Account:
    def __init__(self, account_name, account_number, account_email, account_password):
        self.account_name = account_name
        self.account_number = account_number
        self.account_email = account_email
        self.account_password = self.hash_password(account_password)
        self.balance = 1000.000

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

class Bank:
    def __init__(self):
        self.accounts = []

        if not os.path.exists("accounts"):
            os.mkdir("accounts")

    def create_account(self, account_name, account_email, account_password):
        if os.path.exists(f"accounts/{account_name}.txt"):
            print(account_name, "already exists")
            return None

        account_number = random.randint(1000000000, 9999999999)

        while any(acc.account_number == account_number for acc in self.accounts):
            account_number = random.randint(1000000000, 9999999999)

        new_account = Account(account_name, account_number, account_email, account_password)
        self.accounts.append(new_account)

        with open(f"accounts/{account_name}.txt", "w") as create_file:
            create_file.write(f"- Account Holder: {account_name}\n")
            create_file.write(f"- Account Number: {account_number}\n")
            create_file.write(f"- Account Email: {account_email}\n")
            create_file.write(f"- Account Password: {account_password}\n")
            create_file.write(f"- Balance: ${new_account.balance}")

        print(account_name, "is successfully created!")

        return new_account

    @staticmethod
    def update_account(account_name, new_account_name, new_account_number, new_account_email, new_account_password):
        if os.path.exists(f"accounts/{account_name}.txt"):
            with open(f"accounts/{account_name}.txt", "r") as read_file:
                lines = read_file.readlines()

            with open(f"accounts/{account_name}.txt", "w") as update_file:
                for line in lines:
                    if new_account_name and line.startswith("- Account Holder:"):
                        update_file.write(f"- Account Holder: {new_account_name}\n")
                    elif new_account_number and line.startswith("- Account Number:"):
                        update_file.write(f"- Account Number: {new_account_number}\n")
                    elif new_account_email and line.startswith("- Account Email:"):
                        update_file.write(f"- Account Email: {new_account_email}\n")
                    elif new_account_password and line.startswith("- Account Password:"):
                        update_file.write(f"- Account Password: {new_account_password}\n")
                    else:
                        update_file.write(line)

            os.rename(f"accounts/{account_name}.txt", f"accounts/{new_account_name}.txt")
            print(f"accounts/{account_name}.txt updated successfully")

    @staticmethod
    def find_account(account_name):
        if os.path.exists(f"accounts/{account_name}.txt"):
            with open(f"accounts/{account_name}.txt", "r") as read_file:
                print(account_name, "is found")
                print("-----------------------------------")
                print(read_file.read())
                print("-----------------------------------")
        else:
            print(account_name, "not found")

    @staticmethod
    def get_account_balance(account_name):
        with open(f"accounts/{account_name}.txt", "r") as read_file:
            for line in read_file:
                if line.startswith("- Balance:"):
                    return float(line.split("$")[-1].strip())
        return 0.00

    @staticmethod
    def deposit(account_name, amount):
        with open(f"accounts/{account_name}.txt", "r") as read_file:
            data = read_file.readlines()

        balance = data[len(data) - 1][13:]
        balance = int(balance) + int(amount)

        data[len(data) - 1] = f"- Balance - ${balance}"

        with open(f"accounts/{account_name}.txt", "w") as update_file:
            update_file.writelines(data)

        print(f"+${amount} deposited successfully")

    @staticmethod
    def withdraw(account_name, amount):
        with open(f"accounts/{account_name}.txt", "r") as read_file:
            data = read_file.readlines()

        balance = data[len(data) - 1][13:]

        if int(amount) > int(balance):
            print("you have not enough money to withdraw")
            return None

        data[len(data) - 1] = f"- Balance - ${int(balance) - int(amount)}"

        with open(f"accounts/{account_name}.txt", "w") as update_file:
            update_file.writelines(data)

        print(f"-${amount} withdraw successfully")


    @staticmethod
    def delete_account(account_name):
        try:
            if os.path.exists(f"accounts/{account_name}.txt"):
                os.remove(f"accounts/{account_name}.txt")
                print(account_name, "is deleted successfully")
            else:
                print(account_name, "is not found")
        except FileNotFoundError:
            print(f"{account_name} not found")

    def display_all_accounts(self):
        accounts = self.accounts
        for account in accounts:
            print(account.account_number, account.account_name)

    @staticmethod
    def delete_all_accounts():
       try:
           if os.path.exists("accounts"):
               shutil.rmtree("accounts")
               print("all accounts removed from bank")
           else:
               print("The Folder does not exist")
       except FileNotFoundError:
           print("No accounts to delete")


def run_system():
    bank = Bank()

    print("-----------------------------------")
    print("- Create a new account: *create*")
    print("- Update an account: *update*")
    print("- Delete an account: *delete*")
    print("- Delete all account: *delete all*")
    print("- Find account: *find*")
    print("- Deposit to account: *deposit*")
    print("- Withdraw money: *withdraw*")
    print("- Show all accounts: *show all*")
    print("- Exit from Bank: *exit*")
    print("-----------------------------------")

    option = input("choose an option: ")

    try:
        if option == "create":
            account_name = input("enter account name: ")
            account_email = input("enter your email")
            account_password = input("enter your password")
            loading = 0

            for x in range(0, 100):
                loading += 1
                print(f"%{loading}")

            if loading == 100:
                bank.create_account(account_name, account_email, account_password)

        elif option == "delete all":
            confirm = input("are you sure? yes/no: ")
            if confirm == "yes":
                loading = 0
                for x in range(0, 100):
                    loading += 1
                    print(f"%{loading}")

                if loading == 100:
                    bank.delete_all_accounts()
            else:
                print("canceled successfully")

        elif option == "delete":
            account_name = input("enter your account name: ")
            bank.delete_account(account_name)

        elif option == "update":
            account_name = input("enter your account name: ")
            new_account_name = input("enter your new account name: ")
            new_account_number = input("enter your new account number: ")
            new_account_email = input("enter your new account email: ")
            new_account_password = input("enter your new account password: ")

            bank.update_account(account_name, new_account_name, new_account_number, new_account_email, new_account_password)

        elif option == "find":
            account_name = input("enter your account name: ")
            bank.find_account(account_name)

        elif option == "deposit":
            account_name = input("enter account name: ")

            if os.path.exists(f"accounts/{account_name}.txt"):
                amount = input("enter deposit amount: ")
                bank.deposit(account_name, amount)
            else:
                print("⚠️", account_name, "is not found")

        elif option == "withdraw":
            account_name = input("enter account name: ")

            if os.path.exists(f"accounts/{account_name}.txt"):
                amount = input("enter withdraw amount: ")
                bank.withdraw(account_name, amount)
            else:
                print("⚠️", account_name, "is not found")

        elif option == "get balance":
            account_name = input("enter you account name: ")

            if os.path.exists(f"accounts/{account_name}.txt"):
                bank.get_account_balance(account_name)
            else:
                print("⚠️", account_name, "is not found")

        elif option == "exit":
            print("exiting...")

        else: print("unknown option")
    except():
        print("error has occurred")
    finally: print("system is off")

run_system()