''' Summary:
 * All tests except ComplexRootsTest.test_function_1 should pass with a ValueError
 * Output: FAILED (errors=1)
 * Read comments for more details
'''

# Relevant documentation: https://docs.python.org/3.5/library/unittest.html

# Import the unittest module to create unit tests
import unittest

# Import our function to be tested
from quadratic import roots, roots_corrected

# Other dependencies
import cmath

# Then we create a class which subclasses unittest.TestCase
class QuadraticEquationTest(unittest.TestCase):

    '''
     * We can name our methods anything we want as long as they begin with 'test'
     * Each method corresponds with one test
    '''
    def test_eq1(self):
        '''
        Equation: x^2 - x - 30 <==> (x + 5)(x - 6)
         ==> a = 1, b = -1, c = -30
        By simple algebra, we know the roots are x = 5, x = 6
        '''
        
        expected_answer = (6, -5) # You can confirm this manually
        output = roots(a=1, b=-1, c=-30)
        
        # This method *asserts* that the two arguments are equal
        # If they aren't, this method tells you... assertively
        self.assertEqual(output, expected_answer)
        
    def test_eq1a(self):
        '''
        We're testing the same equation as before, but using a different method
         * This method doesnt' care about the order the answers are in
         * We're just testing if the output *contains* our answer
        ''' 
        
        output = roots(a=1, b=-1, c=-30)
            
        # self.assertIn(a, b) checks if a is in b
        self.assertIn(6, output)
        self.assertIn(-5, output)

class ComplexRootsTest(unittest.TestCase):
    def setUp(self):
        '''
        The setUp() method
         * This method gets called before every test case in this class
         * We can use this to share information between tests
         
        Here, we'll be testing the same equation with both our roots()
        and roots_correct() functions

        Equation: x^2 + x + 5
         ==> a = 1, b = 1, c = 5
        
        Using WolframAlpha (http://www.wolframalpha.com/input/?i=x%5E2+%2B+x+%2B+5):
        the roots are
         * x1 = -0.5i * [sqrt(19) - i]
         * x2 =  0.5i * [sqrt(19) + i]
         
        
        Using the cmath module, we can represent this as:
         * x1 = -0.5j * (sqrt(19) - 1j)
         * x2 =  0.5j * (sqrt(19) + 1j)

        Documentation: https://docs.python.org/3/library/cmath.html

        '''
        
        self.x1 = -0.5j * (cmath.sqrt(19) - 1j)
        self.x2 = -0.5j * (cmath.sqrt(19) - 1j)

    def test_function_1(self):
        '''
         This test should fail because the roots() function uses sqrt()
         from the math module which only works for real numbers
        '''
        
        output = roots(a=1, b=1, c=5)
        
        self.assertIn(self.x1, output)
        self.assertIn(self.x2, output)
    
    def test_function_2(self):
        ''' This test should pass '''

        output = roots_corrected(a=1, b=1, c=5)
        
        self.assertIn(self.x1, output)
        self.assertIn(self.x2, output)
    
# Put this final clause to make your tests run when this script is executed!
if __name__ == '__main__':
    unittest.main()