from neural_network import NN
import numpy as np

# add lineage tracking?

class Gene:
	def __init__(self, input_len, hidden_layers, output_len):
		self.input_len = input_len
		self.hidden_layers = hidden_layers
		self.output_len = output_len
		self.nn = NN(input_len, hidden_layers, output_len)

	def breed(self, gene): # weight-wise? # layer-wise? # average everything?
		# print(gene)

		# technically not the best way of doing this because it will first init the weights and thus wastes time...
		new_gene = Gene(self.input_len, self.hidden_layers, self.output_len)

		for i in np.arange(len(self.nn.weights)):
			new_gene.nn.weights[i] = (self.nn.weights[i] + gene.nn.weights[i]) / 2

		for i in np.arange(len(self.nn.biases)):
			new_gene.nn.biases[i] = (self.nn.biases[i] + gene.nn.biases[i]) / 2

		return new_gene

	def mutate(self): # add epsilon? # pick a weight and re-init?
		pass

	def action(self, state):
		return self.nn.predict(state)

	def save(self, file_name):
		self.nn.save(file_name)

	def load(self, file_name):
		self.nn.load(file_name)
