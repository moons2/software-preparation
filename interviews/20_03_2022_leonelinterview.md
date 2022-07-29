bruno
luan


Input: num1 = "11", num2 = "123"
Output: "134"


approach 1:



num1 = 			 "11"
							^
num2 = 			"123"
						 ^ 	
soma = "134"

C	  010
     39
    ^
+ 11135
	  ^
	   74
  
  //10 %10
  
1110
0079
^
0999 		4
^  
1078

Tempo de Execução:	O(N), para N igual o maior numero de digitos
Armazenamento:			O(N)

# codigo



class Solution:
	def sumStrings(num1, num2):
  	
    carry = 0
    soma = ""
    i = len(num1)-1
    j = len(num2)-1
    res = []
      
    while n1 != 0 and n2 != 0:
    	dig1 = num1[n1] if n1 != 0 else 0
    	
    	c, sum = (int(num1[i]) + int(num2[i]) + c)//10, (int(num2[i]) + int(num1[i]) + c) %10
      res.append(str(soma))
      
      
      n1 =- 1
      n2 =- 1
      
	def add string(..)    
				i, j = len(num1) -1 , len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry > 0:
            n1_val = 0 if i < 0 else int(num1[i])
            n2_val = 0 if j < 0 else int(num2[j])
            unit_res = n1_val + n2_val + carry
            unit_res, carry = unit_res%10, unit_res//10
            res.append(str(unit_res))
            i -= 1
            j -= 1
        return "".join(res[::-1])
    
      
45m
https://leetcode.com/problems/add-strings/
- Perguntas de clarificação
- Gostei que falou sobre carry
- Poderia ter apresentado a solução usando um edge case
- Falou sobre a complexibilidade corretamente de tempo sem eu perguntar, esqueceu o de armazenamento
- Pode colocar umas variáveis com nomes mais intuitivos 
- Uma maneira melhor de trabalhar com concatenar em uma string é usando um array e depois passando para string
- Apresentou uma solução boa e conseguiu identificar os bugs quando perguntei
- Lidou bem com as dicas que foram dadas

# BRUNO
---------------------------------

Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

Input: head = [4,5,1,1,9], node = 5
Output: [4,1,9]

Input: head = [4,5,1,1,9], node = 1
										 
Output: [4,5,9]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



Input: head = [4,5,1,9], node = 5

             
4 -- >1 ---> 9 
             
Big tempo : 0(1)
Big() armazenamento : O(1)

def delNode(head, node):
	nextVal = node.next.val
  nextNode = node.next.next
  node.val = nextVal
  node.next = nextNode
  
def delNode(head, node)
	node.val, node.next = node.next.val, node.next.next
                     
Input: head = [4,5,1,9], node = 1

--------------------------------------------------------------------------------------
problem 2


You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Input: digits = [1,2,3]
Output: [1,2,4]

Input : digits = [1,4,5]
Output: [1,4,6]

Inplace

Input: digits = [9,9,9]
			 
Output: [1,0,0,0]


1 
0999 
   1 
----
1000

Big(O) tempo : O(n) com n tamanho do digits
			 Armazenamento inplace O(1)
       
def addOne(digits):
	i = len(digits) - 1
  carry = 1
  
  while i >= 0:
  	actSum = carry + digits[i]    
    if actSum//10 == 0:
    	 carry = 0
       break
    if actSum%10 > 0:
    	digits[i] = actSum%10
    i -= 1
  if carry > 0:
  	digits.insert(0, carry)
  return digits

i = 2
digits = [1,0,0,0]
				^
carry = 1
													0    
digits = [1,1,1,1,1,1,1,1,1,0,0]

------
FEEDBACK

12 min
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/
- boas perguntas de clarificação (se housse repetição)
- chegou a conclusão ótima de primeira
- acertou na analise Big O
- poderia ter aproveitado para demonstrar conhecimentos sobre estrutura de dados Lista simplesmente ligada
- explicou bem a solução
- chegou numa solução mais raída


30 min
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
- perguntou sobre nums negativos
- chegou na ideia central do carry ser igual a 1
- chegou na analise de complexidades corretas
- bons nomes de variaveis
- existe algum caso onde o carry seja maior que 1?
- chegou na solução


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i], c = (digits[i] + c) % 10, (digits[i] + c) // 10
            if not c:
                break
        
        if c:
            digits.insert(0, c)
        
        return digits
