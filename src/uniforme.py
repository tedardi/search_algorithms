'''
Neste arquivo estão implentados os algoritmos de:
        * Inicializacao de grafo conforme a bibliotece networkx
        * Busca em uniforme no terminal

Referência:
<http://cyluun.github.io/blog/uninformed-search-algorithms-in-python>
'''

import networkx as nx # graph library
import matplotlib.pyplot as plt # matlab plot library
import numpy as np # array manipulation
import matplotlib.colors as colors # For color mapping
import matplotlib.cm as cmx # For color mapping
import queue as Q
 
def inicializaGrafo():
    # Estrutura de dados
    G=nx.Graph()

    # Nos
    G.add_node('A');
    G.add_node('B');
    G.add_node('C');
    G.add_node('D');
    G.add_node('E');
    G.add_node('F');
    G.add_node('G');
    G.add_node('G');
       
    G.add_edges_from([('A', 'B')], weight=75)
    G.add_edges_from([('A', 'C')], weight=170)
    G.add_edges_from([('A', 'D')], weight=118)
    G.add_edges_from([('B', 'E')], weight=71)
    G.add_edges_from([('B', 'F')], weight=75)
    G.add_edges_from([('D', 'G')], weight=99)
    G.add_edges_from([('D', 'H')], weight=111)
      
    return G


def uniforme(graph, start, goal):
    
    visited = set()
    q = Q.PriorityQueue()
    q.put((0, start))
   
    while q:
        cost, node = q.get()
        print("visitei:", node)
        if node not in visited:
            visited.add(node)
            if node == goal:
                print("Finally, we found! Is node", node)
                return           
            for neighbor in graph[node]:
                if neighbor not in visited:
                    total_cost = cost + graph[node][neighbor]['weight']
                    print(".......", neighbor, total_cost)
                    q.put((total_cost, neighbor))
                   
 

if __name__ == "__main__":
    G = inicializaGrafo()
    uniforme(G, 'A', 'E')
    