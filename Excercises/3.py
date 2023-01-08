list1 = []
list2 = []

while True:
    try:
        n = int(input("N= "))
        while n != 0 and n > 0:
            if n % 3 == 0 and n % 2 == 0:
                list1.append(n)
            if n % 7 == 0 and n % 2 != 0:
                list2.append(n)
            n = int(input("N= "))
        break
    except ValueError:
        print("Input integer.")
    except Exception as e:
        print(e)

print(list1)
print(list2)
SumList1 = []
if not list1:
    print('Empty list')
else:
    for i in range(len(list1)):
        if i % 2 != 0:
            SumList1.append(i)
    print("Sum of odd indexes in first list:", SumList1)
if not list2:
    print('Empty list')
else:
    print(sorted(list2, reverse=True))
    print("Min * Max element: ", max(list2) * min(list2))
