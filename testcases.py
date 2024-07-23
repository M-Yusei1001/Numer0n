import unittest
from numeron import Numeron

class TestNumeron(unittest.TestCase):

    #メソッド名は test_ からはじめる           

    def test_case1(self):

        game = Numeron(2)

        ans = [9, 8, 7]
        num = [0, 9, 1]

        expected = {
            "eat":2,
            "bite":1
        }

        test = {
            "eat" : game.count_eats(num, ans),
            "bite" : game.count_bites(num, ans)
        }

        self.assertEqual(expected, test)

    def test_case2(self):

        game = Numeron(2)

        ans = [9, 9, 0]
        num = [3, 2, 9]

        expected = {
            "eat":0,
            "bite":2
        }

        test = {
            "eat" : game.count_eats(num, ans),
            "bite" : game.count_bites(num, ans)
        }

        self.assertEqual(expected, test)

    def test_case3(self):

        game = Numeron(2)

        ans = [9, 9, 0]
        num = [2, 9, 3]

        expected = {
            "eat":1,
            "bite":1
        }

        test = {
            "eat" : game.count_eats(num, ans),
            "bite" : game.count_bites(num, ans)
        }

        self.assertEqual(expected, test)

    def test_case4(self):

        game = Numeron(2)

        ans = [9, 3, 9]
        num = [0, 9, 9]

        expected = {
            "eat":1,
            "bite":1
        }

        test = {
            "eat" : game.count_eats(num, ans),
            "bite" : game.count_bites(num, ans)
        }

        self.assertEqual(expected, test)

if __name__=="__main__":
    unittest.main()        