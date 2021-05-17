# 随机打乱工序
import random
import numpy as np
import setFactory
import test


def ran_process(length):
    tmp = np.arange(1, length + 1, 1, list)
    random.shuffle(tmp)
    return tmp


# 根据设备序列生成设备位置
def layout(pro_series):
    front_x = 0
    front_y = 0
    for i in range(0, len(pro_series)):
        numPro = pro_series[i]  # 工序的编号
        print("工序", pro_series[i])
        # 设定X轴
        # print("前", setFactory.coord[numPro][0])
        if front_x == 0:
            setFactory.coord[numPro][0] = setFactory.area[numPro][0] / 2 + 1
            front_x = setFactory.coord[numPro][0]
        else:
            # 判断换行

            # a = setFactory.area[numPro][0]
            # b = setFactory.coord[pro_series[i - 1]][0]
            # c = setFactory.area[pro_series[i - 1]][0] / 2
            # d = setFactory.fX
            # if (a + b + c > d):
            #     setFactory.coord[numPro][0] = setFactory.area[numPro][0] / 2 + 1
            #     front_x = 0

            if (((setFactory.area[numPro][0] + setFactory.coord[pro_series[i - 1]][0] +
                  setFactory.area[pro_series[i - 1]][0] / 2)) > setFactory.fX):
                print("换行")
                setFactory.coord[numPro][0] = setFactory.area[numPro][0] / 2 + 1
                front_x = 0
            else:
                setFactory.coord[numPro][0] = setFactory.area[pro_series[i - 1]
                                                              ][0] / 2 + front_x
                front_x = setFactory.coord[numPro][0]
        print("后", front_x, setFactory.coord[numPro][0])

        # 设定Y轴
        setFactory.coord[numPro][1] = 0
        if i == 0:
            setFactory.coord[numPro][1] = setFactory.area[numPro][1] / 2
        else:
            for j in range(0, i - 1):
                # 判断x轴是否有交集，如果有，numPro的Y轴 = j的坐标+(numpro宽 + j宽)/2
                testMax = max(
                    setFactory.coord[pro_series[j]][0] -
                    setFactory.area[pro_series[j]][0] / 2,
                    setFactory.coord[numPro][0] - setFactory.area[numPro][0] / 2)
                testMin = min(
                    setFactory.coord[pro_series[j]][0] + (
                        setFactory.area[pro_series[j]][0] / 2),
                    setFactory.coord[numPro][0] + (
                        setFactory.area[numPro][0]))
                tmpMaxCoordY = setFactory.coord[numPro][0]
                if (testMax < testMin):  # 如果有交集
                    setFactory.coord[numPro][1] = setFactory.coord[pro_series[j]][1] + (
                        setFactory.area[pro_series[j]][1] + setFactory.area[numPro][1]) / 2
                else:
                    setFactory.coord[numPro][1] = setFactory.area[numPro][1] / 2

                # 选择较高的Y坐标
                if setFactory.coord[numPro][0] > tmpMaxCoordY:
                    tmpMaxCoordY = setFactory.coord[numPro][0]
                else:
                    setFactory.coord[numPro][0] = tmpMaxCoordY

        test.add_rectangle(setFactory.area[numPro], setFactory.coord[numPro])

        # print(setFactory.coord[numPro])

    # 判断是否变异
    def isChanged(chance):
        return bool(chance < random.random())
