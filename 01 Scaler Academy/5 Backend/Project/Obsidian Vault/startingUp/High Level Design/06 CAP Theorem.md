
**Consistency:**

- **Definition:** Consistency, in the context of distributed systems, means that all nodes in the system present the same view of the data at the same time.
- **Strong Consistency:** Systems that prioritize strong consistency ensure that every read receives the most recent write. Strong consistency can be achieved by having all nodes agree on the order of operations.
- **Trade-offs:** Achieving strong consistency often involves coordination and synchronization between nodes, which can lead to increased latency and reduced availability, especially in the face of network partitions.
- **Stale reads:** occur in distributed systems when a read operation retrieves outdated or stale data, meaning the data is not the most recent or has not been updated to reflect the latest changes, so in consistency no matter to which node read call goes to data will always be updated / consistent / latest .

![[Pasted image 20240126105746.png]]

**Availability:**

- **Definition:** Availability refers to the ability of a system to respond to requests, even in the face of failures or partitions.
- **High Availability Systems:** Systems that prioritize availability aim to provide uninterrupted services and responses, even if some nodes in the system fail or become unreachable due to network issues.
- **Trade-offs:** Prioritizing availability may lead to situations where nodes may return responses without having the most up-to-date data. In some cases, this might result in accepting "stale" or outdated information.
- To mitigate the impact of stale reads, systems might implement strategies such as:

- **Read Repair:** After a read, the client might communicate with other nodes to check for more recent versions of the data and update its local cache accordingly.
    
- **Versioning:** Assigning version numbers to data and ensuring that reads only consider versions equal to or greater than a certain threshold helps in identifying and discarding stale data.
    
- **Tunable Consistency:** Some distributed databases allow users to configure the level of consistency on a per-operation basis, allowing developers to choose the appropriate trade-off between consistency and availability for specific use cases.

1. **Question :** what if we have 2 servers A, B and server B is down due to some reason now if request goes to server B , then what would happen to availability ?
	If server B is down, and a request is directed to server B, the availability of the system depends on how the system is designed and how it handles such situations. Here are a few scenarios:

	1. **High Availability Design (AP Systems):**
	    
	    - In systems that prioritize availability (AP systems in the context of the CAP theorem), the goal is to provide responses even in the face of failures or partitions.
	    - If server B is down, the system may still attempt to serve the request by redirecting it to server A or another available node.
	    - The response may be generated based on the most recent data available in the system, even if server B has not yet been updated.
	2. **Fail-Fast Design:**
	    
	    - Some systems are designed to fail fast. If a request is directed to a down server (like server B), the system might immediately return an error or redirect the request to an alternative healthy server.
	    - This approach ensures that the client receives a quick response, and the system doesn't waste time attempting to communicate with a node that is known to be unavailable.
	3. **Retry Mechanism:**
	    
	    - Another approach is to implement a retry mechanism. If a request is initially directed to a down server, the system might have logic to retry the request on another available server.
	    - This can be accompanied by back-off strategies to prevent overwhelming the system with repeated retries.
	4. **Load Balancer Handling:**
	    
	    - In many distributed systems, requests are typically directed through a load balancer. The load balancer can be configured to detect the unavailability of a server and distribute traffic only to healthy nodes.
	    - If server B is down, the load balancer can route requests to server A or other available servers.

	The specific behavior will depend on the design decisions made during the development of the distributed system. In general, systems that prioritize availability will aim to handle failures gracefully, ensuring that users still receive responses even if some nodes are unavailable. However, the exact approach may vary based on the architecture and requirements of the system.

**Partition Tolerance:** Partition tolerance is one of the key properties described in the CAP theorem (Consistency, Availability, and Partition Tolerance). It refers to the ability of a distributed system to continue operating and providing meaningful responses despite the occurrence of *network partitions*. In other words, a system that is partition-tolerant can still function even if some nodes are unable to *communicate* with each other.

In practical terms, partition tolerance ensures that a distributed system remains operational when network partitions happen, *allowing different parts of the system to continue functioning independently*. This is crucial for systems that prioritize high availability and fault tolerance, as they need to be resilient to network failures and ensure that the entire system doesn't come to a halt if communication between nodes is temporarily disrupted.

