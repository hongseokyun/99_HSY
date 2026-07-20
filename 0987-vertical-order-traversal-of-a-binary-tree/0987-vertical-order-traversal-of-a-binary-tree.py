# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        max_col = float("-inf")
        min_col = float("inf")
        arr = []
        def dfs(root,row,col) :
            if not root :
                return
            arr.append((root.val,row,col))
            dfs(root.left,row+1,col-1)
            dfs(root.right,row+1,col+1)
        dfs(root, 0, 0)
        cols = [c for _, _, c in arr]
        min_col, max_col = min(cols), max(cols)
        arr.sort(key=lambda x: (x[2], x[1], x[0]))
        result = [[] for _ in range(max_col - min_col + 1)]
        for val, r, c in arr:
            result[c - min_col].append(val)
        return result