#atm code
balance = 20000
code = input("To get the pincode entre your state's capital 'remember it should be from India especialy if you are from kashmir also write the season using and'use uppercase letter at first :- ")

#pincode logic (This happens only once at the start)
if(code=="srinager and winter"):
    print("Your code is--->190001")
elif(code=="srinager and summer"):
    print("Your code is--->180001")
elif(code=="Amaravati"):
    print("Your code is--->522503")
elif(code=="Itanagar"):
    print("Your code is--->791111")
elif(code=="Dispur"):
    print("Your code is--->781005")
elif(code=="Patna"):
    print("Your code is--->800001")
elif(code=="Raipur"):
    print("Your code is--->492001")
elif(code=="Panaji"):
    print("Your code is--->403001")
elif(code=="Gandhinagar"):
    print("Your code is--->382010")
elif(code=="Chandigarh"):
    print("Your code is--->160017")
elif(code=="Shimla"):
    print("Your code is--->171001")
elif(code=="Ranchi"):
    print("Your code is--->834001")
elif(code=="Bengaluru"):
    print("Your code is--->560001")
elif(code=="Thiruvananthapuram"):
    print("Your code is--->695001")
elif(code=="Bhopal"):
    print("Your code is--->462001")
elif(code=="Mumbai"):
    print("Your code is--->400001")
elif(code=="Imphal"):
    print("Your code is--->795001")
elif(code=="Shillong"):
    print("Your code is--->793001")
elif(code=="Aizawl"):
    print("Your code is--->796001")
elif(code=="Kohima"):
    print("Your code is--->797001")
elif(code=="Bhubaneswar"):
    print("Your code is--->751001")
elif(code=="Jaipur"):
    print("Your code is--->302001")
else:
    print("Your code is--->455595")

pincode = int(input("Entre your code:- "))
customername = input("Entre your name:- ")
customreage = int(input("Entre your age:- "))

atm_on = True

# --- START OF THE LOOP ---
while atm_on == True:
    # Everything below is INDENTED (pushed to the right)
    print(f"\n--- Welcome {customername} to SBI Bank ---")
    print(f"Current Balance: ₹{balance}")
    customerinput = input("Would you like to deposit, withdraw, see balance, or exit: ").lower()

    if(customerinput == "deposit"):
        d = int(input('Entre your deposit amount---> '))
        balance = balance + d  # This updates the balance in memory
        print(f"Your recent balance: ₹{balance}\nThanks for choosing our bank 'HAVE A NICE DAY🥰'")

    elif(customerinput == "withdraw"):
        e = int(input('Entre your withdraw amount---> '))
        if(e > balance):
            print("Invalid input. Insufficient funds.")
        else:
            balance = balance - e  # This updates the balance in memory
            print(f"You will get ₹{e}. Remaining balance: ₹{balance}\nThanks for choosing our bank'HAVE A NICE DAY🥰'")

    elif(customerinput == "see balance"):
        print(f"Your recent balance is: ₹{balance}")

    elif(customerinput == "exit"):
        print("ATM Shutting down... HAVE A NICE DAY🥰")
        atm_on = False  # This stops the loop gracefully
    
    else:
        print("Unknown command. Please try again.")

print("Program Finished.")
