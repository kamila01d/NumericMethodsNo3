import numpy as np
import matplotlib.pyplot as plt
N = 1000
h = 0.01
y = np.zeros(N, dtype=np.float64)
y[0] = 1
y[1] = (1/(-6 + h*h))*(-4*y[0])

for i in range(1, N-1):
    y[i+1] = -y[i]*h**2 -y[i-1] + 2*y[i]

for i in range(0,N):
    print(y[i])

plt.plot(y)
plt.show()













