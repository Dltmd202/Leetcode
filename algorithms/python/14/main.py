from functools import reduce


class TrieNode:
    def __init__(self, depth):
        self.children = collections.defaultdict()
        self.depth = depth


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for s in zip(*strs):
            s = sorted(list(s))
            if s[0] == s[-1]:
                res += s[0]
            else:
                break
        return res
