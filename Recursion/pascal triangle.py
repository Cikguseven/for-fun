# Recursive function to generate Pascal's triangle (up to row n)

def pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        row_above = pascal_triangle(n-1)[-1]
        current_row = [1]
        for i in range(n-2):
            current_row.append(row_above[i] + row_above[i+1])
        current_row += [1]
        triangle = pascal_triangle(n-1)
        triangle.append(current_row)
        return triangle


print(pascal_triangle(3))