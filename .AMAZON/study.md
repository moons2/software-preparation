
## Time Complexity

Análise de Complexidade Temporal busca estimar quanto tempo um algoritmo levará para cumprir o trabalho baseado em sua estrutura. Independente de hardware e busca responder as perguntas

Este algoritmo é escalável?
Quao bem este algoritmo lidará com grandes datasets?

`Dado um certo problema e mais de um algoritmo, qual será o mais eficiente em termos de eficiencia?`

### The Best Case

O melhor caso ocorre quando a entrada está organizada de forma que o algoritmo produzirá sua melhor performance. A analise de melhor caso apresenta o limitante superior da performance.

### The Worst Case

Estima o tempo maximo que um algoritmo leva para produzir a saida dada determinadas condições. Esta metrica indica que não importa o que aconteça a performance nunca será pior que o indicado.

## Big O notation

Notação usada para quantificar a performance dos algoritmos

### O(1)

Tempo constante, quando não importa o tamanha da entrada, o tempo de resposta para a saída é sempre a mesma

Algumas operações conhecidas de tempo constante

. Adição/Recuperação de um item na pilha
. Recuperação do 1o elemento de uma lista
. Acesso a um elemento de uma tabela hash
. Bucket sort

### O(n)

Quando o tempo de execução cresce proporcionalmente ao tamanha da entrada

. Pesquisar por um elemento
. Encontrar o valor mínimo/máximo

### O(n^2)

Proporcional ao quadraro da entrada

### O(log n)


Uma forma de reduzir a complexidade de um algoritmo é comprometer a acurácia, produzindo um tipo de algoritmo chamado **algoritmo aproximado**.

## Validar um algoritmo

Validar um algoritmo confirma que ele está provendo a solução matemática ao problema que estamos tentando resolver.

Um processo de validação deve checar os resultados para todas as possibilidades de entrada possiveis.

Algoritmos podem ser divididos nos seguintes dois tipos baseados em hipóteses ou aproximações usados para simplificar a lógica para faze-los executar mais rápido.

=> **Algoritmo exato:** esperados produzir a solução precisa sem a determinação de qualquer tipo de hiótese.

=> **Algoritmo aproximado:** Quando a complexidade é dificil demais para se lidar dados os recursos, simplificamos o problema fazendo algumas suposições. Algoritmos baseados em simplificações ou suposições são ditos algoritmos aproximados.

Problema do vendedor viajante: um vendedor deve passar por todas as viagens e retornar ao ponto de partida, passando por todas as cidades, apenas uma vez.

## Explicabilidade

Habilidade de identificar as características que são usadas direta ou indiretamente para surgir com uma decisão particular

`bias: distorção da realidade, devido à intima participação do observador naquilo que está observando.`

A analise etica de algoritmos se tornou uma parte padrão no processo de validação para aqueles algoritmos que podem afetar a tomada de decisão.

# CAPITULO 2

## Estruturas de Dados usadas em Algoritmos

"Algortimos precisam, necessariamente, de estruturas de dados in-memory."

Estrutura de dados que armazenam coleções de dados

.	Listas: sequencia de elementos mutáveis ordenados
.	Tuplas: sequencia de elementos imutáveis ordenados
.	Sets: conjunto de elementos desordenado
.	Dictionary: conjunto desordenado de pares chave-valor
.	Data frames: estruturas bidimensionais para armazenar dados bidimensionais

### Listas ou Array

Tempo de execução das operações

Acesso: 	O(1)
Inserção: 	O(n)
Recuperação:O(n)
Deleção:	O(n)

### Tuplas

Estrutura armazenadora de dados, mas apenas de leitura

```python
tupla = (1, (10, 20, 30), 3)
tupla[0]	// 1
tupla[0] = 1// error, operação impossivel
```

`SEMPRE QUE POSSIVEL, PREFIRA ESTRUTURAS IMUTAVEIS, principalmente ao lidar com Big Data. Estruturas mutáveis tem uma penalidade na performance quando comparada a estruturas imutáveis`

Analise de complexidade

Append:		O(1)

### Dicionario

```python
# criação
bin_colors = dict()
ou
bin_colors = {
	'aprovado' = 'green',
	'reprovado'='vermelho'
}

# atualização
bin_colors['aprovado']='dourado'

# recurepação
bin_colors.get(key)
ou
bin_colors[key]
```

