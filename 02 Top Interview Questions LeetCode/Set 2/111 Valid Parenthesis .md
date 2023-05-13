### Problem Description 

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true


Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


```
class Solution:
    def isValid(self, s: str) -> bool:
        lst = list()
        print(len(s))
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{' :
                lst.append(s[i])
                
            elif s[i] == ')' or s[i] == ']' or s[i] ==  "}":
                if lst == []: 
                    print("Right Parenthesis are MOre: ")
                    return False
                print(lst[-1])
                temp = lst[-1]
                if s[i] == ")" and temp == "(":
                    lst.pop()
                elif s[i] == "]" and temp == "[":
                    lst.pop()
                elif s[i] == "}" and temp == "{":
                    lst.pop()
                else:
                    return False
        # print(len(lst))
        if len(lst) == 0:
            return True
       
        else:
            print("Left Parenthesis are MOre: ")
            return False

```

