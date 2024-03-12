
Imagine a circle with points from [0, 10^18]. Imagine there is a hash function H1, which maps every machineId to a number in [0, 10^18], which you then mark on the circle. Similarly, there is another hash function H which maps userId to [0, 10^18]. 

Let’s assume we assign a user to be present on the first machine in the cyclic order from the hash of the user. 

![](https://lh7-us.googleusercontent.com/6nmoS4MZRozZl3jE6mZbGVth7HqrMpMs2orSjt1DaqRKBfnXUTqLtUE3dba3A5JDd-ONcDEtdXxwFc0BXW7MIJInODDfcdQZU0YJo0FTuA7pTeWCVKAF7v_hYWurVB-ogkx6pWzC8zChmUrEsGIgc-A)

  
  

For example, in the diagram above, Deyan and Affrica are assigned to Node 2, Freddie and Srushtika on Node 5 and so on. 

In implementation, if you have a sorted array with hashes of nodes, then for every user, you calculate the hash, and then binary search for the first number bigger than the given hash. That machine is what the user will be assigned to. 

However, this design suffers from an issue. What happens when you remove a shard. Let’s say Node 2 is down. All load of Node 2 (Deyan + Africa) get assigned to Node 5 and Node5’s load basically doubles. At such high load, there is a good probability that Node 5 dies which will triple the load for Node 4. Node4 can also die and it will trigger cascading failure. 

So, we modify the consistent hashing a little bit. Instead of one hash per machine, you use multiple hashing functions per machine (the more, the better). So, Node 1 is present at multiple places, Node 2 at multiple places and so forth. 

  

![](https://lh7-us.googleusercontent.com/DtAkV-qMg7a2qlCxCF-Hn8kupbf3vh5lSDY4zfzhep6NvaJJVsw2tbVCcTbhNdlAoeYpfnzAZFwW122m3ejty4iOB3GRtLvz2Em8tWjXPbeiw3c7wQEtow4n3DXcH6p6czDah0uX_ToMCWVzNUCeGBs)

  

In the above example, if node A dies, some range of users is assigned to B, some to D and some to C. That is the ideal behaviour.