Analise de Complexidade

Recuperar:	O(1)
Inserir:	O(1)
Copiar:		O(n)

### Conjunto (Sets)

Conjunto armazena apenas chaves sem repetição

```python
novo_conjunto = set()

```

Analise de Complexidade

Adição:		O(1)
Deleção:	O(1)
Copia:		O(n)

O tempo para adicionar um novo elemento é independente do tamanho do conjunto.

### Dataframes

Uma estrutura de dados usada para armazenar tabelas

## Explorando tipo abstratos de dados

Abstrato: conceito usado para definir sistemas complexos em termos de suas funções nucleos comuns.

Abstração dá origem aos Tipos de Dados Abstratos (ADT). Ao esconder os detalhes a nivel de implementação. O uso de ADTs resulta em algoritmos mais simples e limpos.

### Vetor

Estrutura de armazenamento de dados básica de forma sequencial

### Pilha

Uma pilha é uma estrutura de dados usada para armazenar uma lista unidimensional. Armazena tanto em LIFO (last is first out) ou FILO (first in last out). A caracteristica definidora de uma pilha é a maneira que os elementos são adicionados ou removidos do fim da pilha

**push:** inserir na pilha
**pop:** recuperar o ultimo elemento inserido
**isEmpty:** true se a pilha está vazia

```Python
class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[-1]
	def size(self):
		return len(self.items)
```

> COMPLEXIDADE

push:	O(1)
pop:	O(1)
size:	O(1)
peek:	O(1)

Quando um usuario quer navegar pelo historico de navegação na web, uma estrutura de acesso no padrão LIFO. Outro exemplo são programas que necessitam de operações do tipo 'Desfazer'

### Queue

Assim como Stacks, Queues armazenam dados em uma estrutura de unidimensional. Elementos adicionados e removidos no formato FIFO (first in first out)

```Python
class Queue:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def enqueue(self, item):
		self.items.insert(0, item)
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
```

### Priority Queue

Priority Queueu is an Abstract Data Type for maintaining a set **S** of elements, with each element having a "priority" associated with it. In a Priority Queue, an element with high priority is served before an element with low priority and vice versa. In case two elements have the same priority, they are served according to their order in the queue.

Basic operations in a priority queue:

1.	**push(x)** inserts an element in the set S: **O(log(n))**
2.	**top() / peek()** returns the element with highest or lowest priority without modify the queue: **O(1)**
3.	**pop()** returns and remove the element of the set S: **O(log(n))**

### Heap Data Structure (Priority Queue)

Heap implements of the best way a Priority Queue. A common implementation of the heap is through a binary tree, wchich follows two properties:

1.	Structure: a complete binary tree, except possibly by the last one level
2.	Propertie: the key stored in each node is greater (or lower) to the keys in the node's children

Heap é uma árvore binária completa, mas geralmente os valores são armazenados em um vetor e seus valores são acessados através de posições relativas

				2
		3 				 6 			==	[2,3,6,8,10,15,18]
	8 		10 		15 		18

parent(i) = floor((i-1)/2)
left_child(i) = 2i + 1
right_child(i) = 21 + 2

Min Heap Property:	NÓ PAI <= NÓ FILHO
Max Heap Property:	NÓ PAI >= NÓ FILHO

Heaps são cruciais em muitos algoritmos gráficos de alta eficiencia, tais como Dijkstra menos caminho e algoritmo de Prim para árvore de espanha mínima. Ou Heap sorting algorithm e Huffman encoding.



#### Heap Operations

Operações Heapify formam o ponto crucial da maioria das operações em Heap.

Ambas as operações tem complexidade O(long(n))

heapify-down(i)
	pode ser invocada se um elemento A[i] viola a propriedade de heap com seus dois filhos. Mais precisamente quando ocorre uma operação de rotação na árvore.

heapify-up(i)
	é invocado quando o pai de um nó viola a propriedade de heap através da permuta entre o nó corrente e seu pai.



### Tree

Uma das estruturas de dados mais úteis devido a suas caracteristicas hierarquicas de armazenamento. Usa-se Arvore sempre que necessário representar relacões hierarquicas entre os elementos.

**TERMINOLOGIA RELACIONADA A ARVORE**

