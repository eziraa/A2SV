class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        numbers = [n for n in range(1, n + 1)]
        index = -1
        while len(numbers) > 1:
            index = (index + k) % len(numbers)
            numbers.pop(index)
        return numbers[0]
