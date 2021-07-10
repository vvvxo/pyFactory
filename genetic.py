# 随机打乱工序
import random
import matplotlib.pyplot as plt
import numpy as np
import setFactory as sF
import test

safe_distance = 1
imageName = 0


# 随机生成一道工序排布
def ran_process(length):
    tmp = np.arange(0, length, 1, list)
    random.shuffle(tmp)
    return tmp


# 根据设备序列生成设备位置
def layout(pro_series):
    tmpCoord = np.zeros((len(pro_series), 2), int)
    maxX = 0
    maxY = 0
    for i in range(0, len(pro_series)):
        numPro = pro_series[i]  # 工序的编号
        # 设定X轴
        # print("前", tmpCoord[numPro][0])
        if i == 0:
            tmpCoord[numPro][0] = sF.area[numPro][0] / 2 + safe_distance
        else:
            # 判断换行
            rightMaxX = sF.area[numPro][0] + tmpCoord[pro_series[i - 1]][0] + \
                sF.area[pro_series[i - 1]][0] / 2 + \
                safe_distance  # 最右边的X坐标 rightMaxX = 当前长+上一个坐标+上一个长/2+安全距离
            if (rightMaxX > sF.fX):
                # print("换行")
                tmpCoord[numPro][0] = sF.area[numPro][0] / 2 + safe_distance
            else:
                tmpCoord[numPro][0] = (sF.area[pro_series[i - 1]][0] + sF.area[numPro][0]) / 2 + \
                    tmpCoord[pro_series[i - 1]][0] + \
                    safe_distance  # 当前X坐标 = (上一个长+当前长)/2+上一个坐标+安全距离
        if tmpCoord[numPro][0] > maxX: ##获得最大X轴
            maxX = tmpCoord[numPro][0]

        # 设定Y轴
        # tmpCoord[numPro][1] = 0
        if i < 1:
            tmpCoord[numPro][1] = sF.area[numPro][1] / 2
        else:
            for j in range(0, i):
                # 判断x轴是否有交集，如果有，numPro的Y轴 = j的坐标+(numpro宽 + j宽)/2
                leftMax = max(
                    tmpCoord[pro_series[j]][0] - sF.area[pro_series[j]][0] / 2,
                    tmpCoord[numPro][0] - sF.area[numPro][0] / 2)
                rightMin = min(
                    tmpCoord[pro_series[j]][0] + sF.area[pro_series[j]][0] / 2,
                    tmpCoord[numPro][0] + sF.area[numPro][0] / 2)

                if (leftMax < rightMin):  # 如果有交集
                    # 当前坐标= 交集Y坐标+交集宽/2+当前Y/2+安全距离，缓存xtmpMaxCoordY，选择较高的tmpMaxCoordY
                    if tmpCoord[numPro][1] < tmpCoord[pro_series[j]][1] + (
                            sF.area[pro_series[j]][1] + sF.area[numPro][1]) / 2 + safe_distance:
                        tmpCoord[numPro][1] = tmpCoord[pro_series[j]][1] + \
                            (sF.area[pro_series[j]][1] +
                             sF.area[numPro][1]) / 2 + safe_distance
                else:
                    tmpCoord[numPro][1] = max(tmpCoord[numPro][1], sF.area[numPro][1] /
                                              2 + safe_distance)
                if tmpCoord[numPro][1] > maxY:
                    maxY = tmpCoord[numPro][1]
        print(sF.area[numPro], tmpCoord[numPro])
        test.add_rectangle(sF.area[numPro], tmpCoord[numPro])
    # print(tmpCoord)
    return tmpCoord,maxX*maxY


# 判断是否变异
def isChanged(chance):
    return bool(chance < random.random())


def calulateLayout(pro_series):
    # TODO
    return 1

# 计算总费用


def sumFre(layout):
    # 返回总费用
    tmpFree = 0
    for i in range(0, len(layout) - 1):
        tmpFree += (abs(layout[i][1] - layout[i+1][1]) + abs(layout[i][0] -
         layout[i+1][0])) * sF.traFre[i][i+1] * sF.traSpe[i][i+1]
    return tmpFree

#交换两个种群
def exchange(firstArray, secondArray):
    firstArray[7:13], secondArray[7:13] = secondArray[7:13], firstArray[7:13]
    tmpWhile = 1
    while tmpWhile == 1:
        tmpWhile = 0
        for i in range(0, len(firstArray)):
            for j in range(i+1, len(firstArray)):
                if firstArray[i] == firstArray[j]:
                    firstArray[i] += 1
                    if firstArray[i] > 19:# 防止数相加超过序列
                        firstArray[i] = 0
                    tmpWhile = 1    
