class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else: 
            return False
    """
        # Follow up: Could you solve it without converting the integer to a string?
        if x < 0:
            return False
        original = x
        reverse = 0
        while x > 0:
            reminder = x % 10
            reverse = reverse * 10 + reminder
            x //= 10
        return original == reverse
    """