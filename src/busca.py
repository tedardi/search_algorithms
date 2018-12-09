'''
Neste arquivo estão implentados os algoritmos de:
        * Inicializacao de grafo conforme a bibliotece networkx
        * Busca em profundidade no terminal
        * Busca em profundidade com impressao na tela
'''

import networkx as nx # graph library
import matplotlib.pyplot as plt # matlab plot library
import numpy as np # array manipulation
import matplotlib.colors as colors # For color mapping
import matplotlib.cm as cmx # For color mapping



def inicializaGrafo():
     # Estrutura de dados
    G=nx.Graph()

    # Nos
    G.add_node('1');
    G.add_node('2');
    G.add_node('3');
    G.add_node('4');
    G.add_node('5');
    G.add_node('6');
    G.add_node('7');
    G.add_node('8');
    G.add_node('9');
    G.add_node('10');
    G.add_node('11');
    G.add_node('12');
    G.add_node('13');
    G.add_node('14');
    G.add_node('15');

   
    G.add_edges_from([('1', '2'), ('1', '3')], weight=1)
    G.add_edges_from([('2', '4'), ('2', '5')], weight=1)
    G.add_edges_from([('3', '6'), ('3', '7')], weight=1)
    G.add_edges_from([('4', '8'), ('4', '9')], weight=1)
    G.add_edges_from([('5', '10'), ('5', '11')], weight=1)
    G.add_edges_from([('6', '12'), ('6', '13')], weight=1)
    G.add_edges_from([('7', '14'), ('7', '15')], weight=1)
   
    return G

def dfs(graph, start, goal):
    visited = set()
    stack = [start]
    solucao = []

    while stack:
        node = stack.pop()
        solucao.append(node)
        print(node)
        if node not in visited:
            visited.add(node)
            if node == goal:
                print("Nó meta encontrado:", node)
                print(solucao)
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    print("-", neighbor)
                    stack.append(neighbor)
                    
                    

def dfs_plot(graph, start, goal):
    F=nx.Graph()
    color_map = []
    visited = set()
    stack = [start]
    color_map = ["yellow"] 
    while stack:
        node = stack.pop()
        if node not in visited:
            F.add_node(node)
            visited.add(node)
            pos=nx.spring_layout(F)
            nx.draw_networkx(F, node_color = color_map)
            plt.show()
            if node == goal:
                print("Finally, we found! Is node", node)
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    F.add_node(neighbor)
                    F.add_edges_from([(node, neighbor)], weight=1)
                    stack.append(neighbor)
                    

def dfs_iterative(graph, start, goal):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        if  vertex == goal:
                print("Finally, we found! Is node", vertex)
                return path
        for neighbor in graph[  vertex]:
            stack.append(neighbor)

    return path


if __name__ == "__main__":
    G = inicializaGrafo()
    dfs(G, '1', '12')
    #dfs_plot(G, '1', '12')
    #path = dfs_iterative(G, '1', '12')
    #print(path)
