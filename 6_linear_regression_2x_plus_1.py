"""
សមីការ y = 2x + 1
m = 2, b = 1
x | y
--|--
1 | 3
2 | 5
3 | 7
6 | ?
"""
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([[1], [2], [3]])
y = np.array([[3], [5], [7]])

model = LinearRegression()
my_model = model.fit(x,y)

result = my_model.predict([[6]])
print(result)

# គូរបន្ទាត់
plt.scatter(x, y, marker="s")
plt.plot(x, y)
plt.show()