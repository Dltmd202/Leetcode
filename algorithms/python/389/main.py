import collections


# 389. Find the Difference
# Accepted
# Runtime: 32ms
# faster than 83.12% of Python3 online submissions for Find the Difference.
# O(N)
# N = len(s)
# defaultdict 의 조회 및 추가 시간 복잡도 = O(1)
# O(N + (N + 1) = O(2N + 1) = O(N)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        items = collections.defaultdict(int)
        for item in s:
            items[item] += 1
        for item in t:
            items[item] -= 1
            if items[item] < 0:
                return item