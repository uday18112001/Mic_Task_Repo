import time
time.sleep(3)
password=12345
pin=int(input("enter your ATM pin:"))
balance=50000
if pin==password:
    while True:
        print(""" 
           1==balance
           2==withdraw amount
           3==deposite ammount
           4==transfer amount
           5==quit
                  """)
        try:
            option=int(input("please enter your choice:"))
        except:
            print("please enter valid option")

        if option==1:
             print(f"your current balance is={balance}")

        if option==2:
            withdraw_amount=int(input("please enter withdraw_amount:"))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debeted from your account ********123")
            print(f"your current balance is ={balance}")

        if option==3:
            deposit_amount=int(input("please enter your deposit amount:"))
            balance=balance + deposit_amount
            print(f"{deposit_amount} is credited to your account ********123")
            print(f"your current balance is ={balance}")

        if option==4:
            transfer_amount=int(input("please enter your transfer_amount:"))
            balance=balance - transfer_amount
            print(f"{transfer_amount} is debited from your account ********123")
            print(f"your current balance is ={balance}")

        if option==5:
            break
else:
                                                                                                                                                                                 print("wrong pin,please try again")



