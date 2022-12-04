n1 = int(input())
print(bin(n1) [2:])

binar = int(bin(n1) [2:])
myList = list(map(int,str(binar)))

n2 = int(input())
if myList[n2] == 1 :
    print("The number is 1")
else:
    print("The number is 0")
