dict = {}
list = list()
n = int(input('Enter iterations: '))
for i in range(0,n):
    key = input('Enter key: ')
    value = input('Enter value: ')
    dict[key]=value
print(dict)
m = int(input('Enter iterations: '))
for i in range(m):
    lvalue = input('Enter value: ')
    if lvalue in dict.keys():
        list.append(dict[lvalue])
        dict.pop(lvalue)
        continue
    list.append(lvalue)

print(dict)
print(list)
