import numpy as np
import networkx as nx
import pickle
import json
import matplotlib.pyplot as plt

def graph_stats(G):
    deg = []
    for i in G.degree:
        deg.append(i[1])

    stats = {
        'nodes': G.order(),
        'edges': G.number_of_edges(),
        'weights': G.size(),
        'avg_degree': sum(deg) / len(deg)
    }
    
    return stats

def return_sub_graphs(G):
    sub_graphs = {0:[], 1:[]}
    for i in G.nodes:
        G.subgraph(i)
        sub_graphs[G.nodes[i]['value']].append(i)

    for i in sub_graphs:
        sub_graphs[i] = G.subgraph(sub_graphs[i])
    return sub_graphs




def spectral_cluster(G):
    A = nx.to_numpy_array(G)
    D = np.diag(A.sum(axis=1))
    # graph laplacian
    L = D-A
    # eigenvalues and eigenvectors
    vals, vecs = np.linalg.eig(L)
    # sort these based on the eigenvalues
    vecs = vecs[:,np.argsort(vals)]
    vals = vals[np.argsort(vals)]
    print("prediction completed!")
    return [1 if i > 0 else 0 for i in vals]


def spectral_evaluation(G):
    print("evaluation starting")
    pred_list = spectral_cluster(G)
    # Returns accuracy
    evaluate1 = []
    evaluate2 = []
    pred_dict = {0: [], 1: []}
    index = 0
    for i in list(G.nodes(data = True)):
        evaluate1.append(pred_list[index] == i[1]['value'])
        evaluate2.append(pred_list[index] != i[1]['value'])
        pred_dict[i[1]['value']].append(i[1]['label'])
        index += 1

    vals = {
        'predictions': pred_dict,
        'accuracy': max(sum(evaluate1)/len(evaluate1), sum(evaluate2)/len(evaluate2))
    }
    return vals




def create_original_data(graph, file_name):
    #initialze Figure
    plt.figure(num=None, figsize=(50, 50), dpi=100)
    plt.axis('off')
    fig = plt.figure(1)
    pos = nx.spring_layout(graph, seed=22)
    nx.draw_networkx_nodes(graph,pos)
    nx.draw_networkx_edges(graph,pos, alpha=0.5)
    nx.draw_networkx_labels(graph,pos)
    with open(file_name, 'w') as fp:
        pass
    plt.savefig(file_name,bbox_inches="tight")
    del fig

def save_ground_truth_graph(G, ground_truth_filename, file_name):
    plt.figure(num=None, figsize=(50, 50), dpi=100)
    plt.axis('off')
    fig = plt.figure(1)

    with open(ground_truth_filename, 'r') as openfile:
        ground_truth = json.load(openfile)

    pos = nx.spring_layout(G, seed=22)
   
    nx.draw_networkx_nodes(G, pos=pos, nodelist=ground_truth['1'], node_color='r', node_size=50)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=ground_truth['0'], node_color='b', node_size=50)
    nx.draw_networkx_edges(G, pos=pos)

    with open(file_name, 'w') as fp:
        pass
    plt.savefig(file_name,bbox_inches="tight")
    del fig

def save_prediction_graph(G, labels, file_name):
    plt.figure(num=None, figsize=(50, 50), dpi=100)
    plt.axis('off')
    fig = plt.figure(1)

    pos = nx.spring_layout(G, seed=22)
   
    nx.draw_networkx_nodes(G, pos=pos, nodelist=labels[1], node_color='r', node_size=50)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=labels[0], node_color='b', node_size=50)
    nx.draw_networkx_edges(G, pos=pos)

    with open(file_name, 'w') as fp:
        pass
    plt.savefig(file_name,bbox_inches="tight")
    del fig