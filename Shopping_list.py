#This is my experiment.py file, i'll do all different things here to test things.
import sys
#INTRODUCTION
print("*=============================================================*")
print("Welcome to Ruezio Store, here you can find everything you want")
print("Powered by Ruezio.Inc")
print("*==============================================================*")

#NAME

name = input("-->What is your name: ").strip()

if name.replace(" ","").replace(".","").isalpha():
    print(f"Hello {name}")
else:
    print("INVALID NAME \nTry using letter not numbers")
    sys.exit()
#ITEMS

item = input("-->What item(s) do you want: ").lower().strip()
if item.replace(" ","").replace(",","").isalpha():
    print("Done")
else:
    print("INVALID ITEM NAME \nItem Name cant contain numbers and special characters")
    sys.exit()
#*price*
price = input("-->What is the price: ")

if price.replace(".","").isdigit():
    print("Done")
    price = float(price)
else:
    print("INVALID PRICE \nUse numbers for price")
    sys.exit()

#QUANTITY

quantity = input(f"-->How many {item}s do you want(in numbers): ")
if quantity.isdigit():
    print("Done")
else:
    print("INVALID QUANTITY \nUse numbers instead of letters")
    sys.exit()
#TOTAL
quantity = int(quantity)

total = price * quantity

print(f"For {quantity} {item}s, your total will be: ${total}")

#PAYMENT
payment = input("-->How would you like to pay sir/ma'am, Card or Cash: ").lower()

if payment == "cash":
    print("You can visit our counter now")
elif payment == "card":
    print("Scan your card right here -->")
else:
    print("INVALIND PAYMENT METHOD \nTry writing Card or Cash")
    sys.exit()
#Last 
last = input("-->If its done, type Yes and if its not type No: ").lower()
if last == "yes":
    print("Thank you, Visit Again :D")
elif last == "no":
    print("Sorry for the inconvenience, please talk to our staff")
else:
    print("INVALID INPUT")
    sys.exit()
print("/*=====================================================* ")
print("*This program is in beta, will improve this in future*")
print("*WE SELL TRUSTED PRODUCT*")
print("*Ruezio Store*")
print("*Rate us in our website*")
print("*======================================================*")
