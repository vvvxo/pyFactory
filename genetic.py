# 随机打乱工序
import random
import numpy as np
import setFactory as sF
import test

safe_distance = 1


def ran_process(length):
    tmp = np.arange(1, length + 1, 1, list)
    random.shuffle(tmp)
    return tmp


# 根据设备序列生成设备位置
def layout(pro_series):
    for i in range(0, len(pro_series)-1):
        numPro = pro_series[i]  # 工序的编号
        # 设定X轴
        # print("前", sF.coord[numPro][0])
        if i == 0:
            sF.coord[numPro][0] = sF.area[numPro][0] / 2 + safe_distance
        else:
            # 判断换行
            rightMaxX = sF.area[numPro][0] + sF.coord[pro_series[i - 1]][0] + \
                sF.area[pro_series[i - 1]][0] / 2 + safe_distance # 最右边的X坐标 rightMaxX = 当前长+上一个坐标+上一个长/2+安全距离
            if (rightMaxX > sF.fX):
                print("换行")
                sF.coord[numPro][0] = sF.area[numPro][0] / 2 + safe_distance
            else:
                sF.coord[numPro][0] = (sF.area[pro_series[i - 1]][0]+sF.area[numPro][0])/2 + \
                    sF.coord[pro_series[i - 1]][0] + \
                    safe_distance  # 当前X坐标 = (上一个长+当前长)/2+上一个坐标+安全距离

        # 设定Y轴
        # sF.coord[numPro][1] = 0
        if i < 1:
            sF.coord[numPro][1] = sF.area[numPro][1] / 2
        else:
            for j in range(0, i):
                # 判断x轴是否有交集，如果有，numPro的Y轴 = j的坐标+(numpro宽 + j宽)/2
                leftMax = max(
                    sF.coord[pro_series[j]][0] - sF.area[pro_series[j]][0] / 2,
                    sF.coord[numPro][0] - sF.area[numPro][0] / 2)
                rightMin = min(
                    sF.coord[pro_series[j]][0] + sF.area[pro_series[j]][0] / 2,
                    sF.coord[numPro][0] + sF.area[numPro][0]/2)

                if (leftMax < rightMin):  # 如果有交集
                    # 应改写成当前坐标= 交集Y坐标+交集宽/2+当前Y/2+安全距离，缓存xtmpMaxCoordY，选择较高的tmpMaxCoordY
                    # 不用缓存，可以直接判断，如果大于，就更新当前Y坐标，如果否，就不更新
                    # sF.coord[numPro][1] = sF.coord[pro_series[j]][1] + (
                    #     sF.area[pro_series[j]][1] + sF.area[numPro][1]) / 2 + safe_distance
                    if sF.coord[numPro][1] < sF.coord[pro_series[j]][1]+(sF.area[pro_series[j]][1]+sF.area[numPro][1])/2+safe_distance:
                        sF.coord[numPro][1] = sF.coord[pro_series[j]][1] + \
                            (sF.area[pro_series[j]][1] +
                             sF.area[numPro][1])/2+safe_distance
                else:
                    sF.coord[numPro][1] = max( sF.coord[numPro][1],sF.area[numPro][1] / \
                        2 + safe_distance)

        test.add_rectangle(sF.area[numPro], sF.coord[numPro])

        # print(sF.coord[numPro])

    # 判断是否变异
    def isChanged(chance):
        return bool(chance < random.random())
