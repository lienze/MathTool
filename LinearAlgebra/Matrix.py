__author__ = 'lienze'



def matrix_add(matrix_0, matrix_1):
    result = matrix_0 + matrix_1
    return result




if __name__ == "__main__":
    a1 = [0, 0, 0, 0]
    a2 = [0, 0, 0, 0]
    a3 = [0, 0, 0, 0]
    a = [a1, a2, a3]

    b1 = [0, 0, 0, 0]
    b2 = [0, 0, 0, 0]
    b3 = [0, 0, 0, 0]
    b = [b1, b2, b3]

    result = matrix_add(a, b)

    print result