from matplotlib.pyplot import *
from numpy import *

n = linspace(0, 20, 20)
h1 = ones(20)
h2 = []
for i in range(20):
    if i<10:
        h2.append(0)
    else:
        h2.append(1)
xticks(range(0,21))
yticks([0,1,2])
h = h1 * h2
stem(n, h)

savefig("draw.png")