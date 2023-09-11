#Rendering instances for 500 timestamps , performing random actions
import gym 
env = gym.make('Acrobot-v1')
env.reset()
for _ in range(500):
    env.render()
    env.step(env.action_space.sample())
# Checking all env available, also the uninstalled ones
from gym import envs
print(envs.registry.all())
