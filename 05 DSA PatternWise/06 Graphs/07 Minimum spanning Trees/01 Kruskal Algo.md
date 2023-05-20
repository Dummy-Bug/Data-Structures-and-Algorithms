https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1

### Problem Description 

Given a weighted, undirected and connected graph of V vertices and E edges. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.

 

Example 1:

Input:
3 3
0 1 5
1 2 3
0 2 1

Output:
4
Explanation:

The Spanning Tree resulting in a weight
of 4 is shown above.
Example 2:

Input:
2 1
0 1 5

Output:
5
Explanation:
Only one Spanning Tree is possible
which has a weight of 5.
 

Your task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function  spanningTree() which takes number of 
vertices V and an adjacency matrix adj as input parameters and returns an integer denoting the sum of weights of the edges of the Minimum Spanning Tree. 
Here adj[i] contains a list of lists containing two integers where the first integer a[i][0] denotes that there is an edge between i and a[i][0][0] and 
second integer a[i][0][1] denotes that the distance between edge i and a[i][0][0] is a[i][0][1].

In other words , adj[i][j] is of form  { u , wt } . So,this denotes that i th node is connected to u th node with  edge weight equal to wt.

 

Expected Time Complexity: O(ElogV).
Expected Auxiliary Space: O(V2).
 

Constraints:
2 ≤ V ≤ 1000
V-1 ≤ E ≤ (V*(V-1))/2
1 ≤ w ≤ 1000
Graph is connected and doesn't contain self loops & multiple edges.


```

def kruskal_algo(self,V): # V is the number of vertices
    # graph is list of lists containing all the edges: [source,destination,weight] 
    self.graph = sorted(self.graph,key= lambda x:x[2])
    
    parent = [i for i in range(V)]
    rank   = [1 for i in range(V)] # every set will have atleast one node in it.
    i, e = 0, 0
    result = []
    while e < V-1:
        u, v, w = self.graph[i]
        i = i + 1
        
        x = self.find_parent(parent,u)
        y = self.find_parent(parent,v)
        
        # if including this edge is not creating cycle then add it to the tree.
        
        if x != y:
            result.append([u,v,w])
            e = e + 1
            self.union(x,y,parent,rank)
    return result 


def find_parent(self,parent,i):
    if parent[i] == i:
        return i
    parent[i] = self.find_parent(parent,parent[i])
    return parent[i]

def union(u,v,parent,rank):
    
    s1 = find_parent(parent,u)
    s2 = find_parent(parent,v)
    
    if rank[s1] < rank[s2]:
        parent[s1] = s2
        rank[s1]   = rank[s1] + rank[s2]
    else:
        parent[s2] = s1
        rank[s1]   = rank[s1] + rank[s2]



```


```



class Solution{
    public static int findParent(int vertex,int [] parentArr){
        if (parentArr[vertex] != vertex){
            parentArr[vertex] = findParent(parentArr[vertex],parentArr);
        }
        return parentArr[vertex];
    }
    
    public static void findUnion(int parentX, int parentY,int []rank,int [] parent){
        
        if (rank[parentX]<rank[parentY]){
            parent[parentX] = parentY;
        }
        else if(rank[parentX]>rank[parentY]){
            parent[parentY] = parentX;
        }
        else{
            parent[parentX] = parentY;
            rank[parentY]  += 1;
        }
        
    }
	static int spanningTree(int V, int E, int edges[][]){
	    
	    int [] parentArr = new int[V];
	    int [] rank      = new int[V];
	    
	    for(int i = 0; i< parentArr.length;i++){
	        parentArr[i] = i;
	        rank[i] = 1;
	    }
	    
	    Arrays.sort(edges,new Comparator<int[]>(){
	        public int compare(int [] a, int [] b){
	            return a[2]-b[2];
	        }
	    });

	    int currSum   = 0; int currIndex = 0;
	    int currEdges = 0;
	    
	    while (currEdges < V-1){
	        
	        int x = edges[currIndex][0];
	        int y = edges[currIndex][1];
	        
	        int parentX = findParent(x,parentArr);
	        int parentY = findParent(y,parentArr);
	        
	        if (parentX != parentY){
	            currEdges += 1;
	            currSum += edges[currIndex][2];
	            findUnion(parentX,parentY,rank,parentArr);
	        }
	        currIndex += 1;
	    }
	    return currSum;
	}
	
}

```
