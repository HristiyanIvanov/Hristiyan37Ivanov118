n = int(input('Num: '))
ch1 = 0
ch2 = 1
result = 0

for i in range(0,n+2):
    print(ch1)

    result = ch1+ch2
    ch1=ch2
    ch2=result
