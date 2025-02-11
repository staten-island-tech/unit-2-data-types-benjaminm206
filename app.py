""" x = 3
y = float(3)
print(x,y)

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) """

# Challenge notes:
# I will create an input where the terminal will ask a question
# When the user responds, it will count the number of words in the string
# display the number it recieves
""" x = input("What month are we in?")
y= x.split( )
z = y[0]
print(y)
print(z)
count = len(y)
print(count)

time_of_day = input("What month is it?") 
 """
# temperature thing

""" x = "test"
print(f"hello {x}")

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

# odd/even ifyer
# if number ends in 0, 2, 4, 6, 8 --> number is even
# else --> number is odd

number = input("Insert a number")
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
