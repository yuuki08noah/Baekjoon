import sys

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __mul__(self, other):
        res_matrix = Matrix([0 for _ in range(len(other.matrix[0]))])
        for i in range(len(self.matrix)):
            temp = [0] * len(other.matrix[0])
            for j in range(len(other.matrix[0])):
                value = 0
                for k in range(len(other.matrix)):
                    value += self.matrix[i][k] * other.matrix[k][j]
                temp[j] = value % (10**9+7)
            res_matrix.matrix[i] = temp
        return res_matrix

    def __pow__(self, exp):
        if exp == 1:
            return self
        elif exp % 2 == 0:
            temp = self ** (exp // 2)
            return temp * temp
        else:
            temp = self ** (exp // 2)
            return self * temp * temp

fib = Matrix([[1, 1], [1, 0]])
input = sys.stdin.readline
print((fib ** int(input())).matrix[0][1])