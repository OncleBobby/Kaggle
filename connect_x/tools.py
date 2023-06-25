import sys
from kaggle_environments import evaluate, make, utils
from kaggle_environments.agent import get_last_callable
env = make("connectx", debug=True)
def get_agent(path):
    submission = utils.read_file(path)
    return get_last_callable(submission, path=path)
def valide_agent(agent):
    env = make("connectx", debug=True)
    env.run([agent, agent])
    return env.state[0].status == env.state[1].status == "DONE"
def mean_reward(rewards):
    return sum(r[0] for r in rewards) / float(len(rewards))