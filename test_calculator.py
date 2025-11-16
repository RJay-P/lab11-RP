# https://github.com/RJay-P/lab11-RP
# Partner 1: Ray-Jay Peart
import unittest
import calculator as calc


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        assert calc.add(1, 1) == 2
        assert calc.add(2, 1) == 3
        assert calc.add(2, 3) == 5

    def test_subtract(self):  # 3 assertions
        assert calc.subtract(1, 1) == 0
        assert calc.subtract(2, 1) == 1
        assert calc.subtract(2, 3) == -1

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        assert calc.mul(1, 1) == 1
        assert calc.mul(2, 1) == 2
        assert calc.mul(2, 3) == 6

    def test_divide(self):  # 3 assertions
        assert calc.div(1, 1) == 1
        assert calc.div(2, 1) == 2
        assert calc.div(2, 3) == 2 / 3

    ######## Partner 2
    def test_divide_by_zero(self):
        #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            calc.div(0, 5)

    #     fill in code

    def test_logarithm(self):  # 3 assertions
        assert calc.logarithm(10, 100) == 2
        assert calc.logarithm(10, 1000) == 3
        assert calc.logarithm(10, 10000) == 4

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            assert calc.logarithm(1, 100)

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            calc.logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        assert calc.hypotenuse(3, 4) == 5
        assert calc.hypotenuse(5, 12) == 13
        assert calc.hypotenuse(8, 15) == 17

    def test_sqrt(self):  # 3 assertions
        #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            calc.square_root(-1)
        assert calc.square_root(4) == 2
        assert calc.square_root(9) == 3
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