Nó raiz			Nó sem pai
Nivel de um nó	Distáncia do nó raiz
Nós primos 		Dois nós são ditos primos se estão no mesmo nível
Nó filho e pai 	Nó F é dito filho de B se descende diretamente de B
Grau da arvore	O grau maximo de conexoes encontrado entre os nós que constituem
(Aridade)		a árvore

Subarvore		uma porção da arvore onde um nó é eleito um nó raiz
Nó folha		Um nó que não possui filhos
Nó interno		Um nó que não é raiz nem folha
Arvore completa	Um arvore em que todos os nós (exceto folhas) tem a mesma
				aridade da árvore.
Arvore perfeita	Arvore em que todos os nós estão no mesmo nivel
Largura			Numero de nós folhas


### 4 TYPES OF TREE TRAVERSAL ALGORITHMS

*Definition:* Tree is a hierarchical Data Structure, that stores data in a structure manner, the data is sored in nodes, which are connected through edges, and it should not form a cycle.

#### TREE TRAVERSAL (OR TREE SEARCH)

É uma forma de travessia de grafos e faz referencia ao processo de visitar/editar cada nó em uma estrutura de árvore.

*DEPTH FIRTS SEARCH (DFS):* começa do nó raiz e visita todos de uma branch profundamente quão possivel for.

*BREADTH-FIRST SEARCH (BFS):* começa do nó raiz e visita todos os nós de uma dada profundidade antes de mover para a próxima profundidade na árvore.

```python
Inorder traverse

# vai para a arvore mais a esquerda, em seguida visita o dado atual e por fim
# vai para a arvore mais a direita
def InOrderTraverse(root):
	if root:
		InOrderTraverse(root.left)
		print(root.data)
		InOrderTraverse(root.rigth)


		 5
   4          3
 1   2           6

Depois de aplicar a travessia InOrder a saída seria:
[1, 4, 2, 5, 3, 6]

# visita o nó atual, depois vai para a arvore mais a esqueda, sem seguida a arvore mais a direita
def PreOrderTraverse(root):
	if root:
		print(root.data)
		PreOrderTraverse(root.left)
		PreOrderTraverse(root.right)

# input:
		 5
   4          3
 1   2           6

# output:
[5, 4, 1, 2, 3, 6]

def PostOrderTraverse(root):
	if root:
		PostOrderTraverse(root.left)
		PostOrderTraverse(root.rigth)
		print(root.data)

# input:
		 5
   4          3
 1   2           6

# output:
[1, 2, 4, 6, 3, 5]
```

**LEVEL TRAVERSE**

Queue toVisit = Null
toVisit.add(root)

while not toVisit.empty:
	node = toVisit.remove()
	print(node.val)

	if node.left:
		toVisit.add(node.left)
	if node.right:
		toVisit.add(node.right)

```python

# input:
		 5
   4          3
 1   2           6
 					9
 					

# output:
[5, 4, 3, 1, 2, 6]

toVisit = [1, 2, 6]
visited = [5, 4, 3]


```










Visitar a arvore em nível, i.e., todos os nós em certo nível da arvore, em seguida, 

### TIPOS DE ARVORES

#### ARVORE BINARIA 

Uma árvore cuja aridade é 2


## INTRODUCING SORTING AND SEARCHING ALGORITHMS

Why study searching and sorting algorithms is important?
	Because as searching and sorting algorithms are fundamental parts of more complex algorithms, understanding them will help to understand the most complex ones.
	In the era of Big Data, the ability to efficiently sort and search items in complex data structure is quite important as it is needed by many modern algorithms.

```python
# swapping variables in python

var1 = 1
var2 = 2
var1, var2 = var2, var1
```

### BUBBLE SORT

The simplest and slowest algorithm used for sorting.

**Worst-Case:** O(N^2)

```python
size = len(arr) - 1

	for i in range(size, -1, -1):
		smaller = i
		for j in range(i-1, -1, -1):
			if(arr[j] > arr[smaller]):
				smaller = j
		arr[i], arr[smaller] = arr[smaller], arr[i]

	print(arr)
```
### INSERTION SORT

Insertion sort has its better performance if the data set is already sorted, and its worst performance in O(n^2), its space complexity is O(n)

```python
def InsertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        element_next = list[i]
        while (list[j] > element_next) and (j >= 0):
            list[j+1] = list[j]
            j = j-1
        list[j+1] = element_next
    return list
```

### MERGE SORT

