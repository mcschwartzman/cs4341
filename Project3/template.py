import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from keras.utils import np_utils
# Model Template
import random
import PIL
import csv


# with open('eggs.csv', 'wb') as csvfile:
#    	accwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     accwriter.writerow([epoch])

from PIL import Image
from random import shuffle	
#############Pre-processing data##########
images = np.load('images.npy')
labels = np.load('labels.npy')
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []
ten = []

training = []
validation  = []
test = []
placeHolder = []

for i in images:
	placeHolder.append(np.reshape(i,784))
	
x = 0
while x < 6500:
	if x >= 0 and x < 650:
		one.append(placeHolder[x])
	if x >= 650 and x < 1300:
		two.append(placeHolder[x])
	if x >= 1300 and x < 1950:
		three.append(placeHolder[x])
	if x >= 1950 and x < 2600:
		four.append(placeHolder[x])
	if x >= 2600 and x < 3250:
		five.append(placeHolder[x])
	if x >= 3250 and x < 3900:
		six.append(placeHolder[x])
	if x >= 3900 and x < 4550:
		seven.append(placeHolder[x])
	if x >= 4550 and x < 5200:
		eight.append(placeHolder[x])
	if x >= 5200 and x < 5850:
		nine.append(placeHolder[x])
	if x >= 5850 and x < 6500:
		ten.append(placeHolder[x])
	x = x+1
numbers = [one,two,three,four,five,six,seven,eight,nine,ten]
for i in numbers:
	#random.shuffle(i)
	x = 0
	while x < 650:
	#390 in training
		if x < 390:
			training.append(i[x])
	#98 in validation
		if x >= 390 and x < 488:
			validation.append(i[x])

	#165 in test
		if x >= 488 and x < 650:
			test.append(i[x])
		x =x+1
		
		
x_train = np.array(training)
x_val = np.array(validation)


img = Image.fromarray(x_val[1].reshape(28,28), 'L')
img.save('my.png')

test2 = []

	

##do the same thing for labels
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []
ten = []

training = []
validation  = []
test8 = []
x = 0
for i in labels:
	a = keras.utils.np_utils.to_categorical(i,10)
	
	if x >= 0 and x < 650:
		one.append(a)
	if x >= 650 and x < 1300:
		two.append(a)
	if x >= 1300 and x < 1950:
		three.append(a)
	if x >= 1950 and x < 2600:
		four.append(a)
	if x >= 2600 and x < 3250:
		five.append(a)
	if x >= 3250 and x < 3900:
		six.append(a)
	if x >= 3900 and x < 4550:
		seven.append(a)
	if x >= 4550 and x < 5200:
		eight.append(a)
	if x >= 5200 and x < 5850:
		nine.append(a)
	if x >= 5850 and x < 6500:
		ten.append(a)
	x = x+1
numbers = [one,two,three,four,five,six,seven,eight,nine,ten]
for i in numbers:
	#random.shuffle(i)
	x = 0
	while x < 650:
	#390 in training
		if x < 390:
			training.append(i[x])
	#98 in validation
		if x >= 390 and x < 488:
			validation.append(i[x])

	#165 in test
		if x >= 488 and x < 650:
			test8.append(i[x])
		x =x+1
training2 = []
for i in training:
	training2.append(i[0])
y_train = np.array(training2)
validation2 = []

for i in validation:

	validation2.append(i[0])
y_val = np.array(validation2)



######Make Model##############
model = Sequential() # declare model
model.add(Dense(500, input_shape=(28*28, ), kernel_initializer='he_uniform')) # first layer
model.add(Activation('tanh'))

model.add(Dense(250))
model.add(Activation('tanh'))



model.add(Dense(10, kernel_initializer='he_uniform')) # last layer
model.add(Activation('softmax'))


# Compile Model
model.compile(optimizer='sgd',
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Train Model
history = model.fit(x_train, y_train, 
                    validation_data = (x_val, y_val), 
                    epochs=50, 
                    batch_size=180)


# Report Results

recordFile = open('./history.txt', 'w+')
recordFile.write(str(history.history))

print(history.history)

prediction = model.predict(np.array(test))
for i in prediction:
	print(i)
