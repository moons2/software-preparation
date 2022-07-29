'''
https://leetcode.com/problems/unique-paths-ii/

You are given an m x n integer array grid.
There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). 
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. 
A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

---

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

---

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

---

# EM ANALISE
1. Fundamentos da Ciencia da Computaçao
	Estruturas de Dados, Algoritmos
2. Se voce tem heuristica, um método cientifico para solução de problemas ou apenas
	propoe abordagens aleatórias
3. Voce escreve código limpo, lógico e mantenível?

# PROCESSO
.	listen to carefully
I.	clarification questions
II.	speak logic solution out loud
III.runtime analysis
IV.	code
V.	desk test

---

APPROACH I.
	Encaro a grade como um grafo, onde as celulas são vertices
	e as arestas o movimento entre os vertices.

	depois de mapeado o meu grafo eu realizo uma busca em largura
	evitando os vertices onde há obstáculos.

	quando atingido o vertice destino eu incremento a variavel
	que guarda a quantidade de caminhos possiveis


vertice == end, incrementa caminhos possiveis
se grapho(vertice) == obstaculo, não faça nada

grapfo	  =	(grapho, start[i][j], end[i][j])
visitados =	[(i0,j0)]
queue 	  = [(i0,j1), (i1,j0)]
vertice   = (i0,j0)

IPUT:

	[0,1,0]
	[0,0,0]

visited = [(0,0),]
queue = [(0,1),(1,0)]
vertex = (0,0)
nPaths = 0
end    = (0,3)
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
	# def countPaths(graph, start, end):
	# corner cases
	# o que retornar quando o grapho for vazio?
	# o que retornar se start for igual a end?

	columns = len(obstacleGrid[0])
	rows	= len(obstacleGrid)
	end 	= (rows-1, columns-1)

	visited = set()
	queue = [(0,0)]
	nPaths = 0

	while queue:
		vertex = queue.pop(0)

		if vertex == end:
			nPaths += 1

		i, j = vertex
		if obstacleGrid[i, j] is not 1 and vertex not in visited:
			visited.add(vertex)

			if (j+1) < columns:
				queue.append((i, j+1))
			if (i+1) < rows:
				queue.append((i+1, j))

	return nPaths



	
