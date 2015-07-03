__author__ = 'lienze'
# encoding=utf-8


# 实现了两个矩阵相加的功能
def matrix_add(matrix_a, matrix_b):

    # 确保两个矩阵的行数相同
    if len(matrix_a) != len(matrix_b):
        return -1

    # 接下来确保矩阵的列数相同
    na = []
    for la in matrix_a:
        if len(la) not in na:
            na.append(len(la))
    # print na

    nb = []
    for lb in matrix_b:
        if len(lb) not in nb:
            nb.append(len(lb))
    # print nb

    if len(na) != len(nb):
        if len(na) != 1 and len(nb) != 1:
            return -2

    # 之后进行两矩阵相加
    result = [[x0 + y0 for x0, y0 in zip(x, y)] for x, y in zip(matrix_a, matrix_b)]
    return result


if __name__ == "__main__":

    '''
    # 测试matrix_add函数代码
    a1 = [4, 3, 2, 1]
    a2 = [0, 0, 0, 0]
    a3 = [0, 0, 0, 0]
    a = [a1, a2, a3]
    b1 = [1, 2, 3, 4]
    b2 = [0, 0, 0, 0]
    b3 = [0, 0, 0, 0]
    b = [b1, b2, b3]
    res = matrix_add(a, b)
    print res
    '''
    exit(0)
