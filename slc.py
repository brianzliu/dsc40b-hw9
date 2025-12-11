from dsf import DisjointSetForest
import dsc40graph

def slc(graph, d, k):
    disjoint_set_forest = DisjointSetForest(list(graph.nodes))
    
    num_clusters_count = len(graph.nodes)
    edge_weight_pairs = dict.fromkeys(list(graph.edges))

    for edge in graph.edges:
        edge_weight_pairs[edge] = d(edge)
    
    edge_weight_pairs = sorted(edge_weight_pairs.items(), key=lambda x: x[1])
    for edge, weight in edge_weight_pairs:
        if num_clusters_count == k:
            break
        if disjoint_set_forest.find_set(edge[0]) != disjoint_set_forest.find_set(edge[1]):
            disjoint_set_forest.union(edge[0], edge[1])
            num_clusters_count -= 1

    clusters = {}
    for node in graph.nodes:
        if disjoint_set_forest.find_set(node) not in clusters:
            clusters[disjoint_set_forest.find_set(node)] = [node]
        else:
            clusters[disjoint_set_forest.find_set(node)].append(node)
    
    return frozenset([frozenset(cluster) for cluster in clusters.values()])


if __name__ == '__main__':
    import doctest
    doctest.testmod()