### Remove All Adjacent Duplicates In String

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

**Notes**
-> Do check out it's medium Variant in LeetCode.

**Approach**

Consider an example string abba.
When we remove the “bb”, the remaining string is “aa” which has to be removed as well.
So we need to keep track of the characters before the first occurrence of similar consecutive characters.
We can do this using a stack.
We keep pushing the characters in a stack, if the current character is equal to the top of the stack,
we pop from the stack since they represent
a pair of similar characters.
Finally, we print the stack in reverse.

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
