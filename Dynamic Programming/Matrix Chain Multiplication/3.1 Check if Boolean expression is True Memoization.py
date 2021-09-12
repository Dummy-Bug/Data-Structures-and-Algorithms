class Solution:
 
    def countWays(self, N, S):
 
        self.dp = []
 
        for i in range(N+1):
            lst = [[-1 for k in range(2)] for j in range(N+1)]
            self.dp.append(lst)
 
        return self.helper(S,0,N-1,1) # if we want number of ways that are true.
 
    def helper(self,s,i,j,isTrue):
 
        if i > j :
            return 0
 
        elif i == j:
 
            if isTrue == 1:
                if s[i] == 'T':
                    return 1
                else:
                    return 0
 
            else:
                if s[i] == 'F':
                    return 1
                else:
                    return 0
 
        if self.dp[i][j][isTrue] != -1 :
            return self.dp[i][j][isTrue]
 
        ans = 0
        for k in range(i+1,j,2):
 
            lt = self.helper(s,i,k-1,1)# number of ways of making left equation True
            lf = self.helper(s,i,k-1,0)
            rt = self.helper(s,k+1,j,1)
            rf = self.helper(s,k+1,j,0)# number of ways of making right expression False
 
            if s[k] == '|': 
 
                if isTrue: 
                    ans = (ans + lt*rf + lf*rt + lt*rt)%1003
 
                else:
                    ans = (ans + lf*rf)%1003 
 
            elif s[k] == '^':
 
                if isTrue:
                    ans = (ans + lt*rf + lf*rt)%1003
 
                else:
                    ans = (ans +  lf*rf + lt*rt)%1003
 
            else:
 
                if isTrue:
                    ans = (ans + lt*rt)%1003
 
                else:
                    ans = (ans + lt*rf + lf*rt + lf*rf)%1003
 
        self.dp[i][j][isTrue] = ans%1003
 
        return self.dp[i][j][isTrue]