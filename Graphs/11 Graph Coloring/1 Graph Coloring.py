def graph_coloring(V) : # V is the number of vertices
    
    result = [-1]*V # result contains the color of ith vertex
    result[0] = 0 # initializing the firsr vertex color to 0
    
    available = [False]*V # making avaiblity of all the vertices False initially 
    
    for i in range(1,V): # since we have colored the first vertex so now we have to color only V-1 vertices.
        
    
        for v in adj[i]: # adj is adjacency list containing all the neighbors of vertex
            if result[i] != -1 :
                available[i] = True  # if vertex is colored already and is neighbor of v then make its availabilty True
            
    for color in range(V): # Finding the lowest color
        if available[color] == False :
            break
    result[v] = color
    
    for i in range(V): # resetting the availability 
        if result[i] != -1:
            available[i] = False
            