import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.output = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return self.output
        q = collections.deque()
        q.append((root, 0))
        while q:
            now, level = q.popleft()
            if len(self.output) <= level:
                self.output.append([])
            self.output[level].append(now.val)
            if now.left:
                q.append((now.left, level + 1))
            if now.right:
                q.append((now.right, level + 1))
        return self.output