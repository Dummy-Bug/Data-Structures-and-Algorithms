
when we type something on the browser( or search for a website specifically), the first thing browser has to do is talk to a DNS and figure out which IP address the browser should be talking to, and it communicates with the machine at that particular IP. And when you go from one machine to multiple machines, you need a load balancer to distribute traffic uniformly, but after a point when the amount of information cannot fit into a single machine, then the model needs to shard. It can be done using consistent hashing.

However, the machines had both the code and storage in the previous model. Do you think it is a good model?

![](https://lh7-us.googleusercontent.com/iy39KMbPHiTaNvfi5oegD0iZdatvS5WCyBVVRtugLAOyHhjCMe4MBGUQEPMJYDDkRqVduXfFxIZVifNsSwY1pbPIKfwDdbyE1QO82llq_j1MkKkYIz7KLLwffBTsHeX5FqKJPSyYtBbPwOGUGHz2wIQ)

  

It's not, the reasons being:

1. Code and database are tightly coupled, and code deployments cause unavailability.
    
2. Fewer resources are available for the code since the database will also use some of the resources.

4. How to know which appServer's database contains the resource as LB can route the request to any of the appServer , inconsistent.

![[Pasted image 20231030185055.png]]

*CI/CD(whenever we push to the main branch automatically the code would be deployed e.g Jenkins is one way of achieving CI/CD).*

Databases requires HDD and Network resources(for data retrieval) while application requires CPU and RAM, so if we have to scale this system , we would have to scale all HDD,CPU and RAM which would become nothing but vertical scaling. 
So it is better to decouple code and storage. However, *the only downside of decoupling is the additional latency of going from one machine to another (code to the database).*

So it can be concluded that it is not ideal for storing code and database on the same machine. The approach is to separate the code and storage parts to increase efficiency. 

*Different machines storing the same code running simultaneously are called Application Server Machines or App Servers.* Since they don't store data and only have code parts, they are stateless and easily scalable machines.

![[Pasted image 20231030234046.png]]

# Caching

The process of storing things closer to you or in a faster storage system so that you can get them very fast can be termed caching. 

Caching happens at different places. The first place we start caching is the browser. Browser stores/caches things that you need to access frequently. Now let’s look at different levels of caching.

## 1: In-Browser caching

We can cache some IPs so that browser doesn't need to communicate with the DNS server every time to get the same IP address. This caching is done of smaller entries that are likely not to change very often and is called in-browser caching. Browser caches DNS and static information like images, videos, and JavaScript files. This is why a website takes time to load for the first time but loads quickly because the browser caches the information.

## 2: CDN ( Content Delivery Network)

I will discuss fetching images/multimedia from the website (like del.icio.us). You have the browser in some region(say India), and you must fetch the files from the servers located in another region(say the US). When you try to access from your browser, a request is made to the load balancer, and then it goes to the application server and requests files from the file storage. You know that transferring files and other data will be fast for the machines in the same region. But it can take time for machines located on different continents. 
![[Pasted image 20231031001028.png]]
From the website perspective, users worldwide should have a good experience, and these separate regions act as a hindrance. So what’s the solution?

The solution for the problem is CDN, Content Delivery Network. Examples of CDN are companies like

- Akamai
    
- Cloudflare
    
- CloudFront by Amazon
    
- Fastly
    
These companie's primary job is to have machines worldwide, in every region. They store your data, distribute it to all the regions, and provide different CDN links to access data in a particular region. Suppose you are requesting data from the US region. Obviously, you can receive the HTML part/ code part quickly since it is much smaller than the multimedia images. For multimedia, you will get CDN links to files of your nearest region. Accessing these files from the nearest region happens at a much larger pace. Also, you pay per use for using these CDN services.

  

![](https://lh7-us.googleusercontent.com/2CkPfGe90feysmNjnoPRetYNcEwOe4ORaf9kg69TrS8ATpC1sxbUhajyuUrU93PHAfcU4eN7oWZOVFX2fPG5sSftBJ0kiidu6E-J-axijpzNKWpcLbJzXDU0T4FG8Q0llrvI6crEfnaHFxU-jbivMlE)

  
  

One question you might think is how your machine talks to the nearest region only(gets its IP, not of some machine located in another region), when CDN has links for all the regions. Well, this happens in two ways:

1. A lot of ISP have CDN integrations. Tight coupling with them helps in giving access to the nearest IP address. For example, Netflix’s CDN does that. 
    
2. Anycast ([https://www.cloudflare.com/en-gb/learning/cdn/glossary/anycast-network/](https://www.cloudflare.com/en-gb/learning/cdn/glossary/anycast-network/)) 

This CDN process to get information from the nearest machine is also a form of caching.So data goes from our backend database to CDN and once it's cached it speeds up the process as next time CDN would have entry for the data that was sent earlier.Any kind of media file request(not the personal data) e.g scaler-logo.svg would get serve through CDN and CDN would get that file from s3 and cache it.*So no need of LB in such case*.

1. **Origin Server (Amazon.com):**
    
    - Amazon.com, as a large e-commerce platform, has its origin server where the primary website content, including product listings, images, stylesheets, and scripts, is hosted.
2. **Cloudflare Configuration:**
    
    - Amazon.com configures Cloudflare to enhance the delivery of its website content. This involves setting up Cloudflare services to optimize performance, improve security, and leverage the global CDN infrastructure.
3. **Cloudflare Edge Servers:**
    
    - Cloudflare operates a global network of edge servers located in various regions. These edge servers are strategically placed to reduce latency and enhance the speed of content delivery.
4. **Content Replication:**
    
    - Cloudflare replicates or caches frequently accessed content from Amazon.com on its edge servers. This includes product images, CSS files, JavaScript, and other multimedia files. The caching strategy is designed to efficiently serve content from the nearest edge server.
5. **DNS Resolution:**
    
    - When a user attempts to access Amazon.com, the DNS resolution directs the user's request to the nearest Cloudflare edge server. Cloudflare uses Anycast routing to route the user to the optimal edge server based on their location.
6. **Edge Server Delivery:**
    
    - The user's request is served directly from the Cloudflare edge server, which has a cached copy of the requested content. This reduces latency and improves the overall load time for the user.
7. **Caching Strategies:**
    
    - Cloudflare employs caching strategies to optimize content delivery. Popular images, product thumbnails, and other multimedia content are cached at the edge servers. Cloudflare's caching settings allow for customization based on time-based rules and content types.
8. **Security and Performance Features:**
    
    - Cloudflare provides security features, such as DDoS protection and a web application firewall (WAF), to protect Amazon.com from potential threats. Additionally, Cloudflare includes performance optimizations, such as image compression and automatic minification of files, to further enhance the user experience.

*Both Browser chaching and CDN  is outside the backend architecture*
## 3: Local Caching

It is caching done on the application server so that we don't have to hit the database repeatedly to access data.One application server cannot access the local cache of any other server's local cache.

## 4: Global Caching

(This will be discussed in more detail in the next class)

This is also termed In-memory caching. In practice, systems like Redis and Memcache help to fetch actual or derived kinds of data quickly.Global caching layer lies between application server layer and database layers.Every application server can access any cache node in global caching server.
# Problems related to caching

There are also two things related to the cache that you can derive from the discussions so far. 

- Cache is limited in size
    
- It is not the actual source of truth; that is, the actual data is somewhere else. It stores a replica of data.

![](https://lh7-us.googleusercontent.com/Pfca8ruLYIZ7PvFGcUeh0_jbqVpJlIKY9yiJPfVz2LtFzYq9HAj_nfA5xMH6EdC4sQPZJDB4f0AXh8Or5MMqcuPBkCF9ulknpi6aovgzstMkoWUziYQ5C56_bOACw3CuBVZ5y-AFlFop_Bb_NtGr9yw)

There are a few problems that you may face:

- Data can become stale and inconsistent with time (Data in Database - actual source of truth - changes. But is not reflected in cache)
    
- The cache can become full due to its small storage capacity.
    ![[Pasted image 20231031090345.png]]
So what do you think will be the solution to these two problems:

1. What do you have that doesn’t become inconsistent?
    
2. How can you add entries if the cache is full?
 
We will be discussing ways to prevent these problems.

## Case Invalidation Strategy

One solution that is proposed so that cache doesn’t become stale is

### TTL (Time to Live) 

This strategy can be used if there is no problem with the cache being invalid for a very short time, so you can have a periodic refresh. Entries in the cache will be valid for only a period. And after that, to again get the entries, you need to fetch them again.
![[Pasted image 20231031091123.png]]
So, for example, if you cache an entry X at timestamp T with TTL of 60 seconds, then for all requests asking for entry X within 60 seconds of T, you read directly from cache. When you go asking for entry X at timestamp T+61, the entry X is gone and you need to fetch again. 
	*Cache won't throw the stale entry until it gets a read request for that entry*
***Eventual Consistency*** means that for a short amount of time, data may be inconsistent, but for the rest of the time, it will be consistent. For example, if you post something on LinkedIn and then edit that post, upon refreshing the page, sometimes you may see the old post, and other times you may see the edited post. This inconsistency occurs because LinkedIn uses multiple cache servers, and not all of them have been updated yet. However, if you view the same post after a few hours, even after refreshing it multiple times, it will consistently show the edited post. This is known as eventual consistency, and many companies use this strategy because, in most cases, minor inconsistencies are not a significant problem. 

*To clarify, Time To Live (TTL) settings provide eventual consistency. For example, if the TTL is set to 2 hours, and an entry in the database is changed before 2 hours have passed, the cache will still serve the old entry until the 2-hour time limit expires.*

**Write around cache:** Here, the writes are done directly in the database, and the cache might be out of sync with the database. 
![[Pasted image 20231031092935.png]]Hence we can use TTL or any similar mechanism(we have a separate service(CRON job) to periodically check say after 2hrs just acting like TTL ) to fetch the data from the database to cache to sync with it.for scaler leaderboard follows this approach, every 15 minutes scaler has a cron job that takes data from DB and update the cache.However it also gives the eventual consistency because logic is same more or less.

*In TTL and write around cache whenever we write , we write only in DB*
### Keeping cache and DB in sync

This can be done by the strategies like Write through cache, Write back cache, or Write around the cache.

**Write through cache:** In a write-through cache, any write operation that updates data in the cache is also immediately written to the main storage. If failed, changes will be reverted in the cache. So we are kinda writing through the cache.
![](https://lh7-us.googleusercontent.com/SJv55CJwy5uw8oTeMTBBg_PHiMwsnp2tHzcktX_POXtLI6FBylA-5X7nKADiXZ8coCDK_BkdNgOAnAC_V6RKF14J6UGT-XEVc3tUCwUErfNiEgTvwnnIuwI942IkNlNCFlQ5stZwL2pVxbCSfTwfKc0)
1. **Data Write Operation**: When a write operation is initiated, the data is first written to the cache.
    
2. **Write to Main Storage**: Simultaneously, the same data is also written to the main storage or the underlying persistent storage.
    
3. **Confirmation**: The write operation is considered complete only when the data is successfully written to both the cache and the main storage.
4. It makes the writing slower(all the cache servers would have to be updated) but reads much faster. For a read-heavy system, this could be a great approach.

  ![[Pasted image 20231031093625.png]]
*write through gives us immediate consistency*

**Write-back cache** is a caching technique where, when a write operation is initiated, the data is first written to the cache. Once the write in the cache is successful, a success response is immediately returned to the client. Importantly, the data is not written to the database (DB) in the first go. Instead, data is synchronized with the database asynchronously, typically using a CRON job, which now acts in reverse. In this reversed role, it transfers data from the cache to the database without blocking ongoing requests. This method is preferred in situations where immediate data consistency isn't critical, such as in an analytical system where the precise data in the DB doesn't matter, and losing occasional data points won't significantly affect the analysis of trends. 

This approach provides high throughput and low latency, as it prioritizes write speed over immediate data durability. However, there is a risk of data loss if the cache crashes before the data is synchronized with the DB. Data loss can occur when the cache crashes and the unsynchronized data is lost. This might lead to scenarios where, for example, once a month, a small amount of data (e.g., 2 hours worth) may not make it into the database. In the context of platforms like YouTube, where the exact count of views might not be critical, this trade-off can be acceptable. For example, reaching 1 million views may be sufficient, and precise counts beyond that might not matter.

It's worth noting that cache crashes are relatively infrequent, perhaps occurring only once a month. Therefore, data loss is occasional but not constant. For scenarios where many write operations need to be processed quickly, such as when recording likes on a video, it may not be practical to perform a database transaction for every individual write. Using a write-back cache helps optimize write performance in such cases.

Now let’s talk about the second question: How can you add entries if the cache is full?
Well, for this, you be using an eviction strategy.
## Cache eviction 

There are various eviction strategies to remove data from the cache to make space for new writes. Some of them are:
![[Pasted image 20231031090627.png]]

- FIFO (First In, First Out)
    
- LRU (Least Recently Used)
    
- LIFO (Last In, First Out)
    
- MRU (Most Recently Used)

The eviction strategy must be chosen based on the data that is more likely to be accessed. The caching strategy should be designed in such a way that you have a lot of cache hits than a cache miss.