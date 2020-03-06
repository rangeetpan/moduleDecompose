#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:00:53 2020

@author: rangeet
"""

from utils.mnistutil import MNISTUitl
#from utils.sliceutil import Slice
from keras.models import load_model
import itertools
import numpy as np
#Module Load
labs = [0,1,2,3,4,5,6,7,8,9]
labs1 = [0,1]
module=[]
accuracy=[]
class1=0
class2=0
sx = 28
sy = 28

mn = MNISTUitl()
X, Y, x, y = mn.getdata2(0,0,sx,sy)
nm , xt, yt = mn.trainDense4(X, Y, x,y,sx,sy)
acc=nm.predict(xt).argmax(axis=-1)
acc=np.mean(np.equal(acc, yt))
module.append([class1, class2])
accuracy.append(acc)
with open("outputSequenceTrain.txt", "w") as txt_file:
    for line in module:
        txt_file.write(" ".join(str(line)) + "\n")
with open("outputAccTrain.txt", "w") as txt_file:
    for line in accuracy:
        txt_file.write(str(line) + "\n")