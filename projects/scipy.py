import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1])

cs = CubicSpline(x, y)

x_fine = np.linspace(0, 5, 100)
y_fine = cs(x_fine)

plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x_fine, y_fine, label='Cubic Spline', color='blue')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Spline Interpolation')
plt.grid(True)
plt.show()
