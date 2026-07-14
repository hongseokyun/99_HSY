# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        def dfs(r, arr):
            if r is None:
                return len(arr)
            arr.append(r.val)
            left_cnt = dfs(r.left, arr)
            right_cnt = dfs(r.right, arr)
            arr.pop()
            return max(left_cnt, right_cnt)
 
        return dfs(root, [])