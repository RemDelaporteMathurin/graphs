import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, num=200)
center = 0.5
width = 0.05
distribution = 1/(width*(2*3.14)**0.5) * np.exp(-0.5*((x-center)/width)**2)

plt.plot(x, distribution)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.xticks([], [])
plt.yticks([], [])
plt.savefig("gaussian.svg", transparent=True)