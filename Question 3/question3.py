import pandas as pd
train_data_x = pd.read_csv('train_data.txt', sep='\t')
train_data_y = pd.read_csv('train_truth.txt')

from tensorflow import keras
from tensorflow.keras import layers
# Building a neural network (deep learning) model
inputs = keras.Input(shape=(3,))
hidden_layer1 = layers.Dense(4)(inputs)
hidden_layer2 = layers.Dense(4)(hidden_layer1)
hidden_layer3 = layers.Dense(4)(hidden_layer2)
hidden_layer4 = layers.Dense(4)(hidden_layer3)
output = layers.Dense(1)(hidden_layer4)
model = keras.Model(inputs=inputs, outputs=output, name='MLP')
model.compile(optimizer='adam', loss=keras.losses.MeanSquaredError(), metrics=['mae']) # rmsprop, adam, adagrad

for i in range(10):
    model.fit(train_data_x, train_data_y)

test_data_x = pd.read_csv('test_data.txt', sep='\t')
predicted = model.predict(test_data_x)
predicted = [x[0] for x in predicted]

test_output = pd.DataFrame()
test_output['y'] = predicted
test_output.to_csv('test_predicted.txt', index=False)