addup = []
total = 0
price = 0
done = False
while done == False:
    price = int(input("Insert the price of each item, one by one. Press enter after each item: $"))
    
        cont = input("Would you like to insert another number, or are you done? Answer with either 'insert' or 'done': ")
    if cont == "done" or cont == "Done":
        break
    
""" total = #Add all the numbers in a list
while done == True:
    if total >= 100:
        print(total * 0.9)
    else:
        print(total) """