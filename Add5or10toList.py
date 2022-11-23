n = int(input('End of list: '))
li = list()
for i in range(n+1):
    li.append(i)
x = int(input('Enter 0 or 1: '))
for i in range(0,len(li)):
    if x == 0 and li[i] % 2 == 0:
        li[i] += 5
    if x == 1 and li[i] % 2 != 0:
        li[i] += 10
    print(li[i], end=' ')

#Друг вариант
n = int(input('End of list: '))
x = int(input('Enter 0 or 1: '))
li = list(i for i in range(0, n+1))
if x == 0:
    for i in range(0,n,2):
        li[i] += 5
    print(li)
elif x == 1:
    for i in range(1,n,3):
        li[i] += 10
    print(li)
else:
    print('Input 1 or 0')
