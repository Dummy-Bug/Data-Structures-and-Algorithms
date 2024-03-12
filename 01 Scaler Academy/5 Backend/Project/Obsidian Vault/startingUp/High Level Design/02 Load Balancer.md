
Scaler pushes a wide variety of updates to the platform every day, be it, features or bug fixes. You are a developer at Scaler verse. You want to add a new property to the Scaler Verse. Assume that all the non-technical stuff like legal, accounting, and marketing is completed and we now want the users to know about the new property via a dedicated landing page. The Landing page should allow the users to join the waitlist for the property at a nominal fee of 500. You took your time and you built the entire page. You passed with flying colours. The next step is to deploy the landing page on the actual Scaler Server.

For now, we will assume that Scaler is running on One Server only. You somehow log in to the server and copy the new code to the server either by using git or by using some other tool. Independent of the language (NodeJs , Django, Ruby, etc.) being used, the running application must be restarted for the new changes to take effect. Given how huge the platform is, the application would take a considerable amount of time to boot up or load itself into the memory. During the loading time, your application is briefly unavailable. Users are receiving 502 from scaler for some time.

As the traffic scales, you realise that the server is not able to withstand the load and is intermittently(occurring at irregular intervals) going down. To fix this, you work day and night to optimize the code. You increase the memory, storage and processor of the server to cater to the ever-increasing demand.

Scaler wants to increase the number of users on the platform. For the same, They hold a competition and you are informed that the traffic can increase by 10x. 

**DEAD END!!! What to do now?**

Of course, you talk to some of your fellow engineers or read something online to find the solution, i.e., Install a LOAD BALANCER. It can help you tackle all of the above-mentioned issues whilst giving a significant performance boost and saving you a panic attack.

