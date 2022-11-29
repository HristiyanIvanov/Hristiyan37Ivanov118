def list_avg(lst,multiplier=1):
    average=0
    count=0
    for i in lst:
        if type(i)==str and i.isnumeric():
            average += int(i) * multiplier
            count += 1
        elif type(i)==int or type(i)==float:
           average += i * multiplier
           count+=1
    if count==0:
        return 'Error: Division by zero\nNone'
    return average/count

print(list_avg(['4', 1.5, "@7$", 3.5, (1, "hi")]))
print(list_avg(['6', 3, 3.0], 2))
print(list_avg(['%$', {}]))
print(list_avg([]))
