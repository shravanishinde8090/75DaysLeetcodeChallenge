
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def find(index, ans):
            if index == len(digits):
                result.append(ans)
                return

            letters = phone[digits[index]]

            for ch in letters:
                find(index + 1, ans + ch)

        find(0, "")
        return result
