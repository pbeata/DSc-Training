'''

May 29, 2021

Stage 1: Implement the basic multilayer perception (MLP) class 
Status: DONE


Stage 2: Expand MLP class to accomplish the following:
- save activations and derivatives
- implement back propagtion
- implement gradient descent
- implement training step
- train our neural network with a dummy dataset
- make some predictions using our network
Status


'''

import numpy as np
from random import random


'''
A Multilayer Perception Class for Machine Learning with Deep Neural Networks
'''
class MLP:

	# Constructor for MLP class: takes in number of inputs, 
	# 	size of each hidden layer, and number of outputs
	def __init__ (self, num_inputs=3, num_hidden=[3, 5], num_outputs=2):

		# Arguments =============================
		#	num_inputs (int): number of input nodes in the neural network
		#	num_hidden (int): list of integers describing the width of each hidden layer
		# 	num_outputs (int): number of output nodes
		# =======================================

		# initiate the member variables
		self.num_inputs = num_inputs
		self.num_hidden = num_hidden  # number of nodes in the hidden layer
		self.num_outputs = num_outputs

		# size of each layer stored in a temporary list
		layers = [num_inputs] + num_hidden + [num_outputs]

		# initiate the connection weights with random values
		weights = []
		for i in range( len(layers) - 1 ):
			#				   num_rows   num_cols
			w = np.random.rand(layers[i], layers[i+1])
			weights.append(w)
		self.weights = weights

		# we will need to store activations
		activations = []
		for i in range( len(layers) ):
			a = np.zeros(layers[i])
			activations.append(a)
		self.activations = activations

		# we will need to store derivates
		derivatives = []
		for i in range( len(layers) - 1 ):
			d = np.zeros((layers[i], layers[i+1]))
			derivatives.append(d)
		self.derivatives = derivatives
		

	# forward propagate through the network ("left to right") 
	def forward_propagate(self, inputs):
		# for 1st layer, activations are just the original inputs
		activations = inputs
		self.activations[0] = activations

		# update the activations by moving left to right through the layers
		for i, wts in enumerate(self.weights):

			# calculate the net inputs
			net_inputs = np.dot(activations, wts)		# np.dot() --> matrix multiplication

			# calculate the activations
			activations = self._sigmoid(net_inputs)
			self.activations[i+1] = activations  # recall: a_3 = f(h_3),  h_3 = a_2 * W_2

		# return final activations as the outputs
		return activations

	# back propagation
	def back_propagate(self, error, verbose=False):

		# dE/dW_i = (y - a[i+1]) * sig'(h[i+1]) * a[i]
		# sig'(h[i+1]) = sig(h[i+1]) * (1 - sig(h[i+1]))
		# sig(h[i+1]) = a[i+1]

		# dE/dW[i-1] = (y - a[i+1]) * sig'(h[i+1]) * Wi * sig'(h[i]) * a[i-1]

		# iterate backwards through the network layers
		for i in reversed(range(len(self.derivatives))):

			# get activations for the previous layer
			activations = self.activations[i+1]

			# multiply error by the derivative of the sigmoid function 
			delta = error * self._sigmoid_derivative(activations)
			
			# make delta a 2D array with a single row: [[0.1, 0.2]]
			delta_reshaped = delta.reshape(delta.shape[0], -1).T

			# get activations for current layer 
			current_activations = self.activations[i]  
			
			# move from array row to COLUMN 2D array to do matrix dot product: [[0.1], [0.2]]
			current_activations = current_activations.reshape(current_activations.shape[0], -1)

			# save the new derivatives by using matrix multiplication to perform: a[i] * delta[i+1]
			self.derivatives[i] = np.dot(current_activations, delta_reshaped)

			# back propagate the next error: E = (y - a[i+1]) * sig'(h[i+1]) * Wi
			error = np.dot(delta, self.weights[i].T)

			if verbose:
				print("\nDerivatives for W{}: {}".format(i, self.derivatives[i]))

		return error  # (not necessary anymore)

	# gradient descent algorithm
	def gradient_descent(self, learning_rate):
		for i in range(len(self.weights)):

			# get the current weights and derivatives
			weights = self.weights[i]
			derivatives = self.derivatives[i]
			
			# debug:
			# print("\nOriginal W{}: {}".format(i, weights))
			
			# update the weights
			weights += derivatives * learning_rate

			# debug:
			# print("Updated W{}: {}".format(i, weights))

	# training our neural network
	def train(self, inputs, targets, num_epochs, learning_rate):

		# loop over all epochs to train the neural network
		for i in range(num_epochs):
			sum_error = 0.0

			# nice trick for unpacking
			for input_j, target_j in zip(inputs, targets):

				# perform the forward propagation 
				output_values = self.forward_propagate(input_j) 

				# calculate the error
				error = target_j - output_values

				# perform back propagation
				self.back_propagate(error)

				# apply gradient descent
				self.gradient_descent(learning_rate)

				# update the error using MSE metric
				sum_error += self._mse(target_j, output_values)

			# report error for each epoch
			print("Error: {} at epoch {}".format(sum_error / len(inputs), i))

	# mean square error
	def _mse(self, target, output):
		return np.average((target - output) ** 2)

	# sigmoid activation function
	# 	input: x (float)
	#	output: f(x) (float) where f is the sigmoid activation function
	def _sigmoid(self, x):
		return 1.0 / (1.0 + np.exp(-x))

	# derivative of the sigmoid function
	def _sigmoid_derivative(self, x):
		return x * (1.0 - x)


if __name__ == "__main__":


# STAGE 1

	# define the hyperparameters of our deep NN
	# my_inputs = 2
	# my_hidden_layers = [5]
	# my_outputs = 1 

	# set the random seed for our project
	# seed = 1010
	# rng = np.random.default_rng(seed)

	# create an MLP object (the NN)
	# mlp = MLP(num_inputs=my_inputs,
	# 		  num_hidden=my_hidden_layers,
	# 		  num_outputs=my_outputs)

	# create some random dummy inputs to test
	# input_values = np.random.rand(mlp.num_inputs)
	# input_values = rng.random(mlp.num_inputs)

	# perform the forward propagation 
	# output_values = mlp.forward_propagate(input_values) 

	# print the results
	# print("The network input is: {}".format(input_values))
	# print("The network output is: {}".format(output_values))


# STAGE 2

'''
	# simple dummy input and target for testing addition
	input_values = np.array([0.1, 0.2])
	target_values = np.array([0.3])

	# perform the forward propagation 
	output_values = mlp.forward_propagate(input_values) 

	# calculate the error
	error = target_values - output_values

	# perform back propagation
	mlp.back_propagate(error, verbose=False)

	# apply gradient descent
	mlp.gradient_descent(learning_rate=1)
'''

	# create a dataset to train a network for the sum operation
	inputs = np.array([[random()/2 for _ in range(2)] for _ in range(1000)])
	targets = np.array([[i[0] + i[1]] for i in inputs])

	# testing the sum operation
	mlp = MLP(2, [5], 1)

	# train our neural network
	mlp.train(inputs, targets, 50, 0.1)

	# create dummy data
	inputs = np.array([0.3, 0.1])
	targets = np.array([0.4])

	# predictions
	outputs = mlp.forward_propagate(inputs)
	print("\n\nOur network believes that {} + {} is equal to {}.".format(inputs[0], inputs[1], outputs[0]))
