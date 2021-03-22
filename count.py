# def sumOfUnique(nums):
#     mydict={}
#     total=0
#     for i in nums:
#         if i not in mydict:
#             mydict[i]=1
#         else:
#             mydict[i]+=1
#         print(mydict)
#     for key, value in mydict.items():   
#         if  value==1:
#             total=total+key
#     return total
# print(sumOfUnique([1,2,3,1]))
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
    def __init__(self, preorder):
        self.preorder=preorder

    def binarytree(self,preorder):
        if preorder:

            root=TreeNode(preorder.pop(0)) 
        print(root)
        print(preorder)
        return self.helper(root,preorder )
        
        
    def helper(self,root, preorder ):
        for x in preorder:
            if x<root.val:
                x=root.left
                root.left=self.helper(root.left,preorder)
            if x>root.val:
                x=root.right
                root.right=self.helper(root.right,preorder)
        return root 


bt=Solution([1,3])
print(bt.binarytree([1,3]))


        
            

