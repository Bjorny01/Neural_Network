import numpy as np
from Neural_Network import *
from mnist_loader import *

net = Network([784, 30, 10])
training_data, validation_data, test_data = load_data_wrapper()

net.SGD(training_data, 30, 10, 3.0, test_data = test_data)

np.save( 'weights_0.npy' , net.weights[0])
np.save( 'weights_1.npy' , net.weights[1])
np.save( 'biases_0.npy' , net.biases[0])
np.save( 'biases_1.npy' , net.biases[1])


