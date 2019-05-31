import matplotlib.pyplot as plt
import numpy as np

x = [2, 7]
y = [6, 9]

plt.plot(x, y)
plt.show()

x = [2, 7, 5]
y = [6, 9, 4]

plt.plot(x, y)
plt.show()

image = np.random.rand(50,50)

plt.imshow(image)
plt.show()