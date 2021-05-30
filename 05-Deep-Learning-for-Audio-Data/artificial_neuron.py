
import math

def sigmoid(x):
	y = 1.0 / (1.0 + math.exp(-x))
	return y

def activate(inputs, weights):
	# perform net input
	h = 0.0
	for x, w in zip(inputs, weights):
		h += x * w
	
	# perform activation step
	return sigmoid(h)

if __name__ == "__main__":
	print("hello audio world")

	inputs = [0.5, 0.3, 0.2]
	weights = [0.4, 0.7, 0.2]

	output = activate(inputs, weights) # computational unit of the neuron

	print(output)
