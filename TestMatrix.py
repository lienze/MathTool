__author__ = 'lienze'
# encoding=utf-8

from LinearAlgebra import Matrix as M

'''
测试线性代数工具包中的矩阵包
'''

def test_plus():
    mat = M.Matrix(5)
    # mat.show_mat()
    mat1 = M.Matrix(4)
    mat_r = mat + mat1
    if not isinstance(mat_r, int):
        mat_r.show_mat()
    else:
        print 'errno:', mat_r

if __name__ == "__main__":

    # 测试矩阵加法
    test_plus()