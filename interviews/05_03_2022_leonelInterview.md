1. clarificação
2. desenvolvimento enquanto discursa
3. codigo
4. analise de complexidade
5. teste de mesa

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Big(o) : tempo O(n) e armazenamento O(n)

HashTable {
	2: 0
  11: 1,
  
}

[ 2, 11, 7, 15]
 target - x2 (7) = 2
 

x1 + x2 = 9
x1 = 9 - x2
x2 = 9 - x1

# CODIGO

def sumOfNums(nums, target):
	hashT = {}
  
  for i, v in enumerate(nums):
  	if (target - v) in hashT:
    	return [hashT[target - v],  i]
    hashT[v] = i
  
# TESTE DE MESA

sumOfNums([2,3], 5)
hashT = {
	2: 0,
}

valores = [2, 3] => [0, 1]
indices = [0, 1]



20m
https://leetcode.com/problems/two-sum/
- Perguntas de clarificação muito boas
- É importante escrever o big(o) pra que o entrevistador veja claramente
- Alterou o exemplo pra que possa lidar com um possível erro
- Usando estruras de dados e soube explicar bem hashTable
- É interessante oferecer o teste de mesa
- É importante estar atento ao tempo pois em um exercício fácil é muito grande as chances de vir outro
- Importante pegar um exemplo que possa causar algum erro
- nomes das variaveis bem intuitivas e codigo bem limpo





