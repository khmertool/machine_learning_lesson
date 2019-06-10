#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 08:35:35 2019

@author: danhhong
"""
from sklearn import tree

#ប្រមូល និងរៀបចំទិន្នន័យ
features = [[1,4,3,7],
            [2,2,6,3],
            [1,2,6,3],
            [5,6,6,4],
            [1,6,6,7],
            [4,2,4,7],
            [5,2,2,7]]

label = [0,1,0,0,0,0,1]

#បង្រៀនម៉ាស៊ីន
mytree = tree.DecisionTreeClassifier()
train_data = mytree.fit(features,label)

#ព្យាករណ៍លទ្ធផល
input_data = [[1,6,4,3]]

result = train_data.predict(input_data)

print(result)
