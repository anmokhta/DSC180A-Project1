# TEST DATA
# Creates Random Generated Graph with single clique
# ---------------------------------------------------------
# N = total number of nodes in graph (default 75)
# Cn = number of nodes in clique (default 12)
# Cp = probability node in clique is connected to other node in clique (default 0.35)
# Op = probability node NOT in clique is connected to other node NOT in clique (default 0.1)
# q = probability node in clique is connected to other node NOT in clique (default 0.1)
# s = seed for reproducibility (default 3)
# clique = graph of clique nodes and edges
# outer = graph of outer nodes and edges
# combined = combined graph of clique and edges (with random edges base on q)
# clique_nodes = ground_truth list of clique nodes
# outer_nodes = ground_truth list of outer nodes


# TODO: ADD FILENAMES TO JSON CONFIG; LOOK AT OTHER ETL CONFIGS TO COMPARE

from random import random
from random import seed
import pandas as pd
import networkx as nx
import numpy as np
from itertools import product
import pickle
import json
import os


def create_rand_graphs(N, Cn, Cp, Op, q, s, temp_dir, data_dir):
    # check if the files already exist
    if os.path.exists(data_dir + 'cliq_graph.pickle'):
        # delete existing clique graph
        os.remove(data_dir + 'cliq_graph.pickle')
        
    if os.path.exists(data_dir + 'out_graph.pickle'):
        # delete existing graph
        os.remove(data_dir + 'out_graph.pickle')
        
    # make clique
    cliq_graph = nx.gnp_random_graph(Cn, Cp, seed=s) # red
    # make outside of clique
    out_graph = nx.gnp_random_graph(N-Cn, Op, seed=s) # blue

    # save seperate graphs as files



    nx.write_gpickle(cliq_graph, data_dir + 'cliq_graph.pickle')
    print(data_dir + 'cliq_graph.pickle saved!' )
    nx.write_gpickle(out_graph, data_dir + 'out_graph.pickle')
    print(data_dir + 'out_graph.pickle saved!' )






def create_combined(N, Cn, Cp, Op, q, s, temp_dir, data_dir):
    # load in seperate graphs
    clique = nx.read_gpickle(data_dir + 'cliq_graph.pickle')
    outer = nx.read_gpickle(data_dir + 'out_graph.pickle')

    nx.set_node_attributes(clique, "value", '1')
    clique_nodes = clique.nodes(data=True)
    
    # rename the outer nodes
    outer_dict_relabel = dict(zip(range(N-Cn), range(Cn, N)))
    nx.relabel_nodes(outer, outer_dict_relabel, False)
    nx.set_node_attributes(outer, "value", '0')
    outer_nodes = outer.nodes(data=True)
    
    # create ground truth JSON
    ground_truths = {
        "clique_nodes": list(clique.nodes()),
        "outer_nodes": list(outer.nodes())
    }
    
    if os.path.exists(temp_dir + 'ground_truth.json'):
        # delete existing graph
        os.remove(temp_dir + 'ground_truth.json')
    
    with open(temp_dir + 'ground_truth.json', "w") as outfile:
        json.dump(ground_truths, outfile)
    print(temp_dir + 'ground_truth.json saved!' )
    
    
    # create and save combined graph
    combined = nx.Graph()
    combined.add_nodes_from(clique_nodes)
    combined.add_edges_from(clique.edges())
    combined.add_nodes_from(outer_nodes)
    combined.add_edges_from(outer.edges())
    
    

    if os.path.exists(data_dir + 'combined_separated.pickle'):
        # delete existing graph
        os.remove(data_dir + 'combined_separated.pickle')
    
    nx.write_gpickle(combined, data_dir + 'combined_separated.pickle')
    print(data_dir + 'combined_separated.pickle saved!' )

    

    





def create_combined_edges(N, Cn, Cp, Op, q, s, temp_dir, data_dir):
    combined = nx.read_gpickle(data_dir + 'combined_separated.pickle')
    
    with open(temp_dir + 'ground_truth.json', "r") as openfile:
        ground_truth = json.load(openfile)
    
    seed(s)
    combined.add_edges_from([ (u, v) for u, v in product(ground_truth['clique_nodes'], ground_truth['outer_nodes']) if random() < q ])
    if os.path.exists(temp_dir + 'combined.pickle'):
        # delete existing graph
        os.remove(temp_dir + 'combined.pickle')
        
    nx.write_gpickle(combined, temp_dir + 'combined.pickle')
    print(temp_dir + 'combined.pickle saved!' )
    

    