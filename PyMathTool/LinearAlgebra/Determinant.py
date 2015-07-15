__author__ = 'lienze'
# encoding=utf-8

'''
行列式类
'''

class Det:
    def __init__(self, *args):
        self.n = 0  # n阶行列式
        self.det = []
        self.val = 0    # n阶行列式的值
        tmp_args_len = len(args)

        if tmp_args_len == 1:
            if type(args[0]) is int:
                self.init1(args[0])
        elif tmp_args_len == 2:
            if type(args[0]) is int and type(args[1]) is bool:
                self.init1(args[0], args[1])
            elif type(args[0]) is list and type(args[1]) is list:
                self.init0(args)
        else:
            self.init0(args)

    def init0(self, args):
        # 首先检查类型
        count = 0
        max_list_len = 0
        for x in xrange(0, len(args)):
            # print args[x]
            if type(args[x]) is list:
                count += 1
                if max_list_len < len(args[x]):
                    max_list_len = len(args[x])
            else:
                break

        if count == len(args):
            # 全部为list类型
            for i in args:
                # list基本单元先对齐
                if len(i) < max_list_len:
                    '''c = max_list_len - len(i)
                    while c > 0:
                        i.append(0)
                        c -= 1'''
                    i.extend([0 for _ in xrange(1, max_list_len - len(i) + 1)])
                # 之后再添加
                self.det.append(i)

            # 添加未填充的行
            if count < max_list_len:
                for _ in xrange(1, max_list_len - count + 1):
                    self.det.append([0 for _ in xrange(1, max_list_len + 1)])
                self.n = max_list_len
            else:
                self.n = count

        else:
            print u'初始化错误，list数量', count, u'参数数量', len(args)

    # 初始化为n阶单位矩阵或矩阵
    def init1(self, n, b_zero=False):
        for j in xrange(1, n + 1):
            xl = []
            for i in xrange(1, n + 1):
                if i == j and not b_zero:
                    xl.append(1)
                else:
                    xl.append(0)
            self.det.append(xl)
        self.n = n

    # 计算行列式的值
    def calc_det(self):
        pass

    # 显示行列式
    def show_det(self):
        print ''
        for m in self.det:
            print '|',
            for c in m:
                print c,
            print '|'

    # 显示行列式的值
    def show_val(self):
        print self.val

    '''
    功能：行列式的第i行乘以k加到第j行
    参数：i:第i行，k：系数，j：第j行
    返回值：处理之后的行列式
    PS：第ir(row)行mul(乘)k加到jr(row)
    '''
    def ir_mul_k_add_jr(self, i, k, j):
        if i and j and i <= len(self.det) and j <= len(self.det):
            for x in xrange(0, len(self.det[0])):
                self.det[j-1][x] = self.det[i-1][x] * k
        return self
