# Import the unittest module to create unit tests
import unittest

# Import our function to be tested
from matrix_multiplication2 import matrix_multiply

class MatrixMultiplicationTest(unittest.TestCase):

    '''
     * We can name our methods anything we want as long as they begin with 'test'
     * Each method corresponds with one test
    '''
    
    def test_3x3_identity(self):
        matrix_1 = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
        matrix_2 = [[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]]
                  
        expected_answer = matrix_1
        output = matrix_multiply(matrix_1, matrix_2)
        
        self.assertEqual(output, expected_answer)
        
    def test_3x3_3x3(self):
        matrix_1 = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
        matrix_2 = [[2, 2, 2],
                    [2, 2, 2],
                    [2, 2, 2]]
                  
        expected_answer = [[12, 12, 12],
                           [30, 30, 30],
                           [48, 48, 48]]
        output = matrix_multiply(matrix_1, matrix_2)
        
        self.assertEqual(output, expected_answer)
        
    def test_10x10_10x3(self):
        matrix_1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
                    [31, 59, 68, 123, 345, 123, 145, 1000, 1023, 435],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
                    [31, 59, 68, 123, 345, 123, 145, 1000, 1023, 435],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
                    [31, 59, 68, 123, 345, 123, 145, 1000, 1023, 435],
                    [31, 59, 68, 123, 345, 123, 145, 1000, 1023, 435]]
        matrix_2 = [[1, 123, 23],
                    [2, 2, 2],
                    [2, 2, 2],
                    [123, 123, 432],
                    [4394, 432, 23],
                    [1, 123, 23],
                    [2, 2, 2],
                    [2, 2, 2],
                    [123, 123, 432],
                    [4394, 432, 23]]
                  
        expected_answer = [[  67556,    8980,    6162],
                           [ 971956,  145380,  102562],
                           [3570976,  499404,  519098],
                           [  67556,    8980,    6162],
                           [ 971956,  145380,  102562],
                           [3570976,  499404,  519098],
                           [  67556,    8980,    6162],
                           [ 971956,  145380,  102562],
                           [3570976,  499404,  519098],
                           [3570976,  499404,  519098]]
        output = matrix_multiply(matrix_1, matrix_2)
        
        self.assertEqual(output, expected_answer)

    def test_3x3_3x1(self):
        matrix_1 = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
        matrix_2 = [[10],
                    [2],
                    [2]]
                  
        expected_answer = [[ 20],
                           [ 62],
                           [104]]
        output = matrix_multiply(matrix_1, matrix_2)
        
        self.assertEqual(output, expected_answer)
        
    def test_3x3_zero(self):
        matrix_1 = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
        matrix_2 = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
        
        expected_answer = matrix_2
        output = matrix_multiply(matrix_1, matrix_2)
        
        self.assertEqual(output, expected_answer)
        
# Put this final clause to make your tests run when this script is executed!
if __name__ == '__main__':
    unittest.main()