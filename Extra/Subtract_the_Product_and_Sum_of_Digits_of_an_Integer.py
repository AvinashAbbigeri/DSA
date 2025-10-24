# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """

        product = 1
        sums  = 0
        while(n != 0):
            temp = n%10
            product *= temp
            sums += temp
            n //= 10

        diff = product - sums
        return diff