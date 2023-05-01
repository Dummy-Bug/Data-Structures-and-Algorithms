https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

### Problem Description 

You are given a string s. You need to reverse the string.

Example 1:

Input:
s = Geeks
Output: skeeG
Example 2:

Input:
s = for
Output: rof
Your Task:

You only need to complete the function reverseWord() that takes s as parameter and returns the reversed string.

  Expected Time Complexity: O(|S|).
  Expected Auxiliary Space: O(1).

Constraints:
1 <= |s| <= 10000


```

#User function Template for python3

def reverseWord(s):
    # String are immutable in python
    
    stringList = list(s);
    
    i = 0;j = len(s)-1;
    
    while i<j:
        stringList[i],stringList[j] = stringList[j],stringList[i];
        i += 1;
        j -= 1;
    
    return "".join(stringList);
    
```

**Aliter**

```

def reverseWord(s):
    return s[::-1];

```
