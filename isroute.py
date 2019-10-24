#given a directed graph, design a function to determine if there is a path between two nodes
def BFS(root,end,graph):
  nodeq = []
  visited = []
  nodeq.append(root)
  visited.append(root)
  while nodeq != []:
    n = nodeq.pop(0)
    if n == end:
      return True
    for child in graph[n]:
      if child not in visited:
        visited.append(child)
        nodeq.append(child)
  return False
    

def ispath(start,end,connections):
  graph = {}
  for c in connections:
    if c[0] not in graph:
      graph[c[0]] = [c[1]]
    else:
      graph[c[0]] += [c[1]]
    if c[1] not in graph:
      graph[c[1]] = []
  if start not in graph.keys():
    return False
  else:
    return BFS(start,end,graph)

connections = [[1,2],[3,4],[4,5],[4,6],[6,7]]

print(ispath(3,7,connections))
