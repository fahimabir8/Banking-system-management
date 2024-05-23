import random

class User:
    def __init__(self,name,email,address,account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.initial_balance = 0
        self.account_number = random.randint(1000,5000)
        self.transaction_history = []
        self.loan_count = 0
        
    def deposit(self,amount,bank):
        self.initial_balance += amount
        bank.total_balance += amount
        self.transaction_history.append(f"Deposited Amount: {amount}Tk")
        print(f"\n{amount}Tk deposited successfully!!\n")
        
    def withdraw(self,amount,bank):
        if bank.is_bankrupt == True:
            print("\nBank is bankrupt")
            return
            
        elif amount > self.initial_balance:
            print("\nWithdrawal amount exceeded")
            
        else:
            self.initial_balance -= amount
            print(f"**{amount}Tk withdrawal successfull**")
            self.transaction_history.append(f"Withdrawal Amount: {amount}Tk")
        
    def check_balance(self):
        print(f'\nCurrent Balance: {self.initial_balance}') 
    
    def check_transaction(self):
        print(f'\n{self.transaction_history}\n')
    
    def take_loan(self, amount, bank):
        if bank.loan_status == False:
            print("\nCurrently, cannot take any loans!!!")
            return
        
        if self.loan_count < 2:
            self.initial_balance += amount    
            self.loan_count += 1
            bank.total_loan += amount
            self.transaction_history.append(f"Loan amount: {amount}Tk")
            print(f'\n\t{amount}TK loan granted')
        else:
            print("Cannot Take More Loan")
            
    def transfer(self, amount, different_account,bank):
        if amount > self.initial_balance:
            print("\nTransfer amount exceeded")
        elif different_account.account_number not in bank.accounts:
            print("\nAccount doesn't exist")
        else:
            self.initial_balance -= amount
            different_account.initial_balance += amount
            self.transaction_history.append(f"Transferred: {amount}Tk to {different_account.name}")
            different_account.transaction_history.append(f"Received: {amount}Tk from {self.name}")
            print(f'\n{amount} Tk transferred to {different_account.name}')
        
class Bank:
    
    def __init__(self) -> None:
        self.accounts = {}
        self.total_balance = 0
        self.total_loan = 0
        self.loan_status = True
        self.is_bankrupt = False
         
    def create_account(self,account):
        self.accounts[account.account_number] = account
        
    def delete_account(self,email):
        for account_number, user in self.accounts.items():
            if user.email == email:
                del self.accounts[account_number]
                print("\n\t//Account deleted successfully//")
                break
            
            else:
                print("^^Account doesn't exists^^")
        
    def show_users(self):
        for account_number, user in self.accounts.items():
            print(f'\nAccount Number: {account_number}, User: {user.name}')
             
    def totalbalance(self):
        total = sum(user.initial_balance for account_number, user in self.accounts.items())
        print(f"\nTotal balance of bank is {total}")
        
    def totalLoan(self):
         print(f'\nTotal loan amount is : {self.total_loan}') 
       
    def bankruptcy(self):
        self.is_bankrupt = True
        print("\n\t^^Bank is now bankrupt^^")
        
    def non_bankruptcy(self):
        self.is_bankrupt = False
        print("\n\t^^Bank is bankruptcy proof^^")
    
    def OffLoan(self):
        self.loan_status = False
        print("\nLoan status is turned off now.")
    
    def OnLoan(self):
        self.loan_status = True
        print("\nLoan status is turned on now.")

admin = Bank()

def Admin():
    print("\n\t --- Welcome---")
    name = input("Enter name: ")
    password = int(input("Enter password: "))
    
    if name == 'admin' and password == 123:
        while True:
            
            print("\n--- Admin Menu ---")
            print("1. Create Account")
            print("2. Delete Account")
            print("3. Show user list")
            print("4. Show total balance of bank")
            print("5. Show total loan amount of bank")
            print("6. Turn Off Loan feature")
            print("7. Turn On Loan feature")
            print("8. Turn Bankruptcy On")
            print("9. Turn Bankruptcy Off")            
            print("10. Exit")
            ch = int(input("Enter your choice: "))

            if ch == 1:
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                address = input("Enter address: ")
                account = input("Enter your account_type: ")
                customer = User(name=name, email=email, address=address, account_type=account)
                admin.create_account(customer)
                print(f"Thanks for creating account {customer.name}. Your account no. {customer.account_number}")
            elif ch == 2:
                email = input("Enter the email account: ")
                admin.delete_account(email)
            elif ch == 3:
                admin.show_users()
            elif ch == 4:
                admin.totalbalance()
            elif ch == 5:
                admin.totalLoan()
            elif ch == 6:
                admin.OffLoan()
            elif ch == 7:
                admin.OnLoan()
            elif ch == 8:
                admin.bankruptcy()
            elif ch == 9:
                admin.non_bankruptcy()                
            elif ch == 10:
                break
            else:
                print("Invalid choice, please try again.")
                
    else:
        print("\n\t^^^Wrong Credentials^^^")

        
def user():
    current_user = None
    while True:
        if current_user == None:
            
            print("\n\t---Welcome!!!---")
            print("1. Create Account")
            print("2. Log in")
            print("3. Exit")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                address = input("Enter address: ")
                account = input("Enter your account_type: ")
                customer = User(name=name, email=email, address=address, account_type=account)
                admin.create_account(customer)
                print(f"\n Thanks for being with us {customer.name}. Your account number is {customer.account_number}")
            
            elif choice == 2:
                account_number = int(input("Enter your account number: "))
                if account_number in admin.accounts:
                    current_user = admin.accounts[account_number]
                    print(f"Welcome back, {current_user.name}")
   
                else:
                    print("Account Not Found...")
            
            elif choice == 3:
                break
            
            else:
                print("\nInvalid Choice. Please try again!!!")
                
        else:
            
            print("\n\t---User Menu---")
            print(f'Welcome to your account' )
            print("1. Deposit money") 
            print("2. Withdraw money") 
            print("3. Check Balance") 
            print("4. Check Transaction History") 
            print("5. Loan")
            print("6. Transfer Money")
            print("7. Log out")
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                amount = int(input("Enter the deposit amount: "))
                current_user.deposit(amount,admin)
                
            elif choice == 2:
                amount = int(input("Enter the withdrawal amount: "))
                current_user.withdraw(amount,admin)
                
            elif choice == 3:
                current_user.check_balance()
                
            elif choice == 4:
                current_user.check_transaction()
                
            elif choice == 5:
                amount = int(input("Enter the Loan amount: "))
                current_user.take_loan(amount,admin)
                
            elif choice == 6:
                amount = int(input("Enter amount: "))
                account_number = int(input("Enter recipient's account number: "))
                
                if account_number in admin.accounts:
                    recipient = admin.accounts[account_number]
                    current_user.transfer(amount, recipient, admin)
                    
                else:
                    print("Account not found!!")
                    
                
            elif choice == 7:
                print(f"\n\t^^See you again! {current_user.name}^^")
                current_user = None
                break
            
            else:
                print("Invalid choice!! Try again...")
        
        
while True:        
    print("\n\nAre you an Admin or User?")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    
    ch = int(input("Enter Option: "))
    
    if ch == 1:
        Admin()
        
    elif ch == 2:
        user()
        
    elif ch == 3:
        break
    
        
        
        
        
        
        
