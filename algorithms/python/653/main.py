# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def search(node, target=None):
            if target is None:
                left, right = 0, 0
                if node.left:
                    left = search(node.left)
                if node.right:
                    right = search(node.right)
                nums.append(node.val)

            else:
                print(node.val, target, target - node.val)
                if target - node.val in nums:
                    if target - node.val != node.val or cnt[node.val] > 1:
                        print(target, node.val)
                        return True

                print(node.left)
                if node.left and search(node.left, target):
                    return True
                if node.right and search(node.right, target):
                    return True
                return False

        nums = []
        search(root)
        print(nums)
        cnt = collections.Counter(nums)
        print(cnt)

        return search(root, k)