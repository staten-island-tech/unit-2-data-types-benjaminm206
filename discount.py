addup = []
total = 0
price = 0
done = False
while done == False:
    price = int(input("Insert the price of ONE item only: $"))
    addup.append(price)
    print("Items:")
    print(addup)       
    cont = input("Would you like to insert another item, or are you done? Type either 'done' or 'cont': ")
    if cont == "done" or cont == "Done":
        done = True
        total = sum(addup)
        if total >= 100:
            print()
            print(f"Since you spent at least $100, a 10 percent discount was applied. Your total is $")
            print(total * 0.9)
            break
        else:
            print()
            print("Your total is $")
            print(total)
            break

