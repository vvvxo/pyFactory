import numpy as np
import test
import genetic
import setFactory


# 生成初始种群
# size是行号,length是长度
def create(size, length):
    tmp = np.zeros((size, length))
    for i in range(0, size):
        tmp[i] = genetic.ran_process(length)
    print(tmp)


def main():
    genetic.layout([3, 7, 9, 3, 2, 1, 5, 4,6,8])
    test.show_image()

main()
