import random as rand

worm = ["Digging", "Resting", "Nothing"]

user = input("Input (h for help): ")
user = user.lower()

while(user != "q" and user != "quit"):
    if(user == "h"):
        print("quit/q - exit program \nsup - worm response")
    elif(user == "sup"):
        print(rand.choice(worm))
    else:
        print("Invalid input.")
    
    user = input("Input (h for help): ")
    user = user.lower()