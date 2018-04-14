from gene_optimizer import GeneOptimizer
import gym, numpy as np

env = gym.make('CartPole-v0')
input_shape = env.observation_space.shape[0]
output_shape = env.action_space.n

# generations = 50
generations = 20
population_size = 100

def scoring_function(gene):
	repititions = 5

	total_reward = 0.0

	for _ in np.arange(repititions):
		done = False
		state = env.reset()

		while not done:
			# env.render()
			action = gene.action(state[np.newaxis, :])[0]
			state, reward, done, info = env.step(action)
			total_reward += reward

	return total_reward / repititions

def demo(gene):
	done = False
	state = env.reset()
	total_reward = 0.0

	while not done:
		env.render()
		action = gene.action(state[np.newaxis, :])[0]
		state, reward, done, info = env.step(action)
		total_reward += reward

	print(total_reward)

optimizer = GeneOptimizer(input_shape, [10, 5], output_shape, population_size, scoring_function)

counter = 0
while counter < generations:
	# demo(optimizer.champion)
	optimizer.populate()
	demo(optimizer.champion)
	counter += 1
	print(optimizer.champion)

print('\nFinished training')

print('How will it do?')

demo(optimizer.champion)
optimizer.champion.save("champ.p")
