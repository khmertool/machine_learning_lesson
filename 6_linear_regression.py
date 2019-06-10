import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#dataset
features = np.array([[40.3], [38.2], [44.9], [31.0]])
label = np.array([[30.0], [28.5], [32.2], [18.2]])

# មើលទិន្នន័យ
plt.scatter(features, label, marker="s")
plt.plot(features, label)
plt.show()

# បង្រៀនម៉ាស៊ីនតាម y = mx + b: រួចស្វែងរកតម្លៃ m និង b
model = LinearRegression()
my_model = model.fit(features, label)

# ព្យាករណ៍
result = my_model.predict([[60.2]])

print(result)
