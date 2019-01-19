import os

_rep="/Users/olivierpartensky/Desktop/Programme/GitHub/neural-networks-and-deep-learning-master/src/"
os.chdir(_rep)
print(os.listdir(_rep))

import mnist_loader
import network

data = mnist_loader.load_data_wrapper()
training_data, validation_data, test_data = data

net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
