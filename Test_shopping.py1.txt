#Testin 404

import sys

print("<===============================================================>")
print("*Welcome to Ruezio Store, here you can find everything you want*")
print("*Powered By Ruezio*")
print("<===============================================================>\n")

name = input("--> What is your name?: ")

if name.replace(" ","").replace(".","").isalpha():
     print(f"Hello {name}")
else:
     print("Name cant contain special characters or numbers")           #So this was me combining everything that i had learned so far, but inputs are the a function that prompts the user to enter a data.
     sys.exit()                                                         #Actual and normal input command is input("WHATEVER YOU WANT TO ASK:")

#*ITEM*#

item = input("--> What item do you want?: ").lower().strip() # type: ignore

if item.replace(",","").replace(" ","").isalpha():
    print("Done")
else:
    print("Invalid Item Name")
    sys.exit()

#*PRICE*#

price = input("--> What is the price?: ")

if price.replace(".","").isdigit():
    print("Done")
    price = float(price)
else:
    print("TRY WRITING IN NUMBERS")
    sys.exit()

#*QUANTITY*#

quantity = input(f"--> How many {item}s do u want(in numbers)?: ")

if quantity.isdigit():
    print("Done")
    quantity = int(quantity)
else:
    print("TRY WRITING IN NUMBERS")
    sys.exit()


#*TOTAL*#

total = price * quantity

print(f"For {quantity} {item}s, Your total will be ${total}")

#*PAYMENT*#

payment = input("--> How would you like to pay sir? Cash or Card?: ").lower()

if payment == "cash":
    print("You can visit our counter now")
elif payment == "card":
    print("Scan your card with the scanner on your right hand side -->")
else:
    print("Invalid payment method")
    sys.exit()

#*LAST*#

Last = input("--> Write 'Ok' once its done, Write 'No', if its not: ").lower()

if Last == "ok":
    print("Thank You, Visit Again :D")
elif Last == "no":
    print("Sorry for the inconvenience, PLEASE TALK TO OUR STAFF IN THE COUNTER")
else:
    print("ERROR")
    sys.exit()

#*Marketing*#

print("<=====================================================>")
print("*This program is in beta, will improve this in future*")
print("*WE SELL TRUSTED PRODUCT*")
print("*Ruezio Store*")
print("*Rate us in our website*")
print("*ruezioabc@gmail.xom*")
print("<======================================================>")

