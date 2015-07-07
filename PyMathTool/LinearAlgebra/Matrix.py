__author__ = 'lienze'
# encoding=utf-8


'''
功能：两个矩阵相加
参数：matrix_a:矩阵A matrix_b:矩阵B
返回值：相加后的矩阵(list)
'''
def add_matrix(matrix_a, matrix_b):

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


'''
功能：生成零矩阵
参数：m：矩阵的行数，n：矩阵的列数
返回值：零矩阵(m行n列)
'''
def gen_zero_matrix(m, n):
    result = []
    for j in xrange(1, m + 1):
        xl = []
        for i in xrange(1, n + 1):
            xl.append(0)
        result.append(xl)
    return result


'''
功能：生成n阶单位矩阵E
参数：n：矩阵的列数
返回值：单位矩阵E
'''
def gen_e_matrix(n):
    result = []
    for j in xrange(1, n + 1):
        xl = []
        for i in xrange(1, n + 1):
            if i == j:
                xl.append(1)
            else:
                xl.append(0)
        result.append(xl)
    return result


'''
功能：控制台打印矩阵
参数：mat:矩阵变量
返回值：无
'''
def show_matrix(mat):
    for m in mat:
        print m


'''
功能：获取矩阵行数与列数
参数：mat：矩阵变量
返回值：[m, n] list类型
'''
def get_matrix_mn(mat):
    m = len(mat)
    n = len(mat[0])
    return [m, n]


'''
功能：矩阵转置
参数：mat：矩阵变量
返回值：转置后的矩阵
'''
def convert_matrix(mat):
    f_matrix = gen_zero_matrix(len(mat[0]), len(mat))

    for j in xrange(1, len(mat)+1):
        for i in xrange(1, len(mat[0])+1):
            set_matrix_ij(f_matrix, i, j, get_matrix_ij(mat, j, i))
    # show_matrix(f_matrix)
    return f_matrix

'''
功能：设置矩阵ij位置的值
参数：i：矩阵中的行，j：矩阵中的列，x:值
返回值：成功True或失败False
'''
def set_matrix_ij(self, i, j, x):
    self[i-1][j-1] = x
    return True


'''
功能：获取矩阵ij位置的值
参数：i：矩阵中的行，j：矩阵中的列
返回值：返回ij位置的值
'''
def get_matrix_ij(self, i, j):
    return self[i-1][j-1]


'''
以下使用class定义矩阵
'''
class Matrix:
    def __init__(self):
        self.m = 0  # m行
        self.n = 0  # n列
        self.mat = []

    # 初始化为m*n矩阵
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.mat = []
        for j in xrange(1, m + 1):
            xl = []
            for i in xrange(1, n + 1):
                xl.append(0)
            self.mat.append(xl)

    # 初始化为n阶单位矩阵或矩阵
    def __init__(self, n, b_zero=False):
        self.mat = []
        for j in xrange(1, n + 1):
            xl = []
            for i in xrange(1, n + 1):
                if i == j and not b_zero:
                    xl.append(1)
                else:
                    xl.append(0)
            self.mat.append(xl)

    # 显示矩阵
    def show_mat(self):
        for m in self.mat:
            print m

    '''
    功能：两个矩阵相加
    参数：matrix_a:矩阵A matrix_b:矩阵B
    返回值：相加后的矩阵(list)
    '''
    def __add__(self, other):
        matrix_a = self.mat
        matrix_b = other.mat
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
        self.mat = [[x0 + y0 for x0, y0 in zip(x, y)] for x, y in zip(matrix_a, matrix_b)]
        return self

    '''
    功能：获取矩阵行数与列数
    参数：无
    返回值：[m, n] list类型
    '''
    def get_mn(self):
        m = len(self.mat)
        n = len(self.mat[0])
        return [m, n]

    '''
    功能：设置矩阵ij位置的值
    参数：i：矩阵中的行，j：矩阵中的列，x:值
    返回值：成功True或失败False
    '''
    def set_ij(self, i, j, x):
        self.mat[i-1][j-1] = x
        return True

    '''
    功能：获取矩阵ij位置的值
    参数：i：矩阵中的行，j：矩阵中的列
    返回值：返回ij位置的值
    '''
    def get_ij(self, i, j):
        return self.mat[i-1][j-1]

    '''
    功能：矩阵转置
    参数：无
    返回值：转置后的矩阵
    '''
    def convert_t(self):
        f_matrix = Matrix(len(self.mat[0]), len(self.mat))
        for j in xrange(1, len(self.mat)+1):
            for i in xrange(1, len(self.mat[0])+1):
                f_matrix.set_ij(i, j, self.get_ij(j, i))
        return f_matrix


if __name__ == "__main__":

    '''
    # 测试add_matrix函数代码
    a1 = [4, 3, 2, 1]
    a2 = [0, 0, 0, 0]
    a3 = [0, 0, 0, 0]
    a = [a1, a2, a3]
    b1 = [1, 2, 3, 4]
    b2 = [0, 0, 0, 0]
    b3 = [0, 0, 0, 0]
    b = [b1, b2, b3]
    res = add_matrix(a, b)
    print res
    '''

    '''
    测试生成零矩阵
    gen_zero_matrix(4, 5)
    '''

    '''
    测试生成单位矩阵
    gen_e_matrix(5)
    '''

    '''
    测试显示矩阵
    show_matrix(gen_e_matrix(5))
    '''

    '''
    测试获取矩阵行数列数
    x, y =get_matrix_mn(gen_zero_matrix(5, 4))
    print x
    print y
    '''

    '''
    测试矩阵转置函数
    a1 = [4, 3, 2, 1]
    a2 = [4, 13, 12, 11]
    a3 = [5, 23, 22, 21]
    a = [a1, a2, a3]
    convert_matrix(a)
    '''

    exit(0)
