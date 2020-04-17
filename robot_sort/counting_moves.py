# Program used to count moves when moving cards in real life

total = 0
while True:
    print("\n\nTotal moves: " + str(total) + "\n")
    user_in = input(">> ")

    if user_in == "q":
        exit()
    else: 
        total += 1