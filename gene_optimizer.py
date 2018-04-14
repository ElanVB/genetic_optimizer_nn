from gene import Gene
import numpy as np

class GeneOptimizer:
	def __init__(self, input_len, hidden_layers, output_len, population_size, scoring_function):
		self.input_len = input_len
		self.hidden_layers = hidden_layers
		self.output_len = output_len
		self.population_size = population_size

		self.genes = []
		for _ in np.arange(population_size):
			self.genes.append(self.random_gene())

		self.scoring_function = scoring_function

	def random_gene(self):
		return Gene(self.input_len, self.hidden_layers, self.output_len)

	def score(self): # average multiple trials?
		scores = []
		for i in np.arange(self.population_size):
			scores.append(self.scoring_function(self.genes[i]))

		return scores

	def rank(self, score):
		sort_order = np.argsort(score)[::-1]
		# print(sort_order)
		# print(self.genes)
		# print(score)
		# print(sort_order)
		new_genes = []
		# new_scores = []
		for from_index, to_index in enumerate(sort_order):
			# print(from_index, to_index)
			new_genes.append(self.genes[to_index])
			# temp = self.genes[from_index]
			# self.genes[from_index] = self.genes[to_index]
			# self.genes[to_index] = temp

			# new_scores.append(score[to_index])
			# temp = score[from_index]
			# score[from_index] = score[to_index]
			# score[to_index] = temp
		# print(self.genes)
		# self.genes = self.genes[sort_order] # this might not work
		self.genes = new_genes
		self.champion = self.genes[0]
		# print(np.array(new_scores))
		print(np.array(score)[sort_order])

		# for i in sort_order: self.swap(i, self.population_size - 1)
		# might be able to do something clever with the swap order

	def populate(self): # populate the next generation
		# print(self.genes)
		self.rank(self.score())

		num_breeders = int((self.population_size - 1) / 2)
		new_genes = self.genes[:num_breeders]
		for i in np.arange(0, num_breeders, 2):
			new_genes.append(new_genes[i].breed(new_genes[i+1]))

		while len(new_genes) < self.population_size:
			new_genes.append(self.random_gene())

		self.genes = new_genes
		# print(self.genes)

	# def champion(self):
	# 	return self.champion
