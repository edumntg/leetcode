# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def traversal(root):
            if not root:
                return []

            if not root.left and not root.right:
                return [root.val]

            return traversal(root.left) + [root.val] + traversal(root.right)
        
        return traversal(root)

        