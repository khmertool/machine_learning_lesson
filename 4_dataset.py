from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# ទាញយកទិន្នន័យដែលរៀបចំហើយ
iris_dataset = load_iris()

# បំបែកទិន្នន័យ 70% សម្រាប់បង្រៀនម៉ាស៊ីន 30% សម្រាប់ពិសោធន៍
x_train, x_test, y_train, y_test = train_test_split(iris_dataset.data, iris_dataset.target, random_state=0)

# បង្រៀនម៉ាស៊ីន
model = DecisionTreeClassifier()
my_model = model.fit(x_train, y_train)

# ព្យាករណ៍
result = my_model.predict(x_test)
print(result)

# មានផ្កាថ្មី
x_new_iris = np.array([[1.7, 4.0, 5.3, 6.0]])
new_result = my_model.predict(x_new_iris)
print(new_result)

# វាយតម្លៃ
rate = my_model.score(x_test, y_test)
print(rate)