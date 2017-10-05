from __future__ import print_function
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import numpy

data = numpy.load('images.npy')

(x_train, y_train), (x_val, y_val) = data



model = Sequential()

model.add(Dense(10, input_shape = (28*28, ), kernel_initializer='he_normal'))
model.add(Activation('relu'))


model.add(Dense(10, kernel_initializer='he_normal'))
model.add(Activation('softmax'))

model.compile(optimizer='sgd', loss='categorical_cossentropy', metrics=['accuracy'])

history = model.fit(x_train, y_train, validation_data = (x_val, y_val), epochs = 10, batch_size = 512)

print (history.history)

