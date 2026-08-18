#Making a shopping list program.
import sys

print("<===============================================================>")
print("*Welcome to Ruezio Store, here you can find everything you want*")
print("*Powered By Ruezio*")
print("*Build on Trust*")
print("<===============================================================>\n")

name = input("--> What is your name?: ")
if name.replace(" ","").replace(".","").isalpha():
    if len(name) > 20:
        print("!YOUR USERNAME CANT BE MORE THAN 20 LETTERS\nWRITE THE FIRST 20 LETTERS OF YOUR NAME!")
        sys.exit()
    else:
        print(f"Hello {name}\nWelcome to the Store")
else:
     print("!NAME CANNOT CONTAIN SPECIAL CHARACTERS!")
     sys.exit()

#*ITEM*#

item = input("--> What item do you want?: ").lower().strip() # type: ignore

item_count = item.count(",")
if item.replace(",","").replace(" ","").isalpha():
    print("Done")
else:
    print("!INVALID ITEM NAME!")
    sys.exit()

#*PRICE*#

price = input("--> What is the price?: ")

if price.replace(".","").isdigit():
    print("Done")
    price = float(price)
else:
    print("!TRY WRITING IN NUMBERS!")
    sys.exit()

#*QUANTITY*#

quantity = input(f"--> How many {item}s do you want(in numbers)?: ")

if quantity.isdigit():
    print("Done")
    quantity = int(quantity)
else:
    print("!INVALID QUANTITY!")
    sys.exit()

#*TOTAL*#

total = price * quantity

print(f"For {quantity} {item}s, Your total will be ${total}")

#Budget

budget = input("-->What is your budget:$ ")
if budget.replace(".","").isdigit():
    budget = float(budget)
    if budget >= total:
        print("Done")
    else:
        print("Your Total is more than your budget")
        sys.exit()
else:
    print("!INVALID BUDGET!\nTry writing in numbers")
    sys.exit()

#*PAYMENT*#

payment = input("--> How would you like to pay sir? Cash or Card?: ").lower()

if payment == "cash":
    print("You can visit our counter now")
elif payment == "card":
    print("Scan your card with the scanner on your right hand side -->")
else:
    print("Invalid payment method")
    sys.exit()

#*Confirmation*#

conm = input("--> Write 'Yes' once its done, Write 'No', if its not: ").lower()      # conm, here stands for confirmation btw if anyone wondering # conm, here stands for confirmation btw if anyone wondering

if conm == "yes":
    print("Thank You, Visit Again :D")
elif conm == "no":
    print("Sorry for the inconvenience, PLEASE TALK TO OUR STAFF IN THE COUNTER")
else:
    print("ERROR")
    sys.exit()

#*Marketing*#

print("<======================================================>")
print("*This program is in beta, will improve this in future*")
print("*WE SELL TRUSTED PRODUCT*")
print("*Ruezio Store*")
print("*Rate us in our website*")
print("*ruezio***@gmail.com*(fictioinal)")
print("<======================================================>")

