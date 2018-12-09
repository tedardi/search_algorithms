'''
Este algoritmo de busca em profundidade foi baseado no codigo da seguinte referencia:
	EDD MANN. Depth-First Search and Breadth-First Search in Python. Disponível em:
	<http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/>
	Acesso em: 15 abr 2018.

'''

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(grafo, vi, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(vi)
    print(vi)
    for next in grafo[vi] - visitado:
        dfs(grafo, next, visitado)
    return visitado


if __name__ == "__main__":

	grafo_1 = graph
	dfs(grafo_1, 'C') # {'E', 'D', 'F', 'A', 'C', 'B'}