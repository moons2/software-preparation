class Solution:
    def swap(self, matrix, i, j):
        matrix[i][j] = matrix[j][i]
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        .   listen to carefully
        I.  clarification questions
        II. speak your logic solution out loud
        III.runtime analises
        IV. code
        V.  table test
        
        .
        1.  is guaranteed that all elements of a matrix are
            non null?
            In case of null what would you like to be returned?
        2.  I'd make another question about
        
        
        Approach I.
        
        A B C
        D E F
        G H I
        
        percorremos a matriz diagonalmente fazendo a transposição dos elementos
        diagonalmente a direita, isto é, e[a][b] = b[b][a]
        em seguida percorremos a mesma matriz até o centro fazendo o deslocamento das colunas
        
        RUNTIME ANALYSIS
        TIME:  O(N^2) since we must traverse a half of a matrix
        SPACE: O(1)
        
        """
        
        matrixSize = len(matrix)
        
        # transposição
        for i in range(matrixSize):
            for j in range(i+1, matrixSize):
                matrix[i][j],  matrix[j][i] = matrix[j][i],  matrix[i][j]
        
        # espelhamento
        for i in range(matrixSize):
            for j in range(matrixSize // 2):
                matrix[i][j],  matrix[i][matrixSize-j-1] = matrix[i][matrixSize-j-1],  matrix[i][j]
        
        
        
        
        