![[Pasted image 20240126124006.png]]
1. Let's use a simplified example with two nodes representing servers in a distributed system, and we'll consider a scenario involving a network failure with Facebook as an example:

	1. **Nodes in the System:**
	    
	    - Node A: Represents one server in the Facebook distributed system.
	    - Node B: Represents another server in the same distributed system.
	2. **Normal Operation:**
	    
	    - Both Node A and Node B are communicating seamlessly, sharing updates, posts, and user data. The system is fully functional.
	3. **Network Failure Scenario:**
	    
	    - Suddenly, there is a network failure that isolates Node A from Node B. This could be due to a physical issue like a severed network cable, a router failure, or any other network-related problem.
	4. **Impact on Facebook (Partition Tolerance):**
	    
	    - Despite the network failure between Node A and Node B, Facebook's distributed system aims to remain operational.
	    - Users can still access their Facebook profiles, view updates, and interact with the system, even though the communication between Node A and Node B is temporarily disrupted.
	5. **Actions Taken for Partition Tolerance:**
	    
	    - **Load Balancing:** Facebook's infrastructure may utilize load balancing to distribute user requests among multiple servers. If Node A is temporarily unreachable, requests can be redirected to other available nodes.
	    - **Replication:** Important data may be replicated across multiple nodes. Even if one node is unavailable, the replicated data on other nodes ensures that users can still access the information they need.
	6. **Eventual Consistency:**
	    
	    - To maintain availability during network partitions, Facebook may choose to prioritize eventual consistency. This means that even if updates made on Node A are not immediately reflected on Node B, the system guarantees that they will eventually synchronize once the network issue is resolved.
	7. **User Experience:**
	    
	    - Users continue to interact with Facebook, post updates, and view content. The system maintains availability despite the temporary lack of communication between nodes.

The CAP theorem suggests that, in the face of a network partition, a distributed system must make a trade-off between consistency and availability. *A system that prioritizes partition tolerance may choose to sacrifice either consistency (eventual consistency) or availability (limited availability during partitions) to ensure that the system remains operational even in the presence of network disruptions.*
![[Pasted image 20240127174606.png]]user will call @123456789 and internally call will get redirected to either Irfan or Pankti and either of them will add the flight date in their respective registers/databases(not shared)
![[Pasted image 20240127174812.png]]Data Inconsistency cause when user called initially it got picked up by Irfan and now call is picked up by Pankti who has no record of user's flight.

