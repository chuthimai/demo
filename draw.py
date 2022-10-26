from matplotlib.pyplot import *
from numpy import *
from math import *
from cmath import *

n = linspace(0, 40, 40)
s = complex(-1/12, pi/6)
K = 2
x = []
for i in n:
    x.append(K*exp(s*i))

subplot(2, 1, 1)
stem(n, real(x))
title("Phan thuc")
axis([0, 40, -2, 2])

subplot(2, 1, 2)
stem(n, imag(x))
title("Phan ao")
axis([0, 40, -2, 2])
# show()
savefig("draw.png")