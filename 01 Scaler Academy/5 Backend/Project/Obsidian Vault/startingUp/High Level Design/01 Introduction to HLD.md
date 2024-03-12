**What’s system design?

Low level design covers the structure of code in a given component. However, a large scale system will have multiple components / services. *High level design is about the optimal design of which components to have for a fast and efficient system. More on this later.*   

**Why do we need distributed systems?**

Let’s take a real story of a website that started on a single laptop in a dorm room (Exactly how we write code today). Back in 2003, there was a website that went by the name of Del.icio.us ([https://en.wikipedia.org/wiki/Delicious_(website)](https://en.wikipedia.org/wiki/Delicious_(website))). 

Browsing the internet was completely based on bookmarks and you would lose bookmarks the moment you changed browser / machine. So, delicious built a bookmarking website. You login, and then bookmark websites using delicious tool. That way, when you go to any other machine/browser, all you need to do is to login into delicious with your account to get access to all your bookmarks. Basically, largely delicious implemented following 2 functions:

- addBookmark(userId, site_url)
    
- getAllBookmarks(userId)    

If you were to code those 2 functions on your laptop, would you be able to? Assume you store entries in MySQL database which is also on your laptop. 

If yes, congratulations. Your version of delicious is almost ready. 

**Problem 1: How do I ensure that when people type del.icio.us in their browsers, they reach my laptop?** 

The internet world only understands IP Address. How do people know the IP address of my laptop when they type del.icio.us? 

How do you setup your personal website today? 

- You go to GoDaddy to buy a domain. 

Ok, but how does GoDaddy know which domain name is available? People can buy domains from GoDaddy / NameCheap / domains.google and tons of other websites. 

*There must be a central place maintaining domain names and their owners. And yes, there is. It’s called ICANN (The Internet Corporation for Assigned Names and Numbers)*. It’s non profit and has a directory of all registered domain names along with their owner details and the date validity. 
![[Pasted image 20231029140207.png]]

Alright. But that still does not solve my problem. If I go to GoDaddy and buy delicious domain name, is my issue solved? A random user’s browser still does not know how to reach my laptop. 

So, that means I should be able to associate my domain name to my laptop’s IP address. That is exactly what happens. You can create “A” record in GoDaddy that is then registered centrally. 

Ok, so now ICANN knows IP address of my laptop tied to delicious domain name that I bought. ICANN does not provide the IP address it just stores them. Which means theoretically, when someone types delicious in their browser, they can get the IP address they need to go to from ICANN. let's say we type www.scaler.com in our browser then browser will first goto ICANN server and ICANN server will give it the IP address associated with www.scaler.com. But is that a good design? whenever you have come up with some design always ask this question is this a good design ? what is wrong with it ?Not really. ICANN becomes the single point of failure for the entire internet. 
Ok, then what do we do? Imagine if there were thousands of machines all around the internet that had a copy of the information(mapping of domain names to IP addresses) that is there on ICANN. Then our problem could have been solved. Because now people typing delicious on their browser, could find out the IP address from these machines. 

Very simplistically, *these machines are called DNS machines (Domain Name Servers).* While the DNS architecture is decently complicated (You can read [https://support.dnsimple.com/articles/differences-between-a-cname-alias-url/](https://support.dnsimple.com/articles/differences-between-a-cname-alias-url/) if interested), in simple words, DNS machines maintain a copy of information present centrally and they keep pinging every few hours(configurable) to get any recent updates from the central machines. It might also be possible that DNS does not copy all the data from ICANN. let's say Roshan has created it's own DNS and he has very limited RAM in his laptop so he decides to keep top 10 websites according to traffic. so when some user say Aditya tries to get www.abc.com from Roshan's DNS then Roshan's DNS will say website does not exist even though the website it actually there and this is exactly how some of the ISP like Reliance , Airtel try to block some websites(porn). There are other ways of blocking as well.

1. **Registration with a Domain Registrar:**
	- When you create a website, you need to register a domain name (e.g., "ABC.com") with a domain registrar. This is a commercial entity accredited by ICANN to register domain names.
	
1. **Domain Registrar and ICANN Interaction:**
    - The domain registrar collects the necessary information about your website, including its IP address (let's say 123.456.789.123), and submits this information to the central authoritative database managed by ICANN.
    
1. **ICANN's Role:**
    - ICANN maintains the central authoritative database that contains information about domain names and their corresponding IP addresses. This database is a critical part of the overall Domain Name System (DNS) infrastructure.
    
1. **DNS Hierarchy and Replication:**
    
    - The DNS operates in a hierarchical structure. At the top is the root domain, followed by top-level domains (TLDs), subdomains, and individual domain names.
    - ICANN oversees the root DNS servers, and the information about the authoritative DNS servers for each top-level domain is maintained there.
    - When you register a domain with a domain registrar, the information about your domain and its associated IP address is propagated to the authoritative DNS servers for the corresponding TLD (e.g., the servers responsible for the ".com" TLD).
    
1. **Distribution to DNS Servers:**
    
    - The authoritative DNS servers for the TLD (.com, in this case) then distribute this information to lower-level DNS servers.
    - These lower-level DNS servers may include recursive DNS servers operated by internet service providers (ISPs) and other organizations.
6. **DNS Resolving Process:**
    
    - When a user types "ABC.com" in their browser, their device queries a recursive DNS server.
    - The recursive DNS server, if it doesn't have the information cached, queries the authoritative DNS servers for the TLD (.com).
    - The authoritative DNS servers respond with the IP address of the name server responsible for the specific domain "ABC.com."
    - The recursive DNS server then queries the name server for "ABC.com," which responds with the actual IP address (123.456.789.123).
    - The user's device can now connect to the web server at the IP address 123.456.789.123 to access the website."
    
![[Pasted image 20231029140041.png]]
[Not spending time on DNS architecture since the class is not on DNS. We did the discussion to give an insight into how internet works]. 

let's say Airtel has DNS server in US and user Saumya is using Airtel's internet from Mumbai now it would take at least 200ms of time to visit the website she wants to visit (see the pic for calculations). so it does not matter what Saumya does internet cannot be faster than light.so 200ms limit will always be there. So it makes sense for Airtel to have a DNS server in Mumbai also.

**Ok, so now we are live. Delicious is now serving users.** 

There is a small problem though. Every time I want to add new features and re-deploy and re-start my laptop with new code, delicious is unavailable for a few seconds. That’s not good. So, what do I do? 

Maybe instead of one laptop, I have multiple laptops with same code and same information (We will figure out how to keep this information in sync). However, when my code is being deployed to a laptop X, how do I ensure no traffic is coming to X? 

*We need a Load Balancer which keeps track of laptops, which ones are running and is responsible to split the load equally.* 
![[Pasted image 20231029150843.png]]

How does Load balancer do that? 

- Which machines are alive? - Heartbeat / Health Check
    
- Splitting load? - Round robin / Weighted Round Robin / Ip Hash 
    
[https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/) has example of a config setup of a load balancer. 

Imagine, Del.icio.us becomes majorly popular. It starts getting massive traffic. It starts getting a million new bookmarks every day. 
![[Pasted image 20231029151214.png]]
Now, remember this is 2004. Best machines had 40GB hard disk. If you were getting 1 Million new bookmarks every day, and every bookmark is 200 bytes roughly, then you are adding 200MB of new bookmarks every day. Which means you will run out of space in 6 months(200 days). What do you do? 
  ![[Pasted image 20231029151149.png]]
so you have to scale it horizontally. Buy multiple cheap systems.
![[Pasted image 20231029152327.png]]

## Knowledge++

1. A Record (Address Record):
   - An A record maps a domain name to an IPv4 address. In the case of "www.google.com," you would set up an A record to point it directly to Google's IPv4 address. 

   Example:
   ```
   www.google.com   IN  A   172.217.1.100
   ```

   This A record would resolve "www.google.com" to the specific IPv4 address "172.217.1.100."

2. CNAME Record (Canonical Name Record):
   - A CNAME record creates an alias for a domain. If you want "www.google.com" to point to the same location as "google.com," you can create a CNAME record.

   Example:
   ```
   www.google.com   IN  CNAME   google.com
   ```

   This CNAME record would make "www.google.com" an alias for "google.com."

3. ALIAS Record:
   - Some DNS providers, like Amazon Route 53, offer ALIAS records. These are used to point the root domain (apex domain) to another domain. In the case of Google, you could create an ALIAS record to point the root domain (google.com) to an external service, such as a load balancer.

   Example:
   ```
   google.com   IN  ALIAS   loadbalancer.example.com
   ```

   This ALIAS record allows the root domain "google.com" to point to the external load balancer "loadbalancer.example.com."

4. URL Record:
   - URL records are not standard DNS records but are sometimes offered by DNS hosting or management services for URL redirection. If you wanted to create a URL redirect from "www.google.com" to a specific page, you might use a URL record.

   Example (non-standard, and format may vary by DNS service):
   ```
   /maps   IN  URL   https://www.google.com/maps
   ```

   This URL record would typically be used for creating a URL redirect within your DNS management interface.


**To-DO** 
* How does Bluetooth works ?
* How does government block porn websites?
* What is the difference in 3G,4G and 5G ?
