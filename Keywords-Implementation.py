# Banking System Simulation

# Importing necessary modules
import random  # Using 'import' to bring in the random module

class BankAccount:  # Using 'class' to define a blueprint for bank accounts
    def __init__(self, name):  # 'def' defines a function, '__init__' initializes the object
        self.name = name
        self.balance = 0  # Initial balance is set to 0
        self.transactions = []  # List to store transaction history
    
    def deposit(self, amount):
        """Deposit money into the account"""
        assert amount > 0, "Deposit amount must be positive"  # 'assert' ensures valid input
        self.balance += amount  # Adding amount to balance
        self.transactions.append(f"Deposited {amount}")
        return f"{self.name} deposited {amount}. New balance: {self.balance}"
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > self.balance:
            raise ValueError("Insufficient funds")  # 'raise' is used to trigger an error
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")
        return f"{self.name} withdrew {amount}. New balance: {self.balance}"
    
    def get_balance(self):
        """Return current balance"""
        return self.balance
    
    def transaction_history(self):
        """Return transaction history"""
        return self.transactions
    
    def __del__(self):  # Using 'del' to clean up object
        print(f"Account for {self.name} is being deleted.")

# Creating an account
def main():
    name = input("Enter your name: ")
    user = BankAccount(name)
    
    try:
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transaction History\n5. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                print(user.deposit(amount))
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                print(user.withdraw(amount))
            elif choice == "3":
                print("Balance:", user.get_balance())
            elif choice == "4":
                print("Transactions:", user.transaction_history())
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
    
    except ValueError as e:  # Handling errors using 'except'
        print("Error:", e)
    
    finally:  # 'finally' ensures the following block always executes
        print("Banking session ended.")

# Using 'if' statement
def check_status(balance):
    if balance > 0:
        return True
    elif balance == 0:
        return False
    else:
        pass  # 'pass' acts as a placeholder

# Demonstrate 'for', 'while', 'continue', and 'break'
def count_down(n):
    while n > 0:  # 'while' loop continues as long as condition is True
        if n == 2:
            n -= 1
            continue  # 'continue' skips the rest of the loop for this iteration
        print(n)
        n -= 1
    
    for i in range(3):  # 'for' loop iterating over a range
        if i == 2:
            break  # 'break' exits the loop early
        print(f"Counting: {i}")

global_var = "Global Variable"  # 'global' defines a global variable

def modify_global():
    global global_var  # Access and modify the global variable
    global_var = "Modified Global Variable"

modify_global()
print(global_var)  # Check global variable modification

# Using 'with' for file handling
with open("transactions.txt", "w") as file:  # 'with' ensures proper resource management
    file.write("Transaction Log\n")

def generator_example():
    yield "Hello"  # 'yield' allows generator function to return values lazily
    yield "World"

def nested_function_example():
    x = "Outer Variable"
    
    def inner():
        nonlocal x  # 'nonlocal' allows modifying the enclosing function's variable
        x = "Modified Inner Variable"
        print(x)
    
    inner()
    print(x)

nested_function_example()

def return_none_example():
    return None  # 'None' explicitly returned

def check_boolean():
    value = False  # 'False' keyword used
    if not value:  # 'not' negates the boolean
        print("Value is False")
    else:
        print("Value is True")

check_boolean()

gen = generator_example()
print(next(gen))
print(next(gen))

# Run main function
if __name__ == "__main__":
    main()
    count_down(5)
