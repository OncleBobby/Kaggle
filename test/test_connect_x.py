import unittest

class TestStringMethods(unittest.TestCase):

    def test_agent(self):
        import os, sys
        agents_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\\connect_x\\agents\\')

        agent_path = f'{agents_folder}submission.py'
        default_agent_path = f'{agents_folder}default.py'
        num_episodes = 10
        from connect_x.tools import valide_agent, get_agent, battle
        agent = get_agent(agent_path)
        if valide_agent(agent):
            # Run multiple episodes to estimate its performance.
            print("My Agent vs Default Agent:", battle(agent, get_agent(default_agent_path), num_episodes))
            print("My Agent vs Random Agent:", battle(agent, "random", num_episodes))
            print("My Agent vs Negamax Agent:", battle(agent, "negamax", num_episodes))
        else:
            print('Not a valide agent !')

        self.assertEqual('foo'.upper(), 'FOO')