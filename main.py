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
    genetic.layout([0,1,2,3,4,5,6,7,8,9])
    test.show_image()

main()
