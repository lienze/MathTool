__author__ = 'lienze'
# encoding=utf-8

from LinearAlgebra import Matrix as Mt  # Mt = Matrix Test

'''
测试线性代数工具包中的矩阵包
'''

def test_plus():
    mat = Mt.Matrix(5)
    # mat.show_mat()
    mat1 = Mt.Matrix(5)
    mat_r = mat + mat1
    if not isinstance(mat_r, int):
        mat_r.show_mat()
    else:
        print 'errno:', mat_r

def test_convert_t():
    mat1 = Mt.Matrix(5)
    # mat1.show_mat()
    mat1.set_ij(1, 2, 3)
    mat2 = mat1.convert_t()
    mat2.show_mat()

if __name__ == "__main__":

    # 测试矩阵加法
    # test_plus()

    # 测试矩阵转置
    test_convert_t()

