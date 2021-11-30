# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    #직렬화
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = collections.deque([root])
        result = ["#"]
        
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(str(node.val))
            else:
                result.append("#")
        return " ".join(result)
        
    #역직렬화
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "# #":
            return None
        
        nodes = data.split()
        
        root = TreeNode(int(nodes[1]))
        q = collections.deque([root])
        index = 2
        
        while q:
            node = q.popleft()
            #여기서는 is not을 사용했지만 != 를 쓰는 것이 더 좋다. (None 구분이 아니므로)
            if nodes[index] is not "#":
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1
            
            if nodes[index] is not "#":
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
            
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))