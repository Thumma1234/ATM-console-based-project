print("****************")
print("Welcome to ATM !")
print("****************")

accounts = {
    1111 : ["sowmya","12-12-2002",10000,1234],
    2222 : ["sandhya","30-04-2001",20000,1020],
    3333 : ["rani","01-01-2003",5000,None],
    4444 : ["ram","02-02-2003",15000,2468],
    }
dobm = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"July",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
while True:
    print("Choose Your Option")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Pin Generation")
    print("4. Mini Statment")
    print("5. Balance")
    print("6. Exit")
    option = int(input("Enter Your Option: "))
    print()
    if option == 1:
        print("****************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exit !")
        else:
            pin = int(input("Enter Pin: "))
            if accounts[accno][-1] == None:
                print("Generate Pin")
            else:
                if accounts[accno][-1] != pin:
                    print("Invalid Pin")
                else:
                    amt = int(input("Enter Amount to Withdraw: "))
                    if amt > accounts[accno][-2]:
                        print("Insufficient Funds")
                    else:
                        print("Withdraw Successful !")
                        accounts[accno][-2] -= amt
            print(accounts[accno])
        print("****************")
    elif option == 2:
        print("****************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account does not exit")
        else:
            amt = int(input("Enter Amount to deposit: "))
            accounts[accno][-2] += amt
            print("Deposit Successfull")
            print(accounts[accno])
        print("****************")
    elif option == 3:
        print("****************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Account Does not Exists")
        else:
            if accounts[accno][-1] == None:
                pin = int(input("Enter Pin: "))
                cpin = int(input("confirm Pin: "))
                if pin != cpin:
                    print("Pin Does not Match")
                else:
                    accounts[accno][-1] = pin
                    print("Pin Generated Successfully")
            else:
                print("Pin already Exist")
            print(accounts[accno])
        print("****************")
    elif option == 4:
        print("****************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Accounts does not Exist")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][-1]:
                print("Invalid Pin")
            else:
                print(f"Name: {accounts[accno][0]}")
                print(f"Account number: [accno]")
                dob = accounts[accno][1].split("-")
                
                date = dob[0]
                month = dobm[int(dob[1])]
                year = dob[2]
                dob = date + "-" + month + "-" + year
                print(f"Date of Birth: {dob}")
                print(f"Account Balance: {accounts[accno][-2]}")
                
        print("****************")
    elif option == 5:
        print("****************")
        accno = int(input("Enter Account Number: "))
        if accno not in accounts:
            print("Accounts does not Exist")
        else:
            pin = int(input("Enter Pin: "))
            if pin != accounts[accno][-1]:
                print("Invalid Pin")
            else:
                print(f"Your current Balance is: {accounts[accno][-2]}")
        print("****************")
    else:
        break
        
            

