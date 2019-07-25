
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        result = []
        
        result.append([root])
        
        while(1):
            temp = []
            for node in result[-1]:
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)
            if len(temp) == 0:
                break
            result.append(temp)
        
        result2 = []
        for row in result:
            temp = [ node.val for node in row ]
            result2.append(temp)


        return [ result2[ind] if ind%2 == 0 else result2[ind][::-1] for ind in range(len(result2)) ]
        
        
