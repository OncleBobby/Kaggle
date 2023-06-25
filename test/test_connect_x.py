import unittest

class TestStringMethods(unittest.TestCase):

    def test_agent(self):
        self.assertEqual('foo'.upper(), 'FOO')