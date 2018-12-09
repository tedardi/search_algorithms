# tutorial: https://www.datacamp.com/community/tutorials/networkx-python-graph-tutorial

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
import itertools
from enthought.mayavi import mlab


def import_data(t):
	edgelist = pd.read_csv(t)
	print(edgelist.head(10))
	return edgelist

def create_graph(data):
	G = nx.graph() #empty graph
	
	for i, elrow in data.iterrows():
    	g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2:].to_dict())
    
if __name__ == "__main__":
	a = import_data('https://gist.githubusercontent.com/brooksandrew/e570c38bcc72a8d102422f2af836513b/raw/89c76b2563dbc0e88384719a35cba0dfc04cd522/edgelist_sleeping_giant.csv')
	b = import_data('https://gist.githubusercontent.com/brooksandrew/f989e10af17fb4c85b11409fea47895b/raw/a3a8da0fa5b094f1ca9d82e1642b384889ae16e8/nodelist_sleeping_giant.csv')
	create_graph(a)