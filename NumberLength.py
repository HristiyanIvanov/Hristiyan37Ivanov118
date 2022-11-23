n = int(input('Num: '))
li = list()
total = 0
for i in range(1,n+1):
    li.append(int(f'{n}'*i))
    total = total + li[-1]
print(*li, sep=' + ', end='')
print(' =',total)
