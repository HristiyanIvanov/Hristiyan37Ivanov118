def input_nums(n):
    list = []
    for i in range(n):
        num = input('Enter num: ')
        if type(num) == int or num.isnumeric():
            list.append(num)
    return list

def sum_list(lst):
    sum = 0
    for i in lst:
        if type(i) == int or type(i) == float:
            sum += i
        elif type(i) == str and i.isnumeric():
            sum += float(i)
    return sum

def max_of_two(a, b):
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            return a if a >= b else b
        return a
    if type(b) == int or type(b) == float: return b
    return
