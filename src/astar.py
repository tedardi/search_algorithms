import networkx as nx # graph library
import matplotlib.pyplot as plt # matlab plot library
import numpy as np # array manipulation
import matplotlib.colors as colors # For color mapping
import matplotlib.cm as cmx # For color mapping
import queue as Q
import pandas as pd

def inicializaGrafo():
    # Estrutura de dados
    G=nx.Graph()

    # Nos
    G.add_node('Arad');
    G.add_node('Bucarest');
    G.add_node('Craiova');
    G.add_node('Dobreta');
    G.add_node('Eforie');
    G.add_node('Fagaras');
    G.add_node('Giurgiu');
    G.add_node('Hirsova');
    G.add_node('Iasi');
    G.add_node('Lugoj');
    G.add_node('Mehadia');
    G.add_node('Neamt');
    G.add_node('Oradea');
    G.add_node('Pitesti');
    G.add_node('Arad');
    G.add_node('Rimnieu');
    G.add_node('Sibiu');
    G.add_node('Timisoara');
    G.add_node('Urziceni');
    G.add_node('Vaslui');
    G.add_node('Zerind');              


    G.add_edges_from([('Arad', 'Zerind')], weight=75)
    G.add_edges_from([('Arad', 'Timisoara')], weight=118)
    G.add_edges_from([('Arad', 'Sibiu')], weight=140)
    G.add_edges_from([('Zerind', 'Oradea')], weight=71)
    G.add_edges_from([('Timisoara', 'Lugoj')], weight=70)
    G.add_edges_from([('Sibiu', 'Oradea')], weight=151)
    G.add_edges_from([('Sibiu', 'Fagaras')], weight=99)
    G.add_edges_from([('Sibiu', 'Rimnieu')], weight=80)
    G.add_edges_from([('Lugoj', 'Mehadia')], weight=70)
    G.add_edges_from([('Mehadia', 'Dobreta')], weight=75)
    G.add_edges_from([('Dobreta', 'Craiova')], weight=120)
    G.add_edges_from([('Craiova', 'Rimnieu')], weight=146)
    G.add_edges_from([('Craiova', 'Pitesti')], weight=138)
    G.add_edges_from([('Pitesti', 'Rimnieu')], weight=97)
    G.add_edges_from([('Fagaras', 'Bucarest')], weight=211)
    G.add_edges_from([('Giurgiu', 'Bucarest')], weight=90)
    G.add_edges_from([('Urziceni', 'Bucarest')], weight=85)
    G.add_edges_from([('Urziceni', 'Hirsova')], weight=98)
    G.add_edges_from([('Urziceni', 'Vaslui')], weight=142)
    G.add_edges_from([('Hirsova', 'Eforie')], weight=86)
    G.add_edges_from([('Vaslui', 'Iasi')], weight=92)
    G.add_edges_from([('Iasi', 'Neamt')], weight=87)
        
    return G

def resultado_heuristica():
	
	hn = {'Arad': 366,
		 'Bucarest': 0,
		 'Craiova':160,
		 'Dobreta':242,
		 'Eforie': 161,
		 'Fagaras':176,
		 'Giurgiu':77,
		 'Hirsova':151,
		 'Iasi': 226,
		 'Lugoj': 244,
		 'Mehadia': 241,
		 'Neamt': 234,
		 'Oradea': 380,
		 'Pitesti': 100,
		 'Rimnieu': 193,
		 'Sibiu': 253,
		 'Timisoara': 329,
		 'Urziceni': 80,
		 'Vaslui': 199,
		 'Zerind':374}
	return hn

def astar(graph, start, goal):
    hn_list = resultado_heuristica()
    visited = set()
    q = Q.PriorityQueue()
    q.put((0, start))
   
    while q:
        cost, node = q.get()
        print("visitei:", node, " | custo:", cost)
        if node not in visited:
            visited.add(node)
            if node == goal:
                print("Finally, we found! Is node", node)
                return           
            for neighbor in graph[node]:
                if neighbor not in visited:
                    gn = cost + graph[node][neighbor]['weight']                   
                    hn = hn_list[neighbor]
                    fn = gn + hn
                    print("....... Fronteira:", neighbor,
                    	" | ida: ", graph[node][neighbor]['weight'], 
                    	" | g(n):", gn, 
                    	" | h(n):", hn,
                    	" | f(n):", fn)
                    q.put((fn, neighbor))
                    gn = 0
                   
 

if __name__ == "__main__":
    G = inicializaGrafo()
    astar(G, 'Arad', 'Bucarest')
    
