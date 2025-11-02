def num_arr(numbers):

    length = len(numbers)
    sum_of_nums = sum(numbers)
    avg = sum_of_nums/length
    return  avg

sum = num_arr([1, 2, 3, 4, 5])
print(sum)

def add(a, b):
    sum = a+b
    return sum


addnum = add (2, 4)
print (addnum)