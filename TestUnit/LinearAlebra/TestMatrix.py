__author__ = 'lienze'
# encoding=utf-8

from PyMathTool.LinearAlgebra import Matrix as Mt  # Mt = Matrix Test

'''
测试线性代数工具包中的矩阵包
'''

def test_plus():
    mat = Mt.Mat(5)
    # mat.show_mat()
    mat1 = Mt.Mat(5)
    mat_r = mat + mat1
    if type(mat_r) is not int:
        mat_r.show_mat()
    else:
        print 'errno:', mat_r

def test_convert_t():
    mat1 = Mt.Mat(5)
    # mat1.show_mat()
    mat1.set_ij(1, 2, 3)
    mat2 = mat1.convert_t()
    mat2.show_mat()

def test_mul():
    mat1 = Mt.Mat(5, True)
    for x in xrange(1, 6):
        mat1.set_ij(1, x, x)
    mat1.show_mat()
    mat2 = Mt.Mat(5, True)
    for x in xrange(1, 6):
        mat2.set_ij(x, 1, x)
    # mat2.show_mat()
    mat3 = mat1 * 3
    mat3.show_mat()

def test_ir_mul_k():
    mat1 = Mt.Mat(5, True)
    for x in xrange(1, 6):
        mat1.set_ij(1, x, x)
    mat1.show_mat()
    print ''
    mat1.ir_mul_k(1, 2)
    mat1.show_mat()

def test_init():
    mat1 = Mt.Mat([1, 2, 3], [2, 3, 4, 5])
    mat1.show_mat()

def test_jc_mul_k():
    mat1 = Mt.Mat(5, True)
    mat1.show_mat()

    for x in xrange(1, 6):
        mat1.set_ij(1, x, x)
    mat1.show_mat()
    mat1.jc_mul_k(2, 4)
    mat1.show_mat()

def test_get_rank():
    mat1 = Mt.Mat(5)
    mat1.show_mat()
    print mat1.get_rank()

if __name__ == "__main__":

    # 测试计算矩阵的秩
    test_get_rank()

    # 测试矩阵第j行乘以k
    # test_jc_mul_k()

    # 测试不定参数初始化矩阵
    # test_init()

    # 测试矩阵加法
    # test_plus()

    # 测试矩阵转置
    # test_convert_t()

    # 测试矩阵乘法
    # test_mul()

    # 测试矩阵第i行乘以k
    # test_ir_mul_k()
    pass

