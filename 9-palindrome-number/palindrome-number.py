class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stringNum = str(x)
        for index in range(len(stringNum)):
            if index < int(len(stringNum) / 2):
                if stringNum[index] != stringNum[(len(stringNum) -1) - index ]:
                    return False
            else:
                return True
        return True