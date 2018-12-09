'''
Neste arquivo estão implentados os algoritmos de:
        * Inicializacao de grafo conforme a bibliotece networkx
        * Busca em largura no terminal
        * Busca em largura com impressao na tela
'''

import networkx as nx # graph library
import matplotlib.pyplot as plt # matlab plot library
import numpy as np # array manipulation
import matplotlib.colors as colors # For color mapping
import matplotlib.cm as cmx # For color mapping

class Queue:

  #Constructor creates a list
  def __init__(self):
      self.queue = list()

  #Adding elements to queue
  def enqueue(self,data):
      #Checking to avoid duplicate entry (not mandatory)
      if data not in self.queue:
          self.queue.insert(0,data)
          return True
      return False

  #Removing the last element from the queue
  def dequeue(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("Queue Empty!")

  #Getting the size of the queue
  def size(self):
      return len(self.queue)

  #printing the elements of the queue
  def printQueue(self):
      return self.queue


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


def bfs(graph, start, goal):
    visited = set()
    q = Queue()
    q.enqueue(start)
    solucao = []

    while q:
        node = q.dequeue()
        print(node)
        if node not in visited:
            visited.add(node)
            solucao.append(node)

            if node == goal:
                print("Finally, we found! Is node", node)
                print (solucao)
                return
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    print("-", neighbor)
                    q.enqueue(neighbor)
                    #print(q.printQueue())           

  

def bfs_plot(graph, start, goal):
    F=nx.Graph()
    color_map = []
    visited = set()
    q = Queue()
    q.enqueue(start)
    color_map = ["yellow"] 
    
    while q:
        node = q.dequeue()
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
                    q.enqueue(neighbor)

if __name__ == "__main__":
    G = inicializaGrafo()
    bfs(G, '1', '12')
    #bfs_plot(G, '1', '12')
