import networkx as nx

data = open('input.txt', 'r').read().strip().split('\n')
graph = nx.Graph()
for line in data:
    u, children = line.split(': ')
    for v in children.split():
        graph.add_edge(u, v)
graph.remove_edges_from(nx.minimum_edge_cut(graph))
ans = 1
for x in nx.connected_components(graph):
    ans *= len(x)
print(ans)

