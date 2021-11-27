from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            return self.compare(p, q)

    def compare(self, p, q):
        if p.val == q.val:
            left, right = False, False
            if p.left and q.left:
                left = self.compare(p.left, q.left)
            elif not p.left and not q.left:
                left = True

            if p.right and q.right:
                right = self.compare(p.right, q.right)
            elif not p.right and not q.right:
                right = True

            return left and right
        else:
            return False
