'''
    Time Complexity : O(N + M)
    Space Complexity : O(N + M)

    Where 'N' and 'M' denote the number of nodes and the number of edges in the graph.
'''

def printAdjacency(n, m, edges):
    
    graph = [[] for i in range(n)]

    # Creating the graph.
    for i in range(m):

        # Adding adjecent nodes.
        graph[edges[i][0]].append(edges[i][1])
        graph[edges[i][1]].append(edges[i][0])

    # Create an adjacency list of size 'N'.
    adjacencyList = [[] for i in range(n)]

    for i in range(n):
        adjacencyList[i].append(i)

        for j in graph[i]:
            adjacencyList[i].append(j)

    return adjacencyList
