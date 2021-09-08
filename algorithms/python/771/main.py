# 771. Jewels and Stones
# Accepted
# Runtime: 28ms
# faster than 85.16% of Python3 online submissions for Jewels and Stones.
# O(N^2)
# 1 <= jewels.length, stones.length <= 50
# N = len(stones) = len(jewels)
# jewels에 대한 in 연산의 시간 복잡도 O(N)
# stones의 iteration 시간 복잡도 O(N)
# O(N^2)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)