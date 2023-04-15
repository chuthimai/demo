import matplotlib.pyplot as plt
import math
import numpy as np
import time

file_object = open('input.txt')
n = int(file_object.readline())
data = file_object.read().split("\n")
d = 3
mau = ['black', 'blue', 'yellow', 'navy', 'red', 'purple']
x = []
y = []

for i in range(n):
    x.append(int(data[i].split(" ")[0]))
    y.append(int(data[i].split(" ")[1]))
    plt.plot(x[i], y[i], color='green', marker='.')
file_object.close()

plt.scatter(x, y, s=300, edgecolors="black")
for i, txt in enumerate(range(len(x))):
    plt.annotate(txt, (x[i], y[i]))


def kc(a, b, c, d):
    x = a - c
    y = b - d
    kq = ((x * x) + (y * y))
    return kq


visit = np.zeros(n)  # tập các đỉnh
A = np.zeros((n, n))  # ma trận kề
for i in range(n):
    for j in range(i + 1, n):
        if (kc(x[i], y[i], x[j], y[j]) <= d * d):
            xx = [x[i], x[j]]
            yy = [y[i], y[j]]
            plt.plot(xx, yy, color='green')
            A[i, j] = 1
            A[j, i] = 1
lt = []


def dfs(u):
    lt.append(u)
    visit[u] = 1
    for i in range(n):
        if A[u][i] == 1 and visit[i] == 0:
            dfs(i)


cnt = 0
for i in range(n):
    if visit[i] == 0:
        lt.clear()
        dfs(i)
        for ii in range(len(lt)):
            for jj in range(ii + 1, len(lt)):
                if A[lt[ii], lt[jj]] == 1:
                    x1 = [x[lt[ii]], x[lt[jj]]]
                    y1 = [y[lt[ii]], y[lt[jj]]]
                    plt.plot(x1, y1, color=mau[cnt])

        if len(lt) == 1:
            plt.plot(x[lt[0]], y[lt[0]], color=mau[cnt], marker='.')
        cnt = cnt + 1
plt.legend()
plt.show()



