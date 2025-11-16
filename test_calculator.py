import unittest
import calculator 

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        assert add(1,1) == 2
        assert add(2,1) == 3
        assert add(2,3) == 5

    def test_subtract(self): # 3 assertions
        assert subtract(1,1) == 0
        assert subtract(2,1) == 1
        assert subtract(2,3) == -1


    ######## Partner 1
    def test_multiply(self): # 3 assertions
        assert mul(1,1) == 1
        assert mul(2,1) == 2
        assert mul(2,3) == 6

    def test_divide(self): # 3 assertions
        self.assert div(1,1) == 1
        self.assert div(2,1) == 2
        self.assert div(2,3) == 2/3

    ######## Partner 2
    def test_divide_by_zero(self): 
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        assert logarithm(10,100) == 2
        assert logarithm(10,1000) == 3
        assert logarithm(10,10000) == 4

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        assert hypotenuse(3, 4) == 5
        assert hypotenuse(5, 12) == 13
        assert hypotenuse(8, 15) == 17

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(<INSERT_ERROR_TYPE>):
            square_root(-1)
        square_root(4)
        square_root(9)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
