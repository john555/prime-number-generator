import unittest

def generate_primes(n):
    """generates prime numbers from 0 to n"""
    

class GeneratePrimeTest(unittest.TestCase):

    def test_throws_error_if_input_is_not_numeric(self):
        with self.assertRaises(TypeError):
             generate_primes("99")
             generate_primes([])
             generate_primes({})
             generate_primes((0,))

    def test_returns_list_if_input_is_valid(self):
        self.assertEqual(type(generate_primes(0)), type([]))

    def test_returns_empty_list_as_output_for_1(self):
        self.assertEquals(generate_primes(1), [])
    
    def test_returns_correct_output_for_2(self):
        self.assertEquals(generate_primes(2), [2])
    
    def test_returns_correct_output_for_13(self):
        self.assertEquals(generate_primes(13), [2, 3, 5, 7, 11, 13])