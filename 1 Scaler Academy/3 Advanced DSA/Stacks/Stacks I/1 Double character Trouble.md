### Remove All Adjacent Duplicates In String

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

**Notes**
-> Do check out it's medium Variant in LeetCode.

```

from collections import deque;

class Solution:

    def solve(self, A):

        stack = deque([]);

        for char in A:

            if len(stack) == 0 :
                stack.append(char);
            elif stack[-1] != char:

                stack.append(char);
            else:
                stack.pop();
        return "".join(stack);
   
   ```