developed is 1940 by John von Neumann. The defining feature of this algorithm is that its performance is no dependent on whether the input data is sorted. Like MapReduce, this algorithm is based on a divide and conquer strategy

```python
# put implementation here after understand, please

```

Analise de Complexidade
O(n log n)

### SHELL SORT

```python
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)
```

Not for big data. It is used for medium-sized datasets. Uma performance rasoavel em uma lista com até 6k de elementos. Quao melhor ordenado a lista estiver melhor sera a performance do algoritmo. Um vetor ordenado tera performance O(N)

### SELECTION SORT




## INTRO TO SEARCHING ALGORITHMS

Efficiently searching is one of the most important functionalities.

### LINEAR SEARCH

```python
def LinearSearch(list, item):
	# must I return true if the list contains
	# the item ?
	for i, val in enumerate(list):
		if val == item:
			return True
	# achieves the end so, the item is not
	# present
	return False
```

Performance in Worst-Case is O(N)

### BINARY SEARCH

Com uma performance de O(Log N), a busca binaria requer que o conjunto de dados onde a busca é feita esteja ordenado.

```python
def BinarySearch(alist, item):
	l = 0
	r = len(alist) - 1

	while l <= r:
		mid = (r+l) // 2
		if alist[mid] == item:
			return True
		if alist[mid] < item:
			r = mid
		else:
			l = mid
	return False
```

### INTERPOLATION SEARCH

O array deve estar ordenado. Usa o valor alvo para estimar a posição do elemento no vetor ordenado. A busca binária. em contra partida, apenas busca na metade da seção onde a busca está sendo feita.

```python

```

Performace para o pior caso O(N),  e para o caso em que o espaço de busca esta razoavelmente distribuido é O(log(log(N)))


## INTRODUCING THE BASIC CONCEPCTS OF DESIGNING AN ALGORITHM

> _Algoritmo: um conjunto finito e não ambiguo de instruções que dado algum conjunto de condições iniciais pode ser aplicado uma sequencia prescrita para alcançar um certo objetivo e que has um conjunto reconhecido de condições e condições finais._

Então, desenhar um algoritmo é descobrir o _"conjunto finito de instruções não ambiguas"_ da forma mais eficiente possivel para alcançar um certo objetivo.

Os passos de desenhar um algoritmo são geralmente tediosos:

1. Entender o problema que estamos tentando resolver: os requisitos
2. Como fazer

um bom algoritmo deve respeitar as 3 seguintes preocupações:

1. Este algoritmo produzirá o resultado esperado?
2. Este é o jeito ótimo de obter estes resultados?
3. Como ele desempenhara em grandes bases de dados?


1.	Outra definição para algoritmo é _"Um algoritmo é uma solução matemática para um problema do mundo real"_. Para garantir que o algoritmo produzirá a saida necessária devemos nos atentar a.
	- **Definição da verdade:** saidas produzidas que produzem resultados conhecidos.
	- **Choosing metrics:** a definição das metricas corretas ajuda a quantificar com acurácia a qualidade do nosso algortimo 


## GRAPH ALGORITHMS

Uma classe de problemas que são melhor representados em termos de gráfos. Tais problemas são resolvidos usando uma classe de algoritmos chamados. **Algoritmos Gráfos**.

.	pesquisar um valor de forma eficiente em uma representação de dados em forma de grapho
	1.	descobrir a estrutura do grapho
	2.	estratégia correta de percorrer o grapho

### REPRESENTAÇÃO DE GRAPHOS

Um grapho é uma estrutura que representa dados em termos de vertices e arestas.

```representacao
graph = (V, E)
onde
V = conjunto de vertices
E = conjunto de arestas

v > V, é uma representação de um objeto real, como pessoa, nó, computador
e > E, é uma ligação entre dois vertices

e(v1, v2) | e > E & v_i E V
```

Desde que uma aresta conecta dois vertices, então, uma aresta representa
uma relação, que pode ser, uma amizade, dois nós conectados em um cluster
e assim por diante.

#### TIPOS DE GRAPHOS

1.	Grapho não-direcionado
2.	Grapho direcionado
3.	Multigraphos não direcionados
4.	Multigraphos direcionados

##### GRAPHO NÃO DIRECIONADO

Quando a relação entre os vertices não implica qualquer tipo de direção ou ordem.

```
	[1] ---- [3] --- [5]
	|
	|
	[7]
```
	Mike é irmão de Paulo
	Mike é amigo de Ana

