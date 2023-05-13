# https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#


def graphColoring(graph, k, V):
    
    color_array = [0 for i in range(V)]
    
    return helper(graph,V,k,0,color_array)

def helper(graph,n,m,vertex,color_array):
    
    if vertex == n : # if we have colored all vertices then return True
        return True
    
    for i in range(1,m+1):
        if IsSafe(graph,vertex,color_array,i):
            color_array[vertex] = i
            
            if helper(graph,n,m,vertex+1,color_array):
                return True
            else:
                color_array[vertex] = 0
    
    return False # we tried with all colors available but could not
                 # fill all the vertices


def IsSafe(graph,vertex,color_array,color):
    
    for i in range(len(graph[vertex])):
        
        if graph[vertex][i] == 1 and color_array[i] == color:
            return False
    
    return True # we checked all neighbors but  None of them have the 
                # same color as that of current vertex.