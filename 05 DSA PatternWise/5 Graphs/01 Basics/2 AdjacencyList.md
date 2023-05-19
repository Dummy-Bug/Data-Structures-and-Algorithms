```

class Node :
    def __init__(self,val):
        self.val  = val
        self.link = None

class Graph :
    def __init__(self,vertices):
        self.v = vertices
        self.list = [None for i in range(self.v)]
        
        
    def add_edge(self,u,v):
        
        new_node = Node(v)
        new_node.next = self.list[u]
        self.list[u] = new_node
        
        new_node = Node(u)
        new_node.next = self.list[v]
        self.list[v] = new_node
    
    def print_list(self):
        for ptr in self.list:
            row = []
            while ptr:
                row.append(ptr.val)
                ptr = ptr.next
            print(row)
            
g = Graph(4)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(0,1)
g.print_list()

```
