def get_data(fp, years, states):
    ....
    return data

# Parameter
# N  = 75
# p1 = 0.5
# p2 = 0.5
# q  = 0.25


def create_rand_graphs(N=75, Cn=12, Cp=0.35, Op=0.1, q=.1, s=3):
    # make clique
    cliq_graph = nx.gnp_random_graph(Cn, Cp, seed=s) # red
    # make outside of clique
    out_graph = nx.gnp_random_graph(N-Cn, Op, seed=s) # blue
    relabel = {}
    return cliq_graph, out_graph

a, b = create_rand_graphs(N=75, Cn=12, Cp=0.35, Op=0.1, q=.1, s=3)
nx.draw(a, with_labels=True)
#nx.draw_networkx()
nx.draw(b, with_labels=True)
def create_combined(N, Cn, clique, outer, q=.1):
    
    clique_nodes = clique.nodes()
    
    # rename the outer nodes
    outer_dict_relabel = dict(zip(range(N-Cn), range(Cn, N)))
    nx.relabel_nodes(outer, outer_dict_relabel, False)
    outer_nodes = outer.nodes()
    
    
    combined = nx.Graph()
    combined.add_nodes_from(clique_nodes)
    combined.add_edges_from(clique.edges())
    combined.add_nodes_from(outer_nodes)
    combined.add_edges_from(outer.edges())
    
    return combined, clique_nodes, outer_nodes

def create_combined_edges(combined, clique_nodes, outer_nodes, q=0.1, s=3):
    seed(s)
    combined.add_edges_from([ (u, v) for u, v in product(clique_nodes, outer_nodes) if random() < q ])
    return combined, clique_nodes, outer_nodes
a, b = create_rand_graphs(N=75, Cn=12, Cp=0.35, Op=0.1, q=.1, s=3)
g, l1, l2 = create_combined(N, Cn, a, b, q=.1)
combined, clique_nodes, outer_nodes = create_combined_edges(g, l1, l2)
# nx.draw(g, with_labels=True)
# nx.draw(, with_labels=True)

def plot_graph(combined, clique_nodes, outer_nodes):
    pos = nx.spring_layout(combined)
    
    nx.draw_networkx_nodes(combined, pos=pos, nodelist=clique_nodes, node_color='r', node_size=50)
    nx.draw_networkx_nodes(combined, pos=pos, nodelist=outer_nodes, node_color='b', node_size=50)
    nx.draw_networkx_edges(combined, pos=pos)
    return plt.show() 
plot_graph(combined, clique_nodes, outer_nodes)