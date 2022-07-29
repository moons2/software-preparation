





# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    BTS = []
    
    def inOrderTraverse(self, root):

        if root:
            self.inOrderTraverse(root.left)
            self.BTS.append(root.val)
            self.inOrderTraverse(root.right)
        
    
    def isValidBST(self, root):
        """
        .   listen to carefully
        I.  clarfication questions
        II. speak your logic solution out load
        III. runtime analysis
        IV. code
        V.  table test
        
        this appear to be a simple traverse tree problem, where we verify in each visit
        if the left and right node follow the rule of a binary search tree.
        
        
                5
         4              6
       1            3
    
        inOrderTraverse = [ ]
                           ^
        
        BTS = [5,4,6,1,3]
        
        
        visitNode(node):
            if node:
                if node.left
        """
        
        # corner case for single node tree
        if not root.right and not root.left:
            return True
        
        self.inOrderTraverse(root)
        print(self.BTS)
        
        for i in range(1, len(self.BTS)):
            if self.BTS[i] <= self.BTS[i-1]:
                print("False")
                return False

        
        print("True")
        return True
        

if __name__ == '__main__':
    print("Hi")
    root = TreeNode(0)
    root.left = TreeNode(-1)
    solve = Solution()
    solve.isValidBST(root)
