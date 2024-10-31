age = int(input("How old are you")) #we ask for the age of the person

if age >= 18 and age <= 64:         #Sees if age elgible for adult tickets or child and senior tickets
    membership = input("do you have a membership? Answer true or false? ".lower()) #Do they have a membership
    if membership == "true":           #asks if they have a membership
        print("Discounted adult ticket price is $12 ")
    else:                              #means they have no membership
        print("Regular adult ticket price is $15 ")  
elif age >= 65: #if age is over 65 is will print the price of the senior ticket
    print("Senior discount price is $8 ")
else:           #if age is under 18 it will print the price of the senior ticket
    print("Youth ticket price is $10")

computer = input("Is computer on? Answer with yes or no. ".lower()) # Asks if the computer is on to begin with
Wi_fi = input("Are you connected to Wi-Fi? Answer with yes of no. ".lower()) # asks if your connected to the internet


if computer == "yes": #if computer is on itll excute the nested if statement
    if Wi_fi == "no": #countiues the if statement if wi-fi is not on 
        Icon = input("Do you see the wi-fi icon? Answer yes or no. ".lower())
        if Icon == "yes": #Tells us if the icon is visible and help determine if you should reconnect of ask for support.
            print("Try reconnecting to the wi-fi network.") #if they see the icon then it'll print this
        else:
            print("Please check you Wi-Fi settings or contact support.") #if they can't see the icon it will print this
    else:
        print("You are online") #if wifi is on then it prints this out
else:
    print("Please turn on your computer") # if computer is off it'll tell the user to turn on the computer


