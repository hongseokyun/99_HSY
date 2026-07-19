# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return "[]"
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")
        return ",".join(result)

    def deserialize(self, data):
        if data == "[]":
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        queue = [root]
        i = 1
        while queue and i < len(vals):
            node = queue.pop(0)
            if vals[i] != "None":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != "None":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root