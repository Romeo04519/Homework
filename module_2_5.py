def get_matrix(n = 1, m = 1, value = 1):
    matrix = []
    if value <= 0: # задание в примечании возращать пустой список при аргументе <=0
        return matrix
    else:
        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(value)
        return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
