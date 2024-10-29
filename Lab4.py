     
                # Task 1
      # Program 1 : Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


                   # Task 2

pin = 1234  
balance = 1000 

# Step 1:  PIN
user_pin = int(input("Enter your PIN: ")) 

# Step 2: PIN is correct
if user_pin == pin:
    print("\nPIN correct! Welcome to the ATM.")
    
    # Step 3: Display Menu
    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")
        
        # Step 4:  user choice
        choice = int(input("Choose an option (1-3): "))  
        
        if choice == 1:
            # Option 1: Check balance
            print(f"Your current balance is: ${balance}")
            
        elif choice == 2:
            # Option 2: Withdraw money
            withdraw_amount = int(input("Enter amount to withdraw: "))  

            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"${withdraw_amount} withdrawn. New balance: ${balance}")
            else:
                print("Insufficient funds.")
                
        elif choice == 3:
            # Option 3: Exit
            print("Thank you for using the ATM. Goodbye!")
            break
            
        else:
            print("Invalid option. Please try again.")
else:
    print("Incorrect PIN")

                # Task 3

   
    correct_username = "admin"
    correct_password = 12345
    
    # Get 
    username = input("Enter username: ")
    password = int(input("Enter password: "))
    
    # Check 
    if username == correct_username and password == correct_password:
        print("Login Successful!")
    elif username != correct_username:
        print("Incorrect username")
    elif password != correct_password:
        print("Incorrect password")



