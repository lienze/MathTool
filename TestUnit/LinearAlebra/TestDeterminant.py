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

if __name__ == "__main__":

    # 测试行列式初始化
    test_init()

    pass
