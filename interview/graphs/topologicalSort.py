#brady sucks
''' Topological sorting on a DAG is an ordering of nodes such that if there
is an edge from u to v, then u comes before v. Note that this is not possible
if the graph is not a DAG '''

class Graph:
  def __init__(self, v):
    self.v = v # number of nodes
    self.adj = {} # adjacencylist of nodes

  def addEdge(self, v, w): 
    if v not in self.adj:
      self.adj[v] = [w]
    else:
      self.adj[v].append(w)

  def printGraph(self):
    for k,v in self.adj.iteritems():
      print k,v

  def topologicalSort(self):
    stack = []
    visited = [False for _ in range(self.v)]
    for k,v in self.adj.iteritems(): # must start DFS from each of the nodes
      if visited[k] == False:
        self.topological_helper(k, visited, stack)
    while stack:
      print stack.pop()
  
  def topological_helper(self, v, visited, stack):
    ''' Simple DFS but also put self on stack after visiting all its neighbors'''
    visited[v] = True
    if v in self.adj: # only continue if v is not an end node.
      for w in self.adj[v]:
        if visited[w] == False:
          self.topological_helper(w, visited, stack)
    stack.append(v)
        
  # dfs practice
  def DFS(self, v):
    visited = [False for _ in range(self.v)] #node indexed bool array
    visited[v] = True 
    print v
    self.DFS_helper(v, visited)

  def DFS_helper(self, v, visited): 
    for w in self.adj[v]:
      if visited[w] != True:
        visited[w] = True
        print w
        self.DFS_helper(w, visited)


if __name__ == "__main__":
  g = Graph(6)
  g.addEdge(5,2)
  g.addEdge(5,0)
  g.addEdge(4,0)
  g.addEdge(4,1)
  g.addEdge(2,3)
  g.addEdge(3,1)

  g.topologicalSort()
