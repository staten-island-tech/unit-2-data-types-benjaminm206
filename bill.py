bill = int(input("Insert the subtotal bill value:   $"))
service = input("Rate your service by typing one of the following: Bad, Okay, Good, or Great (case sensitive: make first letter capital): ")
# If service is bad, apply no tip
if service == "Bad":
    print(f"Sorry for your unsatisfactory experience. No tip was applied. Your total is ${bill}.")
# If service is okay, apply 15% tip.
elif service == "Okay":
    tip = bill * 0.15
    total = bill + tip
    print(f"15% tip was applied. Your total is ${total}.")
# If service is good, apply 20% tip.
elif service == "Good":
    tip = bill * 0.20
    total = bill + tip
    print(f"20% tip was applied. Your total is ${total}.")
# If service is great, apply 25% tip.
elif service == "Great":
    tip = bill * 0.25
    total = bill + tip
    print(f"Glad you enjoyed your meal! 25% tip was applied. Your total is ${total}.")