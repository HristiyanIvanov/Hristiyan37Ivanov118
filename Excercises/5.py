list1 = []
list2 = []
while True:
    try:
        n = int(input("Enter amount: "))

        for i in range(n):
            k = int(input("Enter N: "))
            if k % 2 == 1 and k % 3 == 0:
                list1.append(k)
            if k % 2 == 0:
                list2.append(k)
        break
    except ValueError:
        print("Enter integer!")

print(list1)
print(list2)
if not list1:
    print("The list is empty")
else:
    print(f"Min: {min(list1)} | Max {max(list1)}")
if not list2:
    print("The list is empty")
else:
    print(f"Sum: {sum(list2)}")
    print(f"Average: {sum(list2) / len(list2)}")
