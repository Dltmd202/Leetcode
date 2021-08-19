class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            print(left, s[left], s[right], right)
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                print(s[left + 1: right + 1], s[left: right], s[left + 1: right + 1][::-1], s[left:right][::-1])
                if s[left + 1: right + 1] == s[left + 1: right + 1][::-1] or \
                        s[left: right] == s[left: right][::-1] or \
                        len(s[left + 1: right]) == 0:
                    return True
                else:
                    return False
        return True