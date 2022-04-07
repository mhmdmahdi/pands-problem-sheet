import numpy as np
import matplotlib.pyplot as plt
# Had to use pip3 install numpy as I have multiple different versions of python running (https://www.pythonpool.com/no-module-named-numpy-solved/)
# matplotlib installed using ref (https://matplotlib.org/stable/users/installing/index.html)

x = np.array(range(0, 4))
fx = np.array(range(0, 4))
gx = x**2
hx = x**3

plt.plot(x, fx, label="f(x)", color="red")
plt.plot(x, gx, label="g(x)", color="green")
plt.plot(x, hx, label="h(x)", color="blue")
plt.xlim([0, 4])
plt.ylim([0, 30])
# x and y axis ranges reference from (https://stackabuse.com/how-to-set-axis-range-xlim-ylim-in-matplotlib/)
plt.legend()
plt.show()