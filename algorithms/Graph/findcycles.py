'''This problem was recently asked by Facebook:

Given an undirected graph, determine if a cycle exists in the graph.

Here is a function signature:

'''


def find_cycle(graphe):
    def dfs(graph, visited):
        for k, v in graph.items():
            if k in visited:
                print(k)
                return True
            visited.add(k)
            if dfs(v, visited):
                return True
            visited.remove(k)
        return False
        
    visited = set()
    return dfs(graphe, visited)

graph = {
  'a': {'a2':{}, 'a3':{} },
  'b': {'b2':{}},
  'c': {}
}

print(find_cycle(graph))
# False
graph['c'] = graph
print(find_cycle(graph))
# True

graph = {
  'a': {'a2':{}, 'a3': {'e':{}} },
  'b': {'b2':{'a3': {}}},
  'c': {}
}
print(find_cycle(graph))
# False
