# print an inverted binary tree

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val= val
        self.left= left
        self.right= right



# insert a node 

    
class Solution:
    def __init__(self):
        self.listroot = None

    def construct(self,listroot):
        
        head=listroot[0]
        print(head)
        newlist=[listroot[2:]]
        print(newlist)
        return self.helper(head,newlist)

    def helper(self,head,newlist):
        root=TreeNode
        root.val=head
        for x in newlist:
            if x>root.val:
                root.left=self.helper(head,root.left)
                x=root
            if x<root.val:
                root.right=self.helper(head,root.right)
                x=root
        return root

    def invertBT(self,root:TreeNode):
        
        if not root: return 
        root.left=self.invertBT(root.left)
        root.right= self.invertBT(root.right)

        temp =root.left
        root.left=root.right
        root.right= temp 

        return root

s1=Solution()
# s1.listroot=[4,2,7,1,3,6,9]
x=s1.construct([4,2,7,1,3,6,9])
print(x)


