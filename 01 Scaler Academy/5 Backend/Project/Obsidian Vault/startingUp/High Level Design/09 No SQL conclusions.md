https://docs.google.com/document/d/1PfCmn-rhCJEyWyWf45VtIUFRHyoqiwFyp5o2TCcrZnE/edit

**Tunable Consistency :-** if we do parameter tuning we can make Cassandra Consistent or Available.
![[Pasted image 20240201115856.png]]
when we use some DB with our application then we have following bottleneck 

* size of the data.
* number of queries.  

Thus we need to shard it , so after sharding data would be present on different machines, so where does the code(consistent hashing) resides that decides in which machine my data is present.
* LB and API gateway are not the solution because they are present between user and application server but here we are talking about application server and database machines.

SQL DBs do not support Sharding then we would have to ourself support sharding. Thus we can write that code in application server itself, but there would be many application servers.

if number of incoming queries are high then we need to increase the number of database machines.
* remember Shards store different data but replicas store same data 
![[Pasted image 20240201120801.png]]
This manager is called orchestrator e.g Kubernetes.So whenever an application server has to execute a query it will ask orchestrator to which database we should give this query.
so we were able to make our SQL DB work like No SQL DB using orchestrator.
![[Pasted image 20240201121514.png]]

if a machine is not able to handle all the data then manager needs to add a new machine and say if it adds it right away then the query to data X now would goto the new machine in yellow color but it was present in D1 and yellow machine will say data X is not present.
are we getting a response ? yes :- hence systems is available
are we getting a correct response ? No :- hence non consistent
 ![[Pasted image 20240201122149.png]]
 So natural solution is to first copy some  data to new Shard from D1 and D2.
![[Pasted image 20240201122705.png]]even during the staging time new read queries and write queries can come, 
**READ :-** Old shards should handle READ queries because data transfer is not completed yet.
**Write :-** 
* if we write to new Shard and immediately after read request comes to the same write then old shard won't be able to give the value.
* if we write to old then once the new shard is live then we would have to copy the new data in old shard to new shard.and till that data is not copied our reads can be inconsistent because new shard is live now hence read would happen from new shard only and new data was not copied yet from old shard hence inconsistency occurs.

![[Pasted image 20240201123500.png]]
we do sharding when our system is already overloaded with requests and even sharding in itself is complex time taking process adding additional overhead that may impact system's process.

![[Pasted image 20240201124222.png]]
while deleting a shard as well we would have to face problem of Availability and Consistency.
for a database typically the load does not reduce because the data is always increasing say Instagram as an example , it's data will always increase the only reason for a Shard deletion most of the time is because machine of that particular Shard has died.
![[Pasted image 20240201124807.png]]
promotion algorithms would take some time to elect one of the slaves(replicas) as master and in meantime
**READ :-** can be done from the replicas but what about writes ?

**Write :-** write to all replicas in this case consistency would be there but system would be slow but if one of the replicas is also down then we would have to wait till that replica is available hence suffers from Availability.
![[Pasted image 20240201125546.png]]

SPOF(single point of failure)
load has increases means number of queries have increased.

![[Pasted image 20240201130101.png]]
* Now we have X owners of a key so no need of replicas because anyways data is being written at multiple places.
* earlier say machine D1 used to store d amount of data a will now has to store X * d amount of data.so we need to have bigger machines, but is there a way to keep same size machines ?
![[Pasted image 20240201204719.png]]
* we can do that by increasing the number of shards, say earlier we had 4 shards of d size each but because of multiMaster X=3 we need to have 3 times the data d * 3 but instead of increasing size we can increase number of shards to n.

![[Pasted image 20240201204820.png]]![[Pasted image 20240201205807.png]]
* So no problem while deleting a shard.

![[Pasted image 20240201205837.png]]

**Adding a Shard :-** Always consistent because while adding a Shard data will always be present on the one of the Shards.

![[Pasted image 20240201210138.png]]

* In multi master we can chose how much consistent and available we want 

![[Pasted image 20240201210422.png]]

out of 5(x) masters read from masters till 2(R) of them have same value if yes then return and write to only one of the master machine and later asynchronously sync the data.
![[Pasted image 20240201210952.png]]

* In 2nd case say we read from 3,4(R = 2) but the value is different in both the machines so we would have to read from one more machine because value was different if it reads from 2 then it will return the correct value so consistent with higher latency but if it reads value from 5 then it is available with higher latency.

* In 3rd case if we read from 1,2,3,4 then we will return 1 as the answer but it should be 3 , hence not consistent.

![[Pasted image 20240201211805.png]]
* we can never get inconsistent data in 4th case, but it is not available as 5 machines with same values are not present, hence it will say some error has happened.
* |R| = 4 does not just means read from 4 machines rather it means read from machines till you have 4 machines returning the same data.

Thus in normal master slave architecture performance of write was suffering but here in multi master architecture if we want fast writes we will set the value |w| very less |R| value to high so that our |R| + |W| > |X| ;

and if we want fast reads then less |R| and big |W| ;

![[Pasted image 20240201232806.png]]

![[Pasted image 20240201233101.png]]