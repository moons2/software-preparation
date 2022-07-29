Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]


   3
 9  20
   15  7
Output: [[3],[9,20],[15,7]]


===
c = 2
q = [9, 20]
out = [[3], [9]]

q = [3, 9, 20, x, y, 15, 7]
out =[[1], [9,20], [15,7]]

2^n - 1

0				2^0 = 1
1				2^1 = 2
2	      2^2 = 4
				2^nivel = len(q)
        n = log(q)/log(2)

ANALISE DE COMPLEXIDADE:
	TEMPO	: O(n)+O(n) = O(n)
  ESPAÇO:	O(1) + O(n) + O(n) = O(n)
        

					3
 			 9        20
    x   y    >15   7

groupedNodes = [[3],[1]]
visitNodes = [3, 1, 2, 0, null, null, 3]
							
						  ^
              i
       ->3(0)
  	1(1)			  2(2)
 0(3)		(4) 	(5)			3(6)
 
 node = visitedNodes.get(0)
 if node.left
		visitedNode.append(node.left)
 if node.right
 		visitedNode.append(node.right)
 
 
# FISRT APPROACH
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def groupNodesByLevel(root):
  	
    queue = []
    out = []
    visitNodes = []
    
    visitNodes.add(root)
    
    while visitNodes:
    	node = visitNodes.remove(0)
      queue.append(node.val)
      
      if node.left:
      	visitNodes.add(node.left)
      else:
      	queue.append(None)
      
    
45m
https://leetcode.com/problems/binary-tree-level-order-traversal/
- Perguntas de clarificação : arvore binária,
- Explicou bem sobre como funciona a travessia em largura
- Teve dificuldade em abordar o problema a partir do algoritmo de travessia em largura
- Não conseguiu usar a dica que eu dei ( n sei se eu que fiz ela zuada kk )
- Teve dificuldade em apresentar a complexibilidade de espaço e tempo ( se enroscou na matemática)
- Não ficou muito claro como ia resolver o problema
 
 def levelOrder(root):
 	
  q = [root]
  out = []
  
  while q:
  	ans = []
    lvl = len(q)
    while lvl:
    	lvl -= 1
      node = q.pop(0)
      ans.append(node.val)
      if node.left:
      	q.append(node.left)
      if node.right:
      	q.append(node.right)
    out.append(ans)
  return out
 
===== 	BRUNO	

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true

			2
   1     3
 

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

true and true = bst valida
             5
          3      8
 		   2	     4	 9	
    
    q = [5]
 		out = [4]
Complexibilidade tempo : O(n) n sendo números de nós
                 espaço: O(1)


se existir nó:
	va para esquerda;
  no atual;
  va para direita;



q = [2,3,5,4,8,9]
         l r

def isValidBST(root):
	left = 0
  right = 1
	if root:
  	helper(root)
  if len(q) == 1:
  	return True
	else:
  	while len(q) > 0:
    	if q[right] > q[left]:
      	right +=1
        left +=1
			else:
      	return False
  
def helper(node):
	if node.left:
  	helper(root.left) 
  q.append(root.val) 
	if node.right	    
    helper(root.right)

## FEEDBACK
https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

problema easy
~ 42min
- boa pergunta de clarificação (apenas uma)
- chegou na ideia solução rápido (muito bom)
- chama fila de pilha (cuidado)
- se enrolou no desenvolvimento, mas com o auxilio tava caminhando pro caminho certo

i.	TRAVESSIA EM ORDEM
ii. VERIFICAR SE O VETOR ESTÁ ORDENADO

travessia em profunidade:
		-	pre, in, pos ordem
travessia em largura:
		- 
  
class Solution:
    BTS = [-inf]
    
    def inOrderTraverse(self, root: Optional[TreeNode]):
        if root:
            self.inOrderTraverse(root.left)
            if BTS[0] > root.val:
            	return False
            self.BTS = [root.val]
            self.inOrderTraverse(root.right)
        
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # corner case for single node tree
        if not root.right and not root.left:
            return True
        
        self.inOrderTraverse(root)
        
        for i in range(1, len(self.BTS)):
            if self.BTS[i] < self.BTS[i-1]:
                return False
        
        return True