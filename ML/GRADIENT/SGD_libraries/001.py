from sklearn.linear_model import SGDRegressor, SGDClassifier 
# SGD for linear Regression with 1000 epochs
regressor = SGDRegressor(loss = 'squared_loss', max_iter = 1000)

import touch.optim as optim
optimizer = optim.SGD(model.parameters(), lr =  0.01)

from tensorflow.keras.optimizers import SGD
optimizer = SGD(learning_rate = 0.01)

