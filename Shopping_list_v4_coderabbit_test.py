#Making a shopping list program.
import sys

print("<===============================================================>")
print("*Welcome to Ruezio Store, here you can find everything you want*")
print("*Powered By Ruezio*")
print("*Build on Trust*")
print("<===============================================================>\n")

name = input("--> What is your name?: ")

while not name.replace(" ","").replace(".","").isalpha() or len(name) > 20:

    if not name.replace(" ","").replace(".","").isalpha():
        print("INVALID NAME\nTry Again!")
        name = input("--> What is your name?(without special characters): ")

    elif len(name) > 20:
        print("Your name is more than 20 letters\nTry writing the first 20 letters of your name")
        name = input("--> What is your name?(with first 20 characters): ")
        
print(f"Hello {name} :D\nWelcome to the store!")


#*ITEM*#

item = input("--> What item do you want?: ").lower().strip()
item_count = item.count(",")

while not item.replace(",","").replace(" ","").isalpha():

    print("INVALID ITEM NAME\nTry Again!")
    item = input("--> What item do you want?: ").lower().strip()

print("Done")


#*PRICE*#

price = input("--> What is the price?: ").lower().strip()

while not price.replace(".","").replace(",","").isdigit():

    print("TRY WRITING IN NUMBERS\nTry Again!")
    price = input("--> What is the price?: ").lower().strip()

price = float(price.replace(",",""))
print("Done")


#*QUANTITY*#

quantity = input("--> How many items do you want(in numbers)?: ")

while not quantity.isdigit():

    print("!INVALID QUANTITY!")
    quantity = input(f"--> How many {item}s do you want(in numbers)?: ")

print("Done")
quantity = int(quantity)

#*TOTAL*#

total = price * quantity

print(f"For {quantity} {item}s, Your total will be ${total:,.2f}")


#Budget

budget = input("-->What is your budget:$ ")

while not budget.replace(".","").replace(",","").isdigit():

    print("!INVALID BUDGET!\nTry writing in numbers")
    budget = input("-->What is your budget:$ ")

budget = float(budget.replace(",",""))

if budget >= total:
    print("Done")

else:
    print("Your Total is more than your budget")
    budget_conf = input("-->Want to re-enter your budget?(Y or N): ").lower().strip()

    if budget_conf == "y":
        new_budget = input("-->What is your budget:$ ")

        while not new_budget.replace(".","").replace(",","").isdigit():

            print("!INVALID BUDGET!\nTry writing in numbers")
            new_budget = input("-->What is your budget:$ ")

        new_budget = float(new_budget.replace(",",""))
        if new_budget >= total:
            print("Done")
        elif new_budget < total:
            print("Your budget is still lower than you total\nSYSTEM RESTARTING\n*If you want to try again, run the program again*")
            sys.exit()

    elif budget_conf == "n":
        print("Done")
        sys.exit()


#*PAYMENT*#

payment = input("--> How would you like to pay sir? Cash or Card?: ").lower().strip()

while not payment == "cash" and not payment == "card":

    print("INVALID INPUT")
    payment = input("--> How would you like to pay sir? Cash or Card?: ").lower().strip()

if payment == "cash":
    print("Done\nYou can visit the counter now")
elif payment == "card":
    print("Done\nYou can Scan the QR on the right side-->")


#*Confirmation*#

conf = input("--> Write 'Yes' once its done, Write 'No', if its not: ").lower()      # conf, here stands for confirmation btw if anyone wondering # conm, here stands for confirmation btw if anyone wondering

while not conf == "yes" and not conf == "no":
    print("INVALID INPUT")
    conf = input("--> Write 'Yes' once its done, Write 'No', if its not: ").lower()

if conf == "yes":
    print("Thank You, Visit Again :D")
elif conf == "no":
    print("Sorry for the inconvenience, PLEASE TALK TO OUR STAFF IN THE COUNTER")


#*Marketing*#

print("<======================================================>")
print("*This program is in beta, will improve this in future*")
print("*WE SELL TRUSTED PRODUCT*")
print("*Ruezio Store*")
print("*Rate us in our website*")
print("*ruezio***@gmail.com*(fictioinal)")
print("<======================================================>")

 
