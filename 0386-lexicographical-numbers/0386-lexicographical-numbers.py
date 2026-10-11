
class Solution(object):
    def lexicalOrder(self, n):
        result = []

        def find(num):
            if num > n:
                return

            result.append(num)

            for i in range(10):
                find(num * 10 + i)

        for i in range(1, 10):
            find(i)

        return result

n = 2