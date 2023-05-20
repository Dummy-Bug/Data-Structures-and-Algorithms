https://leetcode.com/playground/Hf6noaP7


```

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

```


```


// "static void main" must be defined in a public class.

class Graph{
    int [][] graphMatrix; 
    Graph(int size){
        this.graphMatrix = new int[size][size];
    }
    
    void addEdge(int u,int v){
        if (u==v){
            System.out.println("Self loops are not allowed");
            return;
        }
        this.graphMatrix[u][v] = 1;
        this.graphMatrix[v][u] = 1;
    }
    
    void removeEdge(int u,int v){
        if(this.graphMatrix[u][v] == 0){
            System.out.println("No edge is present");
        }
        this.graphMatrix[u][v] = 0;
    }
    void showGraph(){
        System.out.println(" ");
        for (int i = 0; i < this.graphMatrix.length;i++){
            for(int j = 0;j < this.graphMatrix[0].length;j++){
                System.out.print(" "+ graphMatrix[i][j]);
            }
            System.out.println(" ");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello Graphs!");
        Graph g = new Graph(4);
        g.addEdge(1,2);
        g.addEdge(2,3);
        g.addEdge(0,1);
        g.addEdge(2,0);
        g.showGraph();
        g.removeEdge(2,0);
        g.removeEdge(2,3);
        g.showGraph();
        
    }
}

```
