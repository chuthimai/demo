from matplotlib.pyplot import *
from numpy import *

x = linspace(-10, 20, 30)
y = []
for i in x:
    if i<0:
        y.append(0)
    else:
        y.append(0.2*1.5**i)

axis([-10, 21, -0.5, 1000])

stem(x, y)
# show()
savefig("draw.png")