print("Hello World")

def solution(A):
    return len(set(A))

A = [2, 1, 1, 2, 3, 1]
print(solution(A)) # 3


import numpy as np
import matplotlib.pyplot as plt
# 生成数据
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
# 绘制图形
plt.plot(x, y)
# 显示图形
plt.show()
