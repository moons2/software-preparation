
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

