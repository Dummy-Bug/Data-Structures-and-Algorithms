### Problem Description

Write a recursive function that, given a string S, prints the characters of S in reverse order.



Problem Constraints
1 <= |s| <= 1000



Input Format
First line of input contains a string S.



Output Format
Print the character of the string S in reverse order.



Example Input
Input 1:

 scaleracademy
Input 2:

 cool


Example Output
Output 1:

 ymedacarelacs
Output 2:

 looc


Example Explanation
Explanation 1:

 Print the reverse of the string in a single line.
 
 
 ```
 
 def main():

    string = input();
    reverse(string,0);
    return 0

def reverse(string,index):
    
    if index >= len(string) :
        return ;
    
    reverse(string,index+1);
    print(string[index],end='');
    
if __name__ == '__main__':
    import sys;
    sys.setrecursionlimit(10**7);
    main()

 
 ```
