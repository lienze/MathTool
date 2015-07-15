__author__ = 'lienze'
# encoding=utf-8

from PyMathTool.LinearAlgebra import Determinant as Dt  # Dt = Determinant Test

'''
测试线性代数工具包中的行列式包
'''

def test_init():
    det1 = Dt.Det([1, 2, 3], [2, 3, 4, 5])
    # det1 = Dt.Det(5, True)
    det1.show_det()

def test_ir_mul_k_add_jr():
    det1 = Dt.Det([1, 2, 3], [2, 3, 4, 5])
    det1.ir_mul_k_add_jr(1, 2, 3)
    det1.show_det()

if __name__ == "__main__":

    # 测试行列式第i行*k加到第j行
    test_ir_mul_k_add_jr()

    # 测试行列式初始化
    # test_init()

    pass
