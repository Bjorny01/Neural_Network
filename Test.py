from Neural_Network import sigmoid
from Interface import *

#Create input
input = create_bitstring_interface()
input_array = np.array([int(bit) for bit in input]).reshape(784, 1)

#Load trained network
weights_0 = np.load('weights_0.npy')
weights_1 = np.load('weights_1.npy')
biases_0 = np.load('biases_0.npy')
biases_1 = np.load('biases_1.npy')

#Calculate digit
layer_1 = sigmoid(np.dot(weights_0, input_array) + biases_0)
layer_2 = sigmoid(np.dot(weights_1, layer_1) + biases_1)

output = np.argmax(layer_2)
print(output)





