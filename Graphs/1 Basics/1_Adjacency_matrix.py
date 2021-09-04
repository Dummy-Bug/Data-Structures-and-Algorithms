class Graph:
    def __init__(self,size):
        self.adja_matrix = [[0 for j in range(size)] for i in range(size) ]
        print(self.adja_matrix)
        
    def add_edge(self,u,v):
        if u == v :
            return (print("same vertices"))
        if self.adja_matrix[u][v] == 1:
            return (print("Edge Already exist"))
        
        self.adja_matrix[u][v] = 1
        self.adja_matrix[v][u] = 1
        
    def print_Graph(self):
        for row in self.adja_matrix:
            print(row)
        print("--"*20)
    def remove_edge(self,u,v):
        if self.adja_matrix[u][v] == 0:
            return ( print("No edge between the {} and {} v".format(u,v)) )
        self.adja_matrix[u][v] = 0
        self.adja_matrix[v][u] = 0
        
g = Graph(4)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 2)
g.add_edge(2, 3)

g.print_Graph()

g.remove_edge(1,0)
g.remove_edge(0,0)

g.print_Graph()