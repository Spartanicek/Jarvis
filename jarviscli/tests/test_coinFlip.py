import unittest
from tests import PluginTest  
from plugins.coin_flip import coin_flip


class CoinFlipTest(PluginTest):
    def setUp(self):
        self.test = self.load_plugin(coin_flip)

    def test_coin_flip(self):
        coin_flip.coin_flip(self.mock_jarvis, None)

        last_output = self.mock_jarvis.say.call_args[0][0]

        self.assertIn(last_output, ['Heads', 'Tails'])
        

if __name__ == '__main__':
    unittest.main()