https://leetcode.com/problems/keys-and-rooms/

### There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

 

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
 

Constraints:

n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.


```

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]):
        
        n = len(rooms)
        self.visited = [False for j in range(n)]
        
        return self.bfs(rooms,0,n)
    
    def bfs(self,rooms,u,n):
        
        from collections import deque
        q = deque()
        
        self.count = 1
        q.append(u)
        
        while q:
            u = q.popleft()
            
            for v in rooms[u]:
                
                if self.visited[v] == False:
                    self.count += 1
                    q.append(v)
                    
            self.visited[u] = True      
            
        return self.count == n
    
    ```
    
    
    ```
    
    import java.util.Queue;
import java.util.LinkedList;

class Solution {

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {

     boolean [] visited = new boolean[rooms.size()];
     Queue<Integer> queue = new LinkedList<Integer>();

     return helper(rooms,visited,queue);
    }

    public boolean helper(List<List<Integer>> rooms,boolean[] visited,Queue<Integer>queue){
        visited[0] = true;
        queue.add(0);

        while(!queue.isEmpty()){
            int room = queue.remove();

            for (int i = 0; i < rooms.get(room).size(); i++) {
                int key = rooms.get(room).get(i);
                if (!visited[key]) {
                    queue.add(key);
                    visited[key] = true;
                    }
            }

        }
        for(boolean visit:visited){
            if (visit == false){
                return false;
            }
        }
        return true;
    }

}
    
    ```
