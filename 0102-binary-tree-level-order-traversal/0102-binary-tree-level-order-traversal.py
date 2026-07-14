# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        def max_depth(root) :
            if root is None:
                return 0
            return max(max_depth(root.left),max_depth(root.right))+1
        
        depth = max_depth(root)
        if depth == 0 :
            return []
        
        arr = [[] for _ in range(depth)]
        def dfs(root,cnt,arr) :
            if root is None :
                return

            arr[cnt].append(root.val)
            cnt += 1
            dfs(root.left,cnt,arr)
            dfs(root.right,cnt,arr)
            cnt -= 1

            return arr

        return dfs(root,0,arr)