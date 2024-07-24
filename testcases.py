import unittest
import numeron

class TestNumeron(unittest.TestCase):

    #メソッド名は test_ からはじめる           

    def test_case1(self):

        game = numeron.Numeron_game(2)

        ans = [9, 8, 7]
        num = [0, 9, 1]

        expected = {
            "eat":0,
            "bite":1
        }

        test = {
            "eat" : game.count_eats(num, ans),
            "bite" : game.count_bites(num, ans)
        }

        self.assertEqual(expected, test)

    def test_case2(self):

        game = numeron.Numeron_game(2)

        ans = [9, 2, 0]
        num = [3, 2, 9]

        expected = {
            "eat":1,
            "bite":1
        }

        test = {
            "eat" : game.count_eats(num, ans),
            "bite" : game.count_bites(num, ans)
        }

        self.assertEqual(expected, test)

    def test_case3(self):

        game = numeron.Numeron_game(2)

        ans = [9, 8, 0]
        num = [9, 8, 1]

        expected = {
            "eat":2,
            "bite":0
        }

        test = {
            "eat" : game.count_eats(num, ans),
            "bite" : game.count_bites(num, ans)
        }

        self.assertEqual(expected, test)

    def test_case4(self):

        game = numeron.Numeron_game(2)

        ans = [9, 3, 1]
        num = [0, 2, 8]

        expected = {
            "eat":0,
            "bite":0
        }

        test = {
            "eat" : game.count_eats(num, ans),
            "bite" : game.count_bites(num, ans)
        }

        self.assertEqual(expected, test)

    def test_case5(self):

        game = numeron.Numeron_game(2)

        ans = [9, 3, 1]
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

if __name__=="__main__":
    unittest.main()        