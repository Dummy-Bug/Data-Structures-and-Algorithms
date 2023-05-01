### Problem Description

Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls.

1 represents a wall in a matrix and 0 represents an empty location in a wall.

There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall (maze boundary is also considered as a wall). When the ball stops, it could choose the next direction.

Given two array of integers of size B and C of size 2 denoting the starting and destination position of the ball.

Find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the starting position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.



Problem Constraints
2 <= N, M <= 100

0 <= A[i] <= 1

0 <= B[i][0], C[i][0] < N

0 <= B[i][1], C[i][1] < M



Input Format
The first argument given is the integer matrix A.

The second argument given is an array of integer B.

The third argument if an array of integer C.



Output Format
Return a single integer, the minimum distance required to reach destination



Example Input
Input 1:

A = [ [0, 0], [0, 0] ]
B = [0, 0]
C = [0, 1]
Input 2:

A = [ [0, 0], [0, 1] ]
B = [0, 0]
C = [0, 1]


Example Output
Output 1:

 1
Output 2:

 1


Example Explanation
Explanation 1:

 Go directly from start to destination in distance 1.
Explanation 2:

 Go directly from start to destination in distance 1.
 
 **Solution Approach**
 
   We can definitely say that ball will roll only in one of 4 directions, this gives us only 4 options for each place.
  This points towards a BFS based solution. This can be written easily using starting point as source and running bfs until
  queue gets empty or we reach our destiniation.
  
  
  *Better solution than Following is possible*
 
 ```
 
 int possibleMoves[][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};


void BFS(vector<vector<int> > &A, vector<int> B, vector<vector<int>> &distance_travelled) {
    queue<pair<int, int>> q;
    q.push({B[0], B[1]});

    while(!q.empty()) {
        pair<int, int> currCell = q.front();
        q.pop();

        for(int i=0; i<4; i++) {
            int X = currCell.first;
            int Y = currCell.second;
            int count = 0;

            while(X >= 0 && X < A.size() && Y >= 0 && Y < A[0].size() && A[X][Y] == 0) {
                X += possibleMoves[i][0];
                Y += possibleMoves[i][1];
                count++;
            }

            X -= possibleMoves[i][0];
            Y -= possibleMoves[i][1];
            count--;

            if(distance_travelled[currCell.first][currCell.second] + count < distance_travelled[X][Y]) {
                distance_travelled[X][Y] = distance_travelled[currCell.first][currCell.second] + count;
                q.push({X, Y});
            }
        }
    }
}


int Solution::solve(vector<vector<int> > &A, vector<int> &B, vector<int> &C) {
    vector<vector<int>> distance_travelled(A.size(), vector<int> (A[0].size(), INT_MAX));

    distance_travelled[B[0]][B[1]] = 0;
   
    BFS(A, B, distance_travelled);

    return (distance_travelled[C[0]][C[1]] == INT_MAX) ? -1 : distance_travelled[C[0]][C[1]];
}
 
 
 ```
