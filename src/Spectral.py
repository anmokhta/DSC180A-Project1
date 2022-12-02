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