BTW: Assumed architecture is known as a Single Server Architecture.

  

 ![](https://lh7-us.googleusercontent.com/P-SpHCdUKnTMSIfyAcrkz--p4kR4QTOYXRtSSA6FImK0dYWP4x14uQdDODG521dfIysMgGAf8xGxtgBMS_qzX8gz-aJ6mTjVyRzgj8m10VMLZEiE1_JUAexcTR5LFwu-VDJyp5LoEuKgvuV2RSu0s8I)

## Load Balancer

Before diving into what is Load Balancer and its features or advantages, let’s first try to think what would be our approach or algorithm for tackling the above issues.

What if there were 2 hosts for our application? When we want to deploy a newer version of our application, we could deploy them one by one on both these hosts while keeping at least one of them active at all times. A piece of code would be responsible for managing the traffic based on specific circumstances, for example, If one of the 2 hosts is not responding for some reason, be it, application failure or memory failure, the system could notify us immediately. 

The deployment algorithm would follow the following steps:

1. ‘for’ each host for our application
1. Mark the host as inactive
2. Deploy the new code.
3. Restart the application.
4. Perform some basic sanity checks.
5. Mark the host as active
3. If a host is marked as inactive, do not serve the traffic to that host and vice-versa, if a host is not responding to the traffic, mark the host as inactive.
4. Only serve traffic from active hosts.

BTW: This piece of code is Load Balancer.

![](https://lh7-us.googleusercontent.com/aRmaFx1cI3Yr5hjxsp4BW28wTDrT6uGa8gDe6PLH--fBT14d_Vgxr_u7hReCD1vU8oY8nz-om62U1k7TRW4d4wEOuu4Y3Y5Fem74Tb2OLYsrYBAd1MNpsj6IGJT4NTQdRPMCj-0FqWEDUw1B3X7Qt2g)

  

***A load balancer is a device that distributes network or application traffic across several servers. It helps scale horizontally across an ever-increasing number of servers.***

## Concept

**A Load Balancer is a physical/virtual device used to balance the network load across Web-Servers. Load Balancer could sit inside the Data centres for internal Load Balancing but usually are placed facing the internet to balance the load across the Web Servers in the Data-Centers.**

  

![](https://lh7-us.googleusercontent.com/eL1CkpTMiaCI8Ebs_Qp9mHCsFXaASEmSf6GMi-tMlLRVLANHasvKvXQt8U2QNzGDFyjGmdAOmr2JAaQDAih33wwTOwvBPLIapMrJHaFu1mv5fRMbePgcIOZHqihDt-wKNv5tHbZLVSGOvdTjr0J9qnE)

  

From the above diagram, it is clear that *the entry point of our application is now the Load Balancer itself and not the server itself.* Now that we have a fleet(coordinated and organized group of similar entities) of servers, we can efficiently manage and distribute the load or traffic across different servers.
The entire traffic, irrespective of whether it is from a handheld device or a system, arrives directly at the load balancer. *The load balancer then sends the traffic to one of the available servers, based on certain decision-making algorithms. The response is then received from the server by the load balancer which is then straight away sent back to the client*. ***Of course, we can make certain adjustments like a different load balancer of handheld devices*** but for the sake of simplicity, let’s first discuss this above architecture in detail. Assume that the number of EC2 servers (hosts) are infinite for now and that they can be added or removed as per our demand.
![[Pasted image 20231029235818.png]]

## Deployments

The deployments work more or less the way we discussed before. When we are about to deploy a new application version, we loop through all of the available hosts and for each host, we detach the host from the load balancer, deploy the new version on this host, restart the required services on the host and then reattach the host to the load balancer. This beautiful invisible dance helps push the newer updates quickly, reliably, and without downtime.

## Resilience

Since, the entire traffic flows through the load balancer, what if there is a certain low latency monitoring mechanism that notifies us if the traffic is increasing or decreasing at certain times. If we are notified before-hand, we can increase or decrease the hosts so that the load is distributed evenly across all the hosts. The “Load Balancing”!

The above approach is, however, a bit dangerous, because the traffic has already reached the load balancer. Remember, the LB, in our architecture, is configured to just push the traffic to one of the available servers blindly. By the time we add more hosts for our application, it might be too late. To curb(restrain) this, we define a threshold above which we would want our hosts to be increased and a lower bound below which our hosts would be slowly removed.

This architecture also takes care of a scenario when some of our hosts are somehow down. If one or more of the hosts are down, LB has a mechanism known as “Health Check” by which it pings the available hosts after a certain point of time in regular intervals. If the host is unreachable, it is marked as inactive or unhealthy and the host does not receive any traffic. What if our application has some kind of failover that brings back the host online? Right, The LB will ping inactive servers as well to mark them as active in case they are ready to receive the traffic
## Security

What if, the LB is intelligent enough to detect whether the request received is a malicious request or a valid and genuine request? What if, the LB can automatically reject the request if it recognises it as an attack vector?

This is where the security aspect of LB comes into play. Since the LB is the entry point of all the requests, it reduces the chance of Servers’ IP addresses getting leaked, thereby reducing the chance of a direct attack on the server. If the LB is intelligent enough, it can also detect and discard malicious requests. 


1. **Client Request**:
   - You open your web browser and type "www.google.com" in the address bar or click on a bookmark for Google.

2. **DNS Resolution**:
   - Your computer first needs to determine the IP address of "www.google.com" so it can connect to the website. It sends a DNS (Domain Name System) query to your local DNS resolver.

3. **DNS Resolver Query**:
   - Your local DNS resolver may already have cached Google's DNS information. If not, it queries the root DNS servers and various authoritative DNS servers to find the IP address associated with "www.google.com."

4. **DNS Response**:
   - The DNS resolver receives an IP address (for example, an IPv4 or IPv6 address) for "www.google.com." This IP address is associated with the load balancer.

5. **Client Request to Load Balancer**:
   - Your computer sends an HTTP request to the IP address obtained from DNS. This request goes to Google's load balancer. The load balancer acts as the entry point for all incoming requests to Google.

6. **Load Balancer Processing**:
   - The load balancer examines the incoming request. It checks its configuration to determine how to distribute the request among Google's multiple data centers or server clusters. The load balancer can use various load-balancing algorithms (e.g., round-robin, least connections, IP hash) to decide which backend server or data center will handle the request.

7. **Backend Server Selection**:
   - The load balancer selects one of Google's backend servers based on its algorithm and the current server health. It routes the client's request to the chosen server.

8. **Processing by Backend Server**:
   - The selected backend server processes the request. In the case of Google, this might involve serving search results, handling user queries, and more.

9. **Response to Load Balancer**:
   - The backend server generates the response and sends it back to the load balancer.

10. **Load Balancer Response to Client**:
    - The load balancer receives the response from the backend server. It then forwards this response back to your web browser through the same connection that was established earlier.

11. **Client Display**:
    - Your web browser receives the response, which contains the HTML and other assets needed to render the Google homepage. Your browser processes this data and displays the Google search page.

## Performance

**SSL/TLS with Load Balancers**: Load balancers are often used to distribute incoming web traffic among multiple servers or server clusters to ensure scalability, reliability, and improved performance. In this context:

1. **SSL/TLS Termination**: When SSL/TLS encryption and decryption are configured directly on the load balancer, it is said to perform SSL/TLS termination. This means that the client's SSL/TLS connection terminates at the load balancer.
    
2. **Plain Traffic to Servers**: After SSL/TLS termination, the traffic between the load balancer and the backend servers is typically transmitted in plain, unencrypted form. The load balancer decrypts incoming requests, processes them, and then re-encrypts the response (if the response is intended to be secure).
    

**Why is Traffic Between Load Balancer and Servers Plain?**: There are several reasons for this configuration:

- **Efficiency**: SSL/TLS encryption/decryption can be computationally expensive. By offloading this task to the load balancer, backend servers can focus on processing requests and not be burdened with encryption/decryption overhead.
    
- **Load Distribution**: Load balancers need to inspect and distribute incoming requests efficiently. This requires accessing the unencrypted data to make routing decisions based on factors like server health and request type.
    
- **Security**: In some cases, the traffic between the load balancer and backend servers may be transmitted over a secure, private network, making encryption at this stage less critical.
    

In summary, SSL/TLS encryption secures the traffic between clients and the load balancer, with SSL/TLS termination happening at the load balancer to offload processing from the servers. Traffic between the load balancer and servers is typically unencrypted for efficiency but should be transmitted over a secure network.

But How does LB work in itself?
## Reverse Proxy

Strictly speaking, A reverse proxy is a type of proxy server.  *Unlike a traditional proxy server(Psiphon), which is used to protect clients, a reverse proxy is used to protect servers.* A reverse proxy is a server that accepts a request from a client, forwards the request to another one of many other servers, and returns the results from the server that processed the request to the client as if the proxy server had processed the request itself. The client only communicates directly with the reverse proxy server and it does not know that some other server processed its request.

So, the LB is working as a reverse proxy for us. This also fixes a security issue for us. If the response was directly sent from the server, it would have exposed a wide variety of information about the server in response headers. Reverse proxying the request ensures that the information in the response headers is that of the reverse proxy (LB in this case) and not of the running application’s server.
A reverse proxy includes load balancing as one of its features, but it offers a broader set of functions that go beyond load balancing alone. Load balancers focus primarily on evenly distributing network traffic among servers, while reverse proxies offer additional capabilities such as caching, security features, and more. The choice of whether to use a reverse proxy or a dedicated load balancer depends on the specific requirements of the application or service being deployed.

## Health Checks

![](https://lh7-us.googleusercontent.com/X2N3LCQb_3dXFW5BGXaGPq_XotmEeowm_FbK0V5UzBISyj_gxZNQ2XeoSTU1ItvNtYzf_UiSDu_IiM8weTA4SyTkauUXVjvKwPfs8qMU8tWPLnYPGAtNjM4livdf6K6ovzWBqjQ0I4SDsA1pY7To5Zo)

Depending on the provider, The LB checks whether a host is active or not. Active and Inactive terms are generic and providers generally use different terms to denote them. For instance, AWS uses Healthy and Unhealthy terms respectively.

LB pings the server at a certain port (8080) and requests a certain path (/) over a certain protocol (HTTP) after a certain interval (the 30s). The response timeout(5s) for every request is the maximum time LB will wait before terminating the request and marking the same as failed. A total number of Unhealthy Threshold (2) requests are required before marking any of the hosts as inactive or unhealthy. Along the same lines, A total number of Healthy threshold (2) requests are necessary to declare the target host as an active or healthy host.

## Scale itself

Think of a case where LB is bombarded with an insane amount of requests such that LB goes down! Remember, LB is the entry point of our application and if it goes down, we are doomed! 

Depending on the provider, There are different mechanisms put in place to ensure that LB is always ready to scale itself up and down as and when necessary. For instance, the load balancer has a traffic capacity in Gbps in AWS. It can scale itself automatically up to a maximum of 100 nodes.

## Algorithms

The algorithm widely and majorly used to efficiently manage load is Round Robin. You may already be familiar with the Round Robin algorithm but let’s cover it with the help of an architectural diagram.
### Round Robin

Round-robin load balancing is the simplest and most commonly-used load balancing algorithm. Client requests are distributed to application servers in simple rotation. For example, if you have three application servers: the first client request is sent to the first application server in the list, the second client request to the second application server, the third client request to the third application server, and the fourth to the first application server, and so on.

![](https://lh7-us.googleusercontent.com/loFJqCAWADbYwbsiCE_MEwapPVLt24X3cBKo3-kkIMMVZfbt5RzvcaUoo2baiV-NwS1n7pJNec78BhwfupeTKGBt2X1h9pU-CiqUrgHqoM-RxxgcUO5aHK6C5WDXKSeKpvB-PhkbrhdcuZU3kb1-QVM)

## Concepts involved in setting up a Load Balancer

### Listeners
### ![](https://lh7-us.googleusercontent.com/ojk6v3GK1LDyBRVJQM0YFh_N_xEr-2Y4FnA65SwbH46j5uiBZuhEy-dzZn2w2N4NHqW7NBYUaMk9kl-TRGbiVn49nwl95VNUwsvgdEAKgcOb49XKPQDtkN2xL6Stq9gGiNKsZopTf5VRK2b_0TBKmX4)

Listeners for a load balancer are the combination of protocols and ports on which the LB will accept incoming requests. For example, in the above image, only HTTPS connection on 443 and HTTP connection on 80 will be accepted by the LB and the rest of the others will be discarded as-is. We also define the destination for these requests. In the same directed image, HTTPS and HTTP both the requests will be forwarded to the HTTP port 8080 of the host.
### Routing

Load Balancer (in some cases) also allows us to forward a request to a defined destination based on certain conditions. For example, Let’s say I would like to forward all the admin requests to an internal fleet of servers that can serve admin requests. To achieve this, we can create a rule that states that if the request is admin (path matching), forward the request to an internal admin server.

### Target Group

Each target group is used to route requests to one or more registered targets. When we create each listener rule, we specify a target group and conditions. When a rule condition is met, traffic is forwarded to the corresponding target group. We can create different target groups for different types of requests. For example, create one target group for general requests and other target groups for requests to the micro-services for your application.

# Knowledge++

**API Gateway**:

An API gateway is a server or service that acts as an entry point for a collection of microservices or APIs, offering a centralized and managed interface for client applications. It provides several functionalities, including:

1. **API Management**: API gateways are designed to manage and expose a collection of APIs to clients. They serve as a unified entry point for different services and APIs.

2. **Security**: API gateways often handle security-related tasks, such as authentication, authorization, and access control. For example, they can enforce API key validation, OAuth 2.0 authentication, and rate limiting.

3. **Routing and Transformation**: API gateways route incoming API requests to the appropriate backend services, transforming requests and responses as needed. They can modify request headers, payloads, and responses.

4. **Request/Response Transformation**: API gateways can perform transformations like data format conversion (e.g., XML to JSON), aggregating data from multiple services, or filtering and editing responses.

5. **Load Balancing**: While API gateways may include load balancing, their primary focus is on managing and routing API requests to various backend services.

**Example**: Amazon API Gateway, which provides a fully managed service for creating, publishing, and securing APIs. It allows you to define APIs and configure various aspects like authentication, caching, and routing.

**Reverse Proxy**:

A reverse proxy is a server that sits between client devices and backend servers, serving as an intermediary for incoming requests. Its primary functions include:

1. **Load Balancing**: Reverse proxies distribute incoming requests among multiple backend servers to optimize performance and ensure high availability.

2. **Security**: Reverse proxies can provide security by protecting backend servers from direct exposure to the internet, filtering out malicious traffic, and handling SSL/TLS encryption termination.

3. **Caching**: Reverse proxies can cache static assets or responses to reduce the load on backend servers and improve response times.

4. **SSL/TLS Termination**: Reverse proxies can handle SSL/TLS encryption and decryption, offloading this computationally expensive task from backend servers.

5. **Content Compression**: They can compress content before delivering it to clients to reduce bandwidth usage.

**Example**: Nginx, a widely used open-source web server and reverse proxy server. Nginx can serve as a reverse proxy for load balancing and SSL termination, enhancing server performance and security. It also supports features like content caching.

**Key Difference**:

The primary difference lies in their focus and functionality:

- An API gateway is designed for managing and exposing APIs, offering advanced features like security, request/response transformation, and API-specific management.
- A reverse proxy, while it may include load balancing, serves a broader range of functions, including load distribution, SSL termination, caching, and security. It's not API-specific and is used for general web traffic management.

In some scenarios, an API gateway may include reverse proxy capabilities as part of its feature set to handle various aspects of API traffic management. However, they are distinct tools with different use cases.


Suppose a popular e-commerce website, "example.com," wants to ensure high availability and efficient load distribution to handle incoming traffic. To achieve this, they employ DNS load balancing on top of multiple load balancers.

**Components**:

1. **Load Balancers (LB1, LB2, and LB3)**: These are responsible for distributing client requests among backend servers to ensure optimal resource utilization and redundancy.
    
2. **DNS Server**: The DNS server manages the domain name "example.com" and its corresponding DNS records.
    

**Explanation**:

1. **Multiple Load Balancers**:
    
    - The e-commerce website operates multiple load balancers (LB1, LB2, and LB3) to distribute incoming traffic among backend servers. This provides redundancy and load balancing.
2. **DNS Configuration**:
    
    - The DNS server for "example.com" is configured to point to multiple IP addresses corresponding to the load balancers (LB1, LB2, and LB3). Each load balancer has its unique IP address.
        
    - DNS records for "example.com" are set up as follows:
        
        - "example.com" resolves to the IP address of the DNS-based load balancer.
        - The DNS-based load balancer, in this case, is not a physical load balancer but another DNS server that manages DNS records.
3. **DNS-Based Load Balancer**:
    
    - The DNS-based load balancer acts as a traffic director and is responsible for distributing client requests among the multiple load balancers (LB1, LB2, and LB3).
4. **Client Requests**:
    
    - When a client wants to access "example.com," they perform a DNS query to resolve the domain name. The DNS-based load balancer receives the DNS query.
5. **DNS Load Balancing**:
    
    - The DNS-based load balancer dynamically selects one of the physical load balancers (LB1, LB2, or LB3) to handle the client's request. This selection can be based on factors like server load, geographic proximity, or predefined distribution rules.
6. **Request Forwarding**:
    
    - The selected physical load balancer (e.g., LB2) then takes over and distributes the client request to the appropriate backend server based on its own load-balancing algorithm.
## Further Reading and Questions

1. How is the traffic across different regions regulated? On a very high level, how would the deployment in this case execute? (“Global Server Load Balancer”)
    
2. Let’s say that a user is logged in to the account on host A. What if the next request for the same user goes to another host B? What kind of inconsistencies can arise in this case? (Session stickiness concept)
    
3. What is the dynamic and static content? How do you think the load balancer architecture works in this scenario? (Static content hosting)
    
4. Example configuration file: [https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/)