##### GRAPHO DIRECIONADO

Quando a relação entre os vertices impoe uma direção.

```
	[1] ----> [3] ---> [5]
	^
	|
	[7]
```
	Mike vive em sua casa, mas sua casa não vive em Mike
	Paulo é gerente de Julio, mas o oposto não

##### GRAPHICOS MULTIPLOS NÃO DIRECIONADOS

```
	[1] ---- [3] --- [5]
	| |
	| |
	[7]
```
	Mike e jhon são colegas de classe bem como são colegas de trabalho

##### GRAFICOS MULTIPLOS DIRECIONADOS

```
	[1] ----> [3] <--- [5]
	^ |
	| v
	[7]
```

##### TIPOS ESPECIAIS DE ARESTAS

**Auto-aresta:** quando ha uma relação de um vertice para si mesmo

**HiperAresta:** Quando uma aresta conecta mais de dois vertices

**Ego-centered Network:** Quando há um nó com uma única conexão com diversos nós ao redor

### GRAPH TRAVERSALS

Graph traversal refers to the strategy used visit every vertex and edge in a orderly and efficient manner.

Graphs can be visited in a Breadth First Search (BFS busca em largura), e Depth-First Search (DFS Busca em profundidade).


#### BFS (TRAVESSIA EM LARGURA)

```algorithm
graphBFS(graph(V,E))
	visited = set()
	queue = [graph.vertex[0]]

	while(queue)
		node = queue.pop(0)
		visited.append(node)
		neighbours = graph[node]

		for neighbour in neighbours:
			queue.append(neighbour)

	return visited
```

#### DFS (TRAVESSIA EM PROFUNDIDADE)

Em um busca em profundiadade, primeiro percorre-se as arestas
a explorando os primeiros vertices adjacentes o maximo possivel

```algorithm
graphDFS(graph, start, visited=None)
	if visited is None?
		visited = set()
	visited.add(start)
	print(start)
	for nextVertex in graph[start] - visited:
		graphDFS(graph, nextVertex, visited)

	return visited
```

## ALGORIMOS DE LARGA-ESCALA

Desenhados para resolver problemas gigantes. Sua principal caracteristica é a presença de mais de uma engrenagem de execução devido a escala de seus dados e processamento.

Neste capitulo objetivamos discutir quais algoritmos são melhor indicados para executar em paralelo.

### INTRO: DEFININDO UM ALGORITMO DE LARGA ESCALA BEM DESENHADO

Tem as seguintes duas características:
1.	É capaz de lidar com grandes quantidades de dados e processar requisições com uma quantidade limitada de recursos.

2.	É escalável. Capaz de lidar com problemas mais complexos conforme mais recursos é provido.

**Terminologia**

Latencia: tempo decorrido para executar uma opeção de computação. Tfinal-Tinicial

Rendimento: Número de operações que podem ser realizadas simultaneamente. Por exemplo, se em T1 computamos 4 operações, então o rendimento é 4.

### LARGURA DE BISEÇÃO DE REDE

A banda entre duas partes iguais de uma rede. O parametro mais importante para sistemas distribuidos funcionar corretamente. Sem largura de biseção de rede suficiente, os ganhos obtidos com diferentes engines de processamento serão perdidos.

### ELASTICIDADE

A capacidade da infraestrutura reagir a picos repentinos de demanda de processamento através do aprovisionamento/reserva de mais recursos.

## DESENHO DE ALGORITMOS PARALELOS

### LEI DE AMDAHL

Gene Amdahl foi uma das primeiras pessoas a estudar computação paralela por volta de 1960, e cunhou uma lei para explicar as desvantagens da computação em paralelo.











# ENTREVISTA

>> O que é observado na entrevista de código? @https://youtu.be/mjZpZ_wcYFg
	1. Fundamentos da Ciencia da Computaçao
		Estruturas de Dados, Algoritmos
	2. Se voce tem heuristica, um método cientifico para solução de problemas ou apenas
		propoe abordagens aleatórias
	3. Voce escreve código limpo, lógico e mantenível?

>> key principles
	1. Não partir direto para a solução do problema sem olhar para o espaço em que está
	2. Tentar objetivar o problema através de perguntas tentando entender as entradas e saidas, edge cases
	3. Talk out loud


# BIBLIO E REFERENCIAS

[1] método analitico cientifico