1. what if they both maintain a single diary? then diary(storage) would become bottleneck cause there would be too many writes (write throughput is so high that a single DB can't handle the write). so we have to split it into multiple DBs but when we split we have inconsistency issues.

2. what if user's call always goes to irfan? this is consistent hashing solution but what if Irfan is on vocation then same issue will occur again.

so we need a way of sync up the data
![[Pasted image 20240127175640.png]]![[Pasted image 20240127175928.png]]

![[Pasted image 20240127180046.png]]

**CAP Theorem :**
The CAP theorem states that in a distributed system, it is impossible to achieve all three properties simultaneously. When a network partition occurs (nodes are unable to communicate), a distributed system must choose between maintaining consistency (C) or availability (A). This trade-off is inherent in the design of distributed systems.

The theorem is often visualized as a triangle, where a system can optimize for two out of the three properties but cannot achieve all three at the same time. The three common scenarios in the CAP triangle are:

- **CA (Consistency and Availability):** Systems that prioritize consistency and availability but might not be tolerant to network partitions. Traditional relational databases often fall into this category.
    
- **CP (Consistency and Partition Tolerance):** Systems that prioritize consistency and partition tolerance but might experience temporary unavailability. Some distributed databases use this model.
    
- **AP (Availability and Partition Tolerance):** Systems that prioritize availability and partition tolerance but might sacrifice strong consistency. NoSQL databases, particularly those designed for high availability and fault tolerance, often fall into this category.

in large systems network partitions are inevitable so we are left with choosing either consistency or availability.

![[Pasted image 20240127195307.png]]
in stock exchange both consistency and availability is required but then what about the network partitions as these systems would have to handle so many network requests from users and we know we cannot have all three in one systems(CAP theorem)?

if NSE crashes for two days India is going to loose billion of dollars , it will have massive impact on the GDP if India , so these servers are very very critical yet these servers are not distributed .

Inside Mumbai there is a large building and all the servers of NSE they are sitting inside this building itself connected via very very very fast multiple ethernet cables, so even if one or two cable crashes other can handle the load . Hence in this particular system there scope of partition because there are multiple network connections between any two servers.So this is non distributed system.and since we are guaranteeing that there can be no partitions we can achieve both availability and consistency.Thus stock exchange is an AC system.
![[Pasted image 20240127200410.png]]
C+P is not good for Instagram cause say if some of US servers goes down and all other servers  are still active users won't be able to read or make posts because of the unavailability. because in order to provide the consistency we would have to wait till the servers are up so that data can be synced.

ATMs are A+P systems

![[Pasted image 20240127201638.png]]

![[Pasted image 20240127202025.png]]
1. **Consistency (C):**
    
    - **Example for WhatsApp:** When a user sends a message in WhatsApp, the platform ensures that the message is delivered to all the intended recipients and is consistently visible across devices. For example, if User A sends a message to User B, the message is replicated and stored on the servers in a way that ensures all devices associated with User B will eventually receive and display the message.
        
    - **Example for Slack:** In Slack, when a user posts a message in a channel, the system ensures that the message is visible to all members of that channel consistently. This means that if User X posts a message, all other users in the channel, regardless of their location or the devices they are using, should eventually see the same message.
        
2. **Partition Tolerance (P):**
    
    - **Example for WhatsApp:** Consider a scenario where network partitions occur, temporarily disconnecting some users or groups of users from the main WhatsApp servers. Despite these partitions, WhatsApp aims to ensure that messages sent during the partition are eventually delivered to all recipients once the network is restored. Users might not see the real-time updates during the partition, but the system works to converge to a consistent state.
        
    - **Example for Slack:** In Slack, if there are network partitions causing some teams or users to be temporarily isolated from the central Slack servers, the system continues to accept messages locally. Once the network partitions are resolved, the system works to synchronize and deliver the messages to all users, achieving eventual consistency.
        
3. **Trade-offs:**
    
    - The trade-off made by WhatsApp and Slack is that they prioritize data consistency even if it means that, during network partitions, there might be a delay in delivering messages to all users. This aligns with the principles of CP systems, where consistency is maintained, and the system might experience temporary unavailability during network partitions.
4. **Mitigation Strategies:**
    
    - These platforms likely implement strategies to minimize the impact of network partitions, such as using redundant servers, employing distributed databases, and optimizing communication protocols. Additionally, asynchronous replication and eventual consistency mechanisms help synchronize data across distributed nodes.
![[Pasted image 20240127202118.png]]
*Why does Swiggy process and accept payments instantly when I place an order, but when it comes to issuing a refund, it requests that I wait for two to three days*?


![[Pasted image 20240128130452.png]]

1. **Synchronous Replication:**
    
    - In synchronous replication, also known as synchronous commit or synchronous mirroring, the master database ensures that a transaction is not considered committed until the slave database has confirmed that it has received and applied the changes. This means that there is a tight coupling between the master and slave, and the master will wait for acknowledgment from the slave before proceeding with the next transaction.
        
    - **Advantages:**
        
        - Ensures strong consistency between the master and slave databases.
        - Guarantees that the slave has an exact copy of the data as the master at all times.
    - **Disadvantages:**
        
        - Increased latency for write operations on the master, as it has to wait for the acknowledgment from the slave.
        - Higher impact on performance, especially in scenarios where the slave is geographically distant.
2. **Asynchronous Replication:**
    
    - In asynchronous replication, the master does not wait for acknowledgment from the slave before considering a transaction committed. The master sends the changes to the slave, but it does not wait for the slave to apply those changes immediately. The slave processes the changes in the background, and there is a potential for a lag between the master and slave databases.
        
    - **Advantages:**
        
        - Lower impact on the master's performance, as it doesn't wait for the slave's acknowledgment.
        - Allows for more flexibility in dealing with network latency or temporary unavailability of the slave.
    - **Disadvantages:**
        
        - The potential for a delay or lag in data consistency between the master and slave.
        - The slave may not have the latest data immediately after a write operation on the master.

In summary, synchronous replication ensures strong consistency but can introduce latency and performance impact. Asynchronous replication provides better performance on the master but may lead to some level of data lag or inconsistency between the master and slave databases. The choice between synchronous and asynchronous replication depends on the specific requirements of the application, the acceptable level of data consistency, and the trade-offs between performance and data integrity.

here we are following async replication.
![[Pasted image 20240128131006.png]]

![[Pasted image 20240128131236.png]]

watch Naman's classes till now it's not complete and some case FB case study is also not completed i guess