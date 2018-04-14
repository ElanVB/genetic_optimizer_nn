from gene import Gene
import gym, numpy as np

env = gym.make('CartPole-v0')
input_shape = env.observation_space.shape[0]
output_shape = env.action_space.n

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

print('How will it do?')

agent = Gene(input_shape, [10, 5], output_shape)
agent.load("champ.p")
demo(agent)
