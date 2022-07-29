'''

			   ___  A  ____
			  /     |      \
			B 		C 		D
			|
			E
			|
			F


graph = {
	'A': {'B', 'C', 'D'},
	'B': {'A', 'E'},
	'C': {'A'},
	'D': {'A'},
	'E': {'B','F'},
	'F': {'E'},
}

graphBFS(graph, 'A')

visited = [A, B, C, D]
queue	= [A, A]
vertex	= [E]
nbours 	= [B, F]

'''


def graphDFS(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	print(start)
	for nextVertex in graph[start]-visited:
		graphDFS(graph, nextVertex, visited)
	return visited


def graphBFS(graph, start):
	visited = []
	queue 	= [start]

	while (queue):
		vertex = queue.pop(0)

		if vertex not in visited:
			visited.append(vertex)
			neighbours = graph[vertex]
			
			for neighbour in neighbours:
				queue.append(neighbour)

	print(visited)

if __name__ == '__main__':
	graph = {
	'A': {'B', 'C', 'D'},
	'B': {'A', 'E'},
	'C': {'A'},
	'D': {'A'},
	'E': {'B','F'},
	'F': {'E'},
	}

	graphDFS(graph, 'A')