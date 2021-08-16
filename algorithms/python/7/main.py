class Solution:
    def reverse(self, x: int) -> int:
        max_val, min_val = int(pow(2, 31) - 1), -int(pow(2, 31))
        if x >= 0:
            ans = int(str(x)[::-1])
            return ans if ans <= max_val else 0
        else:
            str_x = str(x)
            ans = int(str_x[0] + str_x[1:][::-1])
            return ans if min_val <= ans else 0