class Solution:
    def replaceCharacter(self, s, oldChar, newChar):
        result = ""

        for i in s:
            if i == oldChar:
                result += newChar
            else:
                result += i

        return result