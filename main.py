import tensorflow as tf
from tensorflow import keras
import numpy as np
#import matplotlib.pyplot as plt
import os
#import subprocess
from PIL import Image
labels = []
def importImages():
	imArr = []
	for i in range(10):
		if(i!=9):
			directory = "English/Hnd/Img/Sample00"+(str)(i+1)
		else:
			directory = "English/Hnd/Img/Sample010"
		for file in os.listdir(directory):
			img = Image.open(os.path.join(directory,file))
			imArr.append(img)
			labels.append(i)
dataSet = importImages()
a = tf.placeholder(tf.float32)
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(tf.float32, 1200, 900)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])	
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])	
model.fit(dataSet, labels, epochs = 5, steps_per_epoch = 6)
