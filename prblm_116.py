# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if root is None:
            return root
        
        queue = list()
        queue.append(root)
        queue.append(None)
        
        while(True):
            
            while True:
                ele = queue.pop(0)
                if ele == None:
                    break
                else:
                    ele.next = queue[0]
                    if ele.left:
                        queue.append(ele.left)
                    if ele.right:
                        queue.append(ele.right)
            
            if len(queue):
                queue.append(None)
            else:
                break
        return root
