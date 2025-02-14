# odd/even ifyer
# if number ends in 0, 2, 4, 6, 8 --> number is even
# else --> number is odd

""" number = int(input("Insert a number"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd") """

# factor finder
# 

""" number = int(input("Insert a number: "))
for i in range(1, number + 1):
    if number % i == 0:
        print(i) """

# gcf-ifyer

numfac1 = []
numfac2 = []

num1 = int(input("Insert the first number: "))
num2 = int(input("Insert the second number: "))

for i in range(1, num1 + 1):
    if num1 % i == 0:
        numfac1.append(i)

for u in range(1, num2 + 1):
    if num2 % u == 0:
        numfac2.append(u)

def gcf(numfac1, numfac2):
    common_factor = set(numfac1) & set(numfac2)

    if common_factor:
        return max(common_factor)
    else:
        return None
    
result = gcf(numfac1, numfac2)
if result > 1:
    print(f"The GCF is {result}.")
elif result < 1.1:
    print(f"No GCF found")
