# Recursive function to generate sum of first n integers

def integer_sum(n):
    if n == 0:
        return 0
    else:
        return integer_sum(n - 1) + n


for i in range(11):
    print(integer_sum(i))
