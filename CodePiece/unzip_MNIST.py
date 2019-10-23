# note: this tf version is 1.5.0
import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np

# 1st , download the 4 gz files from official website,and put it into MNIST_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

print(mnist.train.num_examples)
# print(mnist.validation.num_examples)
# print(mnist.test.num_examples)

print(mnist.train.images.shape)
print(mnist.train.labels.shape)

print(mnist.train.labels[:10])

np.save("train_x.npy", np.reshape(mnist.train.images,(mnist.train.images.shape[0],28,28,1)))
np.save("train_y.npy", mnist.train.labels)
