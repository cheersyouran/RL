import sys
sys.path.append('/Users/Youran/Projects/PortfolioManagement')
from task2.QLearningModel_beta.env import Env
from task2.QLearningModel_beta.QLearningModel import QLearningModel
from task2.QLearningModel_beta.market import Market

train_window = 50
test_window = 10

market = Market()

def run_a_kind_of_model(kind):
    print('#######################################################################')
    print('Kind:', kind)
    while True:
        env = Env(train_window, test_window, market)
        env.kind = kind
        RL = QLearningModel(actions=list(range(env.nb_portcodes + 1)))
        count = 0
        episode = 1
        while True:
            rewards = 0
            env.reset()
            obs = env.get_obs()
            while True:
                a = RL.choose_action(str(obs))
                obs_, r, done = env.step(a)
                RL.learn(str(obs), a, r, str(obs_))
                rewards = rewards + r
                obs = obs_
                print(count)
                count = count + 1
                if done:
                    break
            ratio = rewards / (train_window * 10)
            print('Episode: ', episode, 'Rewards: ', rewards, 'Accuracy: ', ratio)
            if (ratio > 0.9):
                break
            if (episode > 10):
                break
            episode = episode + 1

        rewards = 0
        obs = env.get_obs()
        while True:
            a = RL.choose_action(str(obs))
            obs_, r, done = env.step(a)
            rewards = rewards + r
            print('Action: ', a, 'Reward: ', r)
            obs = obs_
            if done:
                break
        ratio = rewards / (test_window * 10)
        print('Rewards: ', rewards, 'Accuracy: ', ratio)
        market.pass_a_day()


# run_a_kind_of_model('银行')
run_a_kind_of_model('计算机')

