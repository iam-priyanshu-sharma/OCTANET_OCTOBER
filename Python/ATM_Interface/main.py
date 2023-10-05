from art import logo


class Account:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ₹{amount}")
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ₹{amount}")
            return True
        else:
            return False

    def transfer(self, to_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Transferred ₹{amount} to {to_account.user_id}")
            to_account.balance += amount
            to_account.transaction_history.append(f"Received ₹{amount} from {self.user_id}")
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history


class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.user_id] = account

    def authenticate(self, user_id, pin):
        if user_id in self.accounts and self.accounts[user_id].pin == pin:
            return self.accounts[user_id]
        else:
            return None


def main():
    atm = ATM()
    account1 = Account("12345", "1234")
    account2 = Account("54321", "4321")
    atm.add_account(account1)
    atm.add_account(account2)

    print(logo)
    user_id = input("Enter your user ID: ")
    pin = input("Enter your PIN: ")

    user_account = atm.authenticate(user_id, pin)

    if user_account:
        while True:
            print("\nOptions:")
            print("1. Transaction history")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Balance")
            print("6. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                history = user_account.get_transaction_history()
                for transaction in history:
                    print(transaction)
            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                if user_account.withdraw(amount):
                    print(f"Withdrew ₹{amount}")
                else:
                    print("Withdrawal failed. Insufficient balance or invalid amount.")
            elif choice == "3":
                amount = float(input("Enter the amount to deposit: "))
                if user_account.deposit(amount):
                    print(f"Deposited ₹{amount}")
                else:
                    print("Deposit failed. Invalid amount.")
            elif choice == "4":
                to_user_id = input("Enter the user ID to transfer to: ")
                amount = float(input("Enter the amount to transfer: "))
                to_account = atm.accounts.get(to_user_id)
                if to_account and user_account.transfer(to_account, amount):
                    print(f"Transferred ₹{amount} to {to_user_id}")
                else:
                    print("Transfer failed. Invalid user ID or insufficient balance.")
            elif choice == "5":
                print(f"Balance: ₹{user_account.get_balance()}")
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Authentication failed. Invalid user ID or PIN.")


if __name__ == "__main__":
    main()
