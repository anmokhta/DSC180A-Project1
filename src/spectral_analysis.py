import numpy as np
import networkx as nx

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