import random
import numpy as np

processLen = 10  # 设置工序长度

maxGen = 100  # 进化代数
popSize = 10
Pc = 0.01  # 变异率
Pm = 0.6  # 交叉概率

# 厂房长和宽
fX = 40
fY = 30
# 工位区域大小,[长,宽]
area = np.array([[3, 2], [4, 3], [4, 1],
                 [6, 4], [7, 4], [2, 4],
                 [4, 4], [2, 4], [4, 4],
                 [2, 4], [4, 4], [2, 4],
                 [4, 4], [2, 4], [4, 4],
                 [2, 4]])
# 存储相应工作的位置
coord = [[0, 0], [0, 0], [0, 0], [0, 0],
         [0, 0], [0, 0], [0, 0], [0, 0],
         [0, 0], [0, 0], [0, 0], [0, 0]]
# 物流频率
traFre = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# 物流费用
traSpe = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
