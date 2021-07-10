import numpy as np
import test
import genetic
import matplotlib as mpl
import matplotlib.pyplot as plt
import setFactory as sF
import random

# 生成物流频率表
sF.createFre(sF.traSpe)


# greatPop = np.zeros(sF.processLen)
# greatPopIndex = 0
# secodPop = np.zeros(sF.processLen)
# secodPopIndex = 0

# 生成初始种群
# size种群大小,length是长度
def create(size, length):
    tmp = np.zeros((size, length), int)
    for i in range(0, size):
        tmp[i] = genetic.ran_process(length)
    return tmp


def main():
    matplotY = np.zeros(100)
    matplotX = np.zeros(100)
    initPop = create(30, 20)
    # print(initPop)
    for p in range(0, sF.maxGen):
        # print(initPop)
        # 开始循环单个种群
        popC = np.zeros(len(initPop))  # 种群对应总费用存储数组
        for i in range(0, len(initPop)):
            genetic.imageName = i
            tmpLayout, area = genetic.layout(initPop[i])
            popC[i] = genetic.sumFre(tmpLayout) * (area/80)

        # 计算适应度函数
        popFc = suitFuncgionn(popC)
        # 归一化
        popNormalization = popFc / np.sum(popFc)

        tmpG, tmpGI, tmpS, tmpSI = copyGreatPop(popNormalization, initPop)
        chooser = random.random()
        for i in range(0, len(popNormalization)):
            if np.sum(popNormalization[0:i + 1]) > chooser:
                initPop[i] = genetic.ran_process(sF.processLen)  # 被选中的种群
                break  # 轮盘赌结束
        # 变异
        if genetic.isChanged(sF.Pc):
            tmp1 = random.randint(0, sF.processLen - 1)
            tmp2 = random.randint(0, sF.processLen - 1)
            initPop[random.randint(
                0, 29)][tmp1] = initPop[random.randint(0, 29)][tmp2]

        # 交叉
        if genetic.isChanged(sF.Pm):
            tmp1 = random.randint(0, len(initPop) - 1)
            tmp2 = random.randint(0, len(initPop) - 1)
            genetic.exchange(initPop[tmp1], initPop[tmp2])

        initPop[tmpGI] = tmpG
        initPop[tmpSI] = tmpS
        print(tmpG,end=',')
        print(popFc[tmpGI])
        # 画图
        matplotY[p] = np.min(popC)
        matplotX[p] = p
    
    
    plt.figure()
    plt.plot(matplotX,matplotY)
    plt.show()


# 选出最好的两个种群，并且保存至全局变量greatPop和secondPop
def copyGreatPop(popNormal, population):
    tmpList = np.sort(popNormal)
    greatPopF = tmpList[len(popNormal) - 1]
    secodPopF = tmpList[len(popNormal) - 2]
    greatPopIndex = np.where(popNormal == greatPopF)
    secodPopIndex = np.where(popNormal == secodPopF)
    greatPop = population[greatPopIndex]
    secodPop = population[secodPopIndex]
    return greatPop, greatPopIndex, secodPop, secodPopIndex


def suitFuncgionn(popFree):
    tmArray = np.zeros(len(popFree))
    for i in range(0, len(popFree)):
        tmArray[i] = 1 / (popFree[i] / 100000 )
    return tmArray


main()
