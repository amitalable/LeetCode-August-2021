# https://leetcode.com/problems/complex-number-multiplication
class Solution:
    '''
        a + bi * c+di 
        ac + (ad + bc)*i -bd
    '''

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        ind1 = num1.index("+")
        ind2 = num2.index("+")
        x1, y1 = int(num1[:ind1]), int(num1[ind1+1:-1])
        x2, y2 = int(num2[:ind2]), int(num2[ind2+1:-1])
        return str(x1*x2-y1*y2) + "+" + str(x1*y2+x2*y1)+"i"
