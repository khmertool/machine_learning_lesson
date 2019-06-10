import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

fields = ['sepal.length', 'sepal.width', 
          'petal.length', 'petal.width', 
          'variety']
data_frame = pd.read_csv("data/iris.csv", 
                         skipinitialspace=True, 
                         usecols=fields)

# បំបែក data frame ទៅជា data & label
features = data_frame[['sepal.length', 'sepal.width', 
                       'petal.length', 'petal.width']]
label = data_frame[['variety']]

data_array = np.asarray(features)   # បំលែងទៅ numpy array
label_array = np.asarray(label)     # បំលែងទៅ numpy array

# បង្រៀនម៉ាស៊ីន
model = DecisionTreeClassifier()
my_model = model.fit(data_array, label_array)

# ព្យាករណ៍
x_new_iris = np.array([[1.7, 4.0, 5.3, 6.0]]) # ផ្កាថ្មី
result = my_model.predict(x_new_iris)
print(result)
