

Given the head of a linked list, remove the nth node from the end of the list and return its head.

#1 
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



head = [1,2,3,4,5], n = 2
            ^ ^


Big (o) tempo : O(n), n tamanho da lista 
				Armazenamento O(1)

def removeNode(head, n):
	count = 0
  init = head
  prev = None
  pres = head
	if head == None:
  	return None
  while head:
  	count += 1
    head = head.next
  count = count - n + 1
  
  for i in range(count - 1):
  	prev = pres
    pres = pres.next
  
  prev.next = pres.next
  
  return init
  

head = [1,2,3,5], n = 2 
head              ^
init    ^
prev        ^
pres          ^ 
count = 0
        
==== 	FEEDBACK
# problema 1
~ 34min
dificuldade facil

https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

"No caso de ponteiro nulo, o que gostia de retornar?"
clafiricação: perguntou sobre nulo e sobre circular
- não chegou na solução
- precisou de ajuda na analise assintótica
- poderia ter explicado o que é lista simplesmente ligada
- bons usos de nomes de variaveis, mas poderia ser melhor
- explicou bem depois que entendeu o problema


						1 -> 2 -> 3 -> 				n = 2
s			 	    ^
f 					              ^ 
dummy 			^

s.next = s.next

dummy = ListNode(0, head)
        left = dummy
        faster = head
        
        while faster:
            if n != 0:
                n -= 1
            else:
                left = left.next
            faster = faster.next
        
        left.next = left.next.next
        
        return dummy.next
        
        
        
===================================================================================================== luan ===
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]


            4
				2      7
      1   3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# approach 1:
															n = 4
						    5
			  	3						7
			1  ->  4
	0

#	1. verifica se o elemento atual é o procurado e retorna
# 2. verifica se lemento procurado é menor que o atual e vai para a esquerda
# 3. se não vai para a direita
3 4. return None porque não encontrou

analise assintótica
tempo:			O(log(n)), sendo n o numero de nós na arvore
spaço:			O(1)

# CÓDIGO

class Solution:
	def findSubTree(self, root, n):
  	
    iterator = root
    while iterator:
    	if iterator.val == n:
      	iterator
      if n < iterator.val:
      	iterator = iterator.left
			else:
      	iterator = iterator.right
    
    return None

# TESTE DE MESA


# CASO 
															N = 1
						  5
			  3						7
		 >1      4
	0

# CASO 2

							5
			  3						7
		 1      4
	0

problem 2

==========

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.


Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

pilha  = [)]

				"( ( ( ( ) ) [ ]"
         ^
         
         
         char 
         	
Analise Big O:
	tempo:	O(n), n sendo o numero de caracteres
  spaco:	O(n)


# CODIGO

class Solution:
	def isStringValid(s):
  	
    pilha = []
    closedDict = {
    	")":"(",
      "]":"[",
      "}":"{"
    }
    
    for char in s:
    	if char in closedDict.values():
      	pilha.append(char)
      else:
      	if pilha[-1] != closedKeys[char]:
        	return False
      

FEEBACK

16m
https://leetcode.com/problems/search-in-a-binary-search-tree/
- Perguntas de clarificação
- Explicação clara de como sulucionar o problema
- Falou sobre árvore binária de busca e explicou corretamente
- Análise de complexibilidade correta tanto para tempo quanto para espaço
- Chegou em uma solução
- Nomes das variáveis claras e intuitivas
- Teste mesa muito fácil de visualizar 

20m
https://leetcode.com/problems/valid-parentheses/
- Perguntas de clarificação
- Falou sobre pilha e explicou bem como é o funcionamento
- Apresentou uma solução teórica muito clara
- Análise de complexibilidade tanto de espaço quanto de tempo exata 
- Chegou em uma solução apesar do tempo ter acabado


class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        
        for ch in s:
            if ch == '(':
                li.append(')')
            elif ch == '{':
                li.append('}')
            elif ch == '[':
                li.append(']')
            elif len(li) != 0:
                if ch == li[-1]:
                    li.pop()
                else:
                    return False
            else:
                return False
        if len(li) == 0:
            return True
        else:            
            return False

