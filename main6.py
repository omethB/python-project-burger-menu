bread = {'tiger':5,'herbal': 7,'soft':6,'cheese':8}
toppings = {'chicken':7,'sea-food':8,'pork':9,'vegetarian':7}

print("HELLO WELCOME TO CHEAP BURGER!!!.."+ "\n"+ "PLEASE GO THROUGH OUR MENU AND CHOOSE THE TYPE OF BREAD AND TOPPING TO YOUR BURGER." +"\n")

contactno = int(input("Enter your contact number: "))
nooforders = int(input("How many burgers would you be ordering today? "))

##############################################################################
a = 0
finalbill = 0
transation1 = 0
transation2 = 0
no = 1
##############################################################################

while(a<nooforders):
    print("\n")
    print("#BURGER "+str(no))
    print("TYPE OF BREAD WITH THEIR COST")

    n = 1
    for k in bread:
        record = str(n) + "." + str(k) + " = Rs." + str(bread[k])
        n = n +1
        print(record)
    choice1 = input("Enter your choice of bread by entering the number represented by the bread type: ")

    print("\n")

    print("TYPE OF TOPPING WITH THEIR COST")

    i = 1
    for k in toppings:
        record = str(i) + "." + str(k) + " = Rs." + str(toppings[k])
        print(record)
        i = i + 1

    choice2 = input("Enter your choice of bread by entering the number represented by the bread type: ")

    print("\n")

########################################################################################################

    breadtype = {'1':'tiger','2':'herbal','3':'soft','4':'cheese'}
    toppingtype = {'1':'chicken','2':'sea-food','3':'pork','4':'vegetarian'}


    for k in breadtype:
        if k == choice1:
            valid = breadtype[k]
            transaction1 = (bread[valid])

    for k in toppingtype:
        if k == choice2:
            valid = toppingtype[k]
            transaction2 = (toppings[valid])

    total = transaction1 + transaction2
    finalbill = finalbill + total
    a = a+1
    no = no + 1
print("PRICE OF THE TOTAL BILL IS RS." + str(finalbill))




