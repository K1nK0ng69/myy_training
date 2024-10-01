n = int(input())
m = int(input())
value = int(input())

def get_matrix(n, m, value):
    matrix = [[value for _ in range(m)] for _ in range(n)]
    return matrix
result_matrix = get_matrix(n, m, value)
print(result_matrix)