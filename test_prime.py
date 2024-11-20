from prime import is_prime
import unittest

def is_prime(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):
    def test_prime_2(self):
        self.assertTrue(is_prime(2))

    def test_prime_3(self):
        self.assertTrue(is_prime(3))

    def test_prime_5(self):
        self.assertTrue(is_prime(5))

    def test_prime_7(self):
        self.assertTrue(is_prime(7))

    def test_non_prime_1(self):
        self.assertFalse(is_prime(1))

    def test_non_prime_4(self):
        self.assertFalse(is_prime(4))

    def test_non_prime_6(self):
        self.assertFalse(is_prime(6))

    def test_non_prime_8(self):
        self.assertFalse(is_prime(8))

    def test_large_prime(self):
        self.assertTrue(is_prime(7919))

    def test_large_non_prime(self):
        self.assertFalse(is_prime(8000))

    def test_prime_11(self):
        self.assertTrue(is_prime(11))

    def test_prime_13(self):
        self.assertTrue(is_prime(13))

    def test_non_prime_9(self):
        self.assertFalse(is_prime(9))

    def test_non_prime_15(self):
        self.assertFalse(is_prime(15))

    def test_prime_17(self):
        self.assertTrue(is_prime(17))

    def test_prime_19(self):
        self.assertTrue(is_prime(19))

    def test_non_prime_20(self):
        self.assertFalse(is_prime(20))

    def test_prime_23(self):
        self.assertTrue(is_prime(23))

    def test_prime_29(self):
        self.assertTrue(is_prime(29))

    def test_non_prime_25(self):
        self.assertFalse(is_prime(25))

if __name__ == '__main__':
    unittest.main()