class Solution:
    def convert(self, s: str, numRows: int) -> str:
        limit = max(1, numRows * 2- 2)
        length = len(s)
        cnt = 0
        ans = ""
        for r in range(1, numRows + 1):
            grad = [limit - (r - 1) * 2, (r - 1) * 2]
            cur = r - 1
            idx = False
            while cur < length:
                if (grad[0] and grad[1]) or not idx:
                    ans += s[cur]
                cur += grad[idx]
                idx = not idx
        return ans