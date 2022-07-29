
# LOGIC SOLUTION

'''
input:
[1, 2, 3]

output:
[1, 2, 4]


c = 0
[1, 2, 3]
	   ^

c = 0
[1, 2, 9]  


c = 0
[1, 2, 4]
 	   ^
 	   3+c = 4

if c = 0, exit


if c:
	num.insert(0, c)

'''




class Solution:
	def plusOne(digits):

		c = 1
		for i in range(len(digits)-1, -1, -1):
			digits[i], c = (digits[i] + c) % 10, (digits[i] + c) // 10

			if not c:
				break

		if c:
			digits.insert(0, c)

		return digits

# tempo de execução O( n ), sendo n o numero de digitos no vetor
# complexidade de espaço O( n ), porque só teremos 1 vetor com n digitos

'''
Exemplo 1:

c = 1
[1, 0, 0, 0]
 ^
        		


'''