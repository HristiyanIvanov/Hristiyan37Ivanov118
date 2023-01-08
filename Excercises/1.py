"""
Зад. 1. Напишете програма, в която потребителя въвежда две цели положителни числа n и k.
След това въвежда още толкова числа, колкото е стойността на n (например: ако п=10, се въвеждат още 10 числа).
Създайте два списъка. (7 т.) В първия списък да се добавят само тези числа от въведените n на брой,
които са по-големи от k. Да се намери произведението на елементите от този списък, чиито индекси са нечетни.
Да се намери индекса на елемента с минимална стойност. (15 т.) Във втория списък да се добавят тези числа от введените n на брой,
които са по-малки или равни на k и са положителни. Да се намери разликата между елемента с максимална
и елемента с минимална стойност. (15 Т.)
"""

import math

list1 = []
list2 = []
while True:
    try:
        n = int(input("N= "))
        k = int(input("K= "))
        if n < 0:
            print("Sorry, N must be a positive integer, try again")
            continue
        elif k < 0:
            print("Sorry, K must be a positive integer, try again")
            continue
        break
    except ValueError:
        print("That's not an int!")
    except Exception as e:
        print(e)


for i in range(n):
    x = int(input("X= "))
    if x > k:
        list1.append(x)
    if x <= k and x > 0:
        list2.append(x)
print(list1)

print("List Index: ", list1.index(min(list1)))
mult = 1
for i in range(1, len(list1), 2):
    mult *= list1[i]
print("Multiply Result: ", mult)

print(list2)
if not list2:
    print("The list is empty")
else:
    print("Subtraction: ", max(list2) - min(list2))
