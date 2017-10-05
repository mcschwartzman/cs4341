from __future__ import print_function
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import numpy

class zero:
	def __init__(self, label, image):
		self.label = label
		self.image = image # use function to find image per label?

##... use different class for each number ...##




labelarray = numpy.load('labels.npy')

######=========== Read data into chunks for validation, test, and train ========########

print(data)

for n in data:
	print(n)




model = Sequential()

model.add(Dense(10, input_shape = (28*28, ), kernel_initializer='he_normal'))
model.add(Activation('relu'))

#############============ MODEL GOES HERE ====================############

model.add(Dense(10, kernel_initializer='he_normal'))
model.add(Activation('softmax'))

model.compile(optimizer='sgd', loss='categorical_cossentropy', metrics=['accuracy'])

history = model.fit(x_train, y_train, validation_data = (x_val, y_val), epochs = 10, batch_size = 512)

print (history.history)

