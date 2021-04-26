import unittest
from gumballmachine import push, State, Message


class GumBallMachineTest(unittest.TestCase):
    def testCoinLeadsToCoinIn(self):
        result = push(State.wait_for_coin, Message.insert_coin)
        self.assertEqual(result, State.coin_in)

    def testRequestGumLeadsToCoinOutOrGumOut(self):
        result = push(State.coin_in, Message.request_gum)
        self.assertIn(result, {State.gum_out, State.coin_out})

    def testCoinOutLeadsToWaitForCoin(self):
        result = push(State.coin_out, Message.item_out)
        self.assertEqual(result, State.wait_for_coin)

    def testGumOutLeadsToWaitForCoin(self):
        result = push(State.gum_out, Message.item_out)
        self.assertEqual(result, State.wait_for_coin)

    def testWrongInputLeadsToSameState(self):
        result = push(State.gum_out, Message.insert_coin)
        self.assertEqual(result, State.gum_out)


if __name__ == 'main':
    unittest.main()
