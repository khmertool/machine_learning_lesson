import numpy as np

# array ធម្មតា
data = [[1,4,3,7],
        [2,2,6,3],
        [1,2,6,3],
        [5,6,6,4],
        [1,6,6,7],
        [4,2,4,7],
        [5,2,2,7]]
# numpy array
np_array = np.array([[1,4,3,7],
                    [2,2,6,3],
                    [1,2,6,3],
                    [5,6,6,4],
                    [1,6,6,7],
                    [4,2,4,7],
                    [5,2,2,7]])
print(np_array.ndim) # ចំនួន dimension 2

print(np_array.shape) #ចំនួន row និង column (7, 4)

print(len(np_array)) # ទំហំ array 7

print(np_array[0]) # [1 4 3 7]

print(np_array[0][:2]) # [1 4]