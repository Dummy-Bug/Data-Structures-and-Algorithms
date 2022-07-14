class Solution:

    def solve(self, A):

        i = 0; setBits = 0;
        mod = 10**9 + 7;

        while (1<<i) <= A:

            group_size = 1<<i;

            total_groups = (A+1)//group_size;

            setBits = (setBits + (total_groups//2)*(group_size))%mod;

            if total_groups%2 != 0:
                setBits = (setBits + (A+1)%(group_size))%mod;
            i = i + 1;
        
        return setBits;
        