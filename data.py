# Strings represent characters, names, words
name = "Kammy"
# Integers for whole numbers
age = 14
# Boolean is True of False, typically used for evaluations
graduated = False
# Floats for decimal
money = 4.50

def add(x,y):
    print(round(x + y))
""" add(54, "11") """
# Input seeks user response and outputs that into the variable
# Bill value will be equal to the response of the user
# Input result is a string
bill = float(input("How much was the bill?"))
add(15,bill)

# Lists which store lists of data
students = ["Kammy", "Rachel", "Denis", "Ian", "Chaojie?", "Superior Alexander", "Inferior Alexander"]
moneys = [1,2,3,4,5,6]
# similar to for i in range(4)
# scaleable
for student in students:
    print(student)
x = 0
for money in moneys:
    x = x + money
    print(x)