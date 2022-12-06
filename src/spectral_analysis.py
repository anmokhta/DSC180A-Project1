import numpy as np
import networkx as nx


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

def create_original_data():


def create_prediction_data():


def create_ground_truth_data():



# def plot_graph(combined, clique_nodes, outer_nodes):
#     combined = pickle.load(open('data/test/temp/combined.pickle', 'rb'))
#    
#     with open('data/test/temp/ground_truth.json', 'r') as openfile:
#         ground_truth = json.load(openfile)
#
#   
#     pos = nx.spring_layout(combined)
#    
#     nx.draw_networkx_nodes(combined, pos=pos, nodelist=ground_truth['clique_nodes'], node_color='r', node_size=50)
#     nx.draw_networkx_nodes(combined, pos=pos, nodelist=ground_truth['outer_nodes'], node_color='b', node_size=50)
#     nx.draw_networkx_edges(combined, pos=pos)
#     return plt.show()