# While loops = excutes some code while some condition remains true
# While loops and for loops
# are forms of iteratrion
# iteration is the process of
# reapearting or looping through
# a set of steps or instructions
# to iterate is the verb
# form of iteration
# be careful of infinite loops\
# they will crash your program
# and you will have to restart it
# infinite loops are loops that never end

# name = input("Enter you name: ")
# # if name == "":
# #     print("You did not enter your name")

# # else:
# #     print(f"Hello {name}")

# #This will run forever control c stops it
# while name == "":
#     print("You did not enter your name")

# print(f"Hello {name}")

#Gives user a ecsape route
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
#     print(f"Hello {name}")

#another example of while loop

# age = int(input("Enter your age:"))

# while age < 0:
#     print("Age can't be be negative")
#     age = int(input("Enter your age:" ))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit): ")

# #Won't end the loop until you type in q
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")

# num = int(input("Enter a number between 1 - 19: "))

# while num < 1 or num > 10:
#     print(f"{num} is not vaild")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f"Your number is {num}")
# for loops = execute a block of code a fixed number of times 
# You can iterate over a range, string, sequence, etc.

#counts up to 11
# for x in range(1,11):
#     print(x)

#counts by 2
# for x in range(1, 11, 2):
#     print(x)


#Counts down due to reversed
# for x in reversed(range(1,11)):
#     print(x)

# print("HAPPY NEW YEAR! ")

#prints out the credit card number

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)


# for x in range(1,21):
#     if x ==13:
#         continue # skips over 13 
#     else:
#         print(x)

# #Or operator can help skip oiver multiple numbers 
# for x in range(1,21):
#     if x ==13 or x ==15 or x==19:
#         continue # skips over 13, 15 ,19
#     else:
#         print(x)

# for x in range(1,21):
#     if x ==13:
#         break # stops counting at 12 
#     else:
#         print(x)

horror_movies = ["The Exorcist","The Shining","The Conjuring","The Ring"]


for x in horror_movies:
    if x == "The Shining":
        print("The Shining")
        print(x)
        break
    else: 
        print("The Shining was not found")
        print(x)

horror_char = ["chucky", "Freddy Krueger", "Freddy Fazbear", "Jason" ]


for x in horror_char:
    if x == "Freddy Krueger":
        continue
    else: 
        print(x)

horror_monsters = ["Zombie","Swamp Thing","Alien","Godzilla"]


for x in horror_monsters:
    if x == "Swamp Thing":
        x = "William Aftongit" 
        print(x)
    else: 
        print(x)
