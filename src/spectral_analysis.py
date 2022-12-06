import numpy as np
import networkx as nx
import pickle
import json
import matplotlib as plt

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
    return [1 if i > 0 else 0 for i in vals]


def prediction_evaluation(G, pred_list):
    # Returns accuracy
    evaluate1 = []
    evaluate2 = []
    index = 0
    for i in list(G.nodes(data = True)):
        evaluate1.append(pred_list[index] == i[1]['value'])
        evaluate2.append(pred_list[index] != i[1]['value'])
        index += 1

    return max(sum(evaluate1)/len(evaluate1), sum(evaluate2)/len(evaluate2))

def spectral_evaluation(G):
    preds = spectral_cluster(G)
    vals = {
        'predictions': spectral_cluster(G),
        'accuracy': prediction_evaluation(G, preds)
    }
    return vals