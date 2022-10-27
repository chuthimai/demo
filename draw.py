from matplotlib.pyplot import *
from numpy import *
from cmath import *
from scipy import signal # xu ly tin hieu co sawtooth va square

A = 3
L = 100
N = 15
Fs = 20
DRX = 60
Ts = 1/Fs
t = linspace(0, L, L)

subplot(2,1,1)
x1 = A*signal.sawtooth(2*pi*t/N)
stem(t, x1)
xlabel("Thoi gian (s)")
ylabel("Bien do")
title("Day xung rang cua")

subplot(2,1,2)
x2 = A*signal.square(2*pi*t/N, DRX/L)
stem(t, x2)
xlabel("Thoi gian (s)")
ylabel("Bien do")
title("Day xung vuong")
savefig("draw.png")