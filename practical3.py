# TO create program to find five exception handling

a= int(input("Enter no1: "))
b =int(input("Enter second Number: "))
try:
    c = a/b
except ZeroDivisionError:
    print("Numberator is not divisible by 0")
except :
    pass

