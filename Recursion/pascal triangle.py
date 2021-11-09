# Recursive function to generate Pascal's triangle (up to row n)

def pt(n):
    if n == 1:
        return [[1]]
    else:
        previous_row = pt(n - 1)[-1]
        current_row = [1]
        for i in range(n-2):
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]
        triangle = pt(n-1)
        triangle.append(current_row)
        return triangle


print(pt(8))

# Faster iterative solution
'''
from math import comb

def pt(n):
    triangle = []
    for i in range(n):
        current_row = []
        for j in range(i + 1):
            current_row.append(comb(i, j))
        triangle.append(current_row)
    return triangle

print(pt(20))
'''