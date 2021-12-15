import time
import math

print("Welcome to the circle helper... Please choose what value you want to be found for you below:")
time.sleep(1)
print("\t1. Circumference")
time.sleep(1)
print("\t2. Area")
time.sleep(1)
print("\t3. Diameter")

user_choice = int(input("Enter the 'number' of the choice you want here (Ex: Put 2 for Area) "))

time.sleep(1)

if user_choice == 1:
    r = int(input("Enter the radius: "))
    result = 2 * math.pi * r
    print(round(result, 2))
elif user_choice == 2:
    r = int(input("Enter the radius: "))
    result = math.pi * r ** 2
    print(round(result, 2))
elif user_choice == 3:
    c = int(input("Enter the circumference: "))
    result = c / math.pi
    print(round(result, 2))