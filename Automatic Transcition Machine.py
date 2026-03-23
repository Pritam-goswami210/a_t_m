#atm code
balance = 10000
customerinput = input("Would to like to deposit or withdraw:- ")
if(customerinput=="deposit"):
    d = (int(input('Entre your deposit amount---> ')))
    sum = 10000+d
    print("Balance:",sum,"rupees")
elif(customerinput=="withdraw"):
    e = (int(input('Entre your deposit amount---> ')))
    sub =10000-e
    print("You will get",sub,"rupees")
else:
    print("Error:unknown variable writen")
    exit()