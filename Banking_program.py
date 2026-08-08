def show_balance(balance):
    print("*******************************")
    print(f"Your balance is $:{balance:.2f}")
    print("*******************************")
def deposite():
    amount = float(input("Enter amount to deposit: $"))
    if amount< 0:
        print("Invalid amount")
        return 0
    else:
     return amount
def withdraw(balance):
    amount = float(input("Enter the amount to be withdraw:$"))
    if amount > balance:
       print("Insufficient balance")
       return 0
    elif amount < 0:
       print("Amount must be grater then zero")
       return 0
    else:
       return amount
def main():
    balance =0
    is_running = True
    while is_running:
       print("***************")
       print("Banking Program")
       print("***************")
       print("1. Show Balance")
       print("2. Deposit")
       print("3. Withdraw")
       print("4. Exit")
       print("***************")
       choice = input("Enter your choice (1-4): ")
       if choice == '1':
          show_balance(balance)
       elif choice == '2':
          balance += deposite()
       elif choice == '3':
          balance -= withdraw(balance)
       elif choice == '4':
          is_running = False
       else:
          print("********************************")
          print("Invalid choice. Please try again.")
    print("********************************")  
    print("Thank you for using the banking program.") 
    print("********************************")
if __name__ == "__main__":
    main()  
                     
                      
        