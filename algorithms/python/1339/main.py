# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.total = 0
        self.ans = 0
        self.mod = int(10e8) + 7

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.total = self.get_total(root)
        self.get_total(root)

        return (self.ans % self.mod)

    def get_total(self, root: Optional[TreeNode]):
        left, right = 0, 0
        if root.left:
            left = self.get_total(root.left)
        if root.right:
            right = self.get_total(root.right)
        tot = left + right + root.val

        if self.total != 0:
            self.ans = max(self.ans, ((self.total - tot) * tot))
        return tot
