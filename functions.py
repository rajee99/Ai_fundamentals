def cal_sum(a, b):
    sum = a + b
    print(sum)
    return sum


cal_sum(5, 5)
cal_sum(10, 5)

a = 2
b = 10


heros = ["superman", "Batman", "WonderWoman", "Goldman"]

def print_len(anyKindOfList):
    return len(anyKindOfList)

print(print_len(heros))

def printListInaSingleLine(AnyList):
    for lists in AnyList:
        print(lists, end=" ")

printListInaSingleLine(heros)

def calFact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(calFact(5))

 