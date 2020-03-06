#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:20:48 2020

@author: rangeet
"""

from utils.mnistutil import MNISTUitl
from utils.sliceutil import Slice
from keras.models import load_model
import numpy as np
def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union
#In[]Module Load
model=load_model('mnist.h5')
module0=load_model('module0.h5')
module1=load_model('module1.h5')
module2=load_model('module2.h5')
module3=load_model('module3.h5')
module4=load_model('module4.h5')
module5=load_model('module5.h5')
module6=load_model('module6.h5')
module7=load_model('module7.h5')
module8=load_model('module8.h5')
module9=load_model('module9.h5')
#In[]: Module List
w1,b1 = model.layers[1].get_weights()
w2,b2 = model.layers[2].get_weights()
w1a=w1.flatten()
w2a=w2.flatten()
w1a=np.array(w1a)
w2a=np.array(w2a)
w_model=np.concatenate((w1a,w2a))
#In[]: List formation
w1,b1 = module0.layers[1].get_weights()
w2,b2 = module0.layers[2].get_weights()
w1a=w1.flatten()
w2a=w2.flatten()
w1a=np.array(w1a)
w2a=np.array(w2a)
w_module0=np.concatenate((w1a,w2a))
#In[]: List formation
w1,b1 = module1.layers[1].get_weights()
w2,b2 = module1.layers[2].get_weights()
w1a=w1.flatten()
w2a=w2.flatten()
w1a=np.array(w1a)
w2a=np.array(w2a)
w_module1=np.concatenate((w1a,w2a))
#In[]: List formation
w1,b1 = module2.layers[1].get_weights()
w2,b2 = module2.layers[2].get_weights()
w1a=w1.flatten()
w2a=w2.flatten()
w1a=np.array(w1a)
w2a=np.array(w2a)
w_module2=np.concatenate((w1a,w2a))

w1,b1 = module3.layers[1].get_weights()
w2,b2 = module3.layers[2].get_weights()
w1a=w1.flatten()
w2a=w2.flatten()
w1a=np.array(w1a)
w2a=np.array(w2a)
w_module3=np.concatenate((w1a,w2a))

w1,b1 = module4.layers[1].get_weights()
w2,b2 = module4.layers[2].get_weights()
w1a=w1.flatten()
w2a=w2.flatten()
w1a=np.array(w1a)
w2a=np.array(w2a)
w_module4=np.concatenate((w1a,w2a))

w1,b1 = module5.layers[1].get_weights()
w2,b2 = module5.layers[2].get_weights()
w1a=w1.flatten()
w2a=w2.flatten()
w1a=np.array(w1a)
w2a=np.array(w2a)
w_module5=np.concatenate((w1a,w2a))

w1,b1 = module6.layers[1].get_weights()
w2,b2 = module6.layers[2].get_weights()
w1a=w1.flatten()
w2a=w2.flatten()
w1a=np.array(w1a)
w2a=np.array(w2a)
w_module6=np.concatenate((w1a,w2a))

w1,b1 = module7.layers[1].get_weights()
w2,b2 = module7.layers[2].get_weights()
w1a=w1.flatten()
w2a=w2.flatten()
w1a=np.array(w1a)
w2a=np.array(w2a)
w_module7=np.concatenate((w1a,w2a))

w1,b1 = module8.layers[1].get_weights()
w2,b2 = module8.layers[2].get_weights()
w1a=w1.flatten()
w2a=w2.flatten()
w1a=np.array(w1a)
w2a=np.array(w2a)
w_module8=np.concatenate((w1a,w2a))

w1,b1 = module9.layers[1].get_weights()
w2,b2 = module9.layers[2].get_weights()
w1a=w1.flatten()
w2a=w2.flatten()
w1a=np.array(w1a)
w2a=np.array(w2a)
w_module9=np.concatenate((w1a,w2a))
#In[]: Jaccard similarities
w_append=[]
w_append.append(w_module0)
w_append.append(w_module1)
w_append.append(w_module2)
w_append.append(w_module3)
w_append.append(w_module4)
w_append.append(w_module5)
w_append.append(w_module6)
w_append.append(w_module7)
w_append.append(w_module8)
w_append.append(w_module9)
index=[0,1,2,3,4,5,6,7,8,9]
index1=[0,1,2,3,4,5,6,7,8,9]
jaccard_index=[]
for i in index:
        temp=jaccard_similarity(w_model,w_append[i])
        jaccard_index.append(temp)
JI=np.mean(jaccard_index)
print('mean jaccard index: '+str(round(JI, 2)))