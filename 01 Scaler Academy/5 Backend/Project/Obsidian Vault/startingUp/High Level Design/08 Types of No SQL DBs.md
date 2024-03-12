https://docs.google.com/document/d/1CfwsMMw8NTn2zavVokiYG08EH648Gsd1zJ7aAM7NvS4/edit

![[Pasted image 20240130201913.png]]

**Key-Value pair :-** Hashmap is nothing but a key-value pair but why  relational DB cannot be used as key-value pair ? because as we can see in the given figure below we have the type of the data as the constraint in values column. so every item to be inserted inside values should have fixed data type.

![[Pasted image 20240130202309.png]]
but what if we do not have fixed data type ?
* So key value pair No SQL DB is typical used when we do not have a fixed data type for values.
* e.g many people will try to open home page of scaler.com in a day so we can make www.scaler.com as key and it's value can be complete html code of scaler's home page and cache it so whenever in future someone tries to open the home page it can be served in no time without even going to database.
* we can cache the test cases of question where values can contain list of test cases corresponding to the questionId as the key.
* similarly  environment variables can also be stored in key value pair.
so in both of the examples data types of key and value were not fixed 
![[Pasted image 20240130222818.png]]
*we can use key value databases when all the queries are on  keys*
* since queries are only on the keys hence it is optimized for particular type of queries 
![[Pasted image 20240130223124.png]]
what if we want to search get those rows where name is Naman then it is nothing but query on the values , such types of queries won't be fast. because key value pair are only optimized to get a key and set a key.
*using dynamoDB as backend create MongoDB it can be done easily*

**Document DB :-** when we have unstructured data where every entity can have it's own set of attributes.
![[Pasted image 20240130224005.png]]
* Even key value pair can store unstructured data but it will fail if we query on the values . e.g give me the phone that have RAM > 6GB etc are queries on values.
* Document DBs are also key value pairs with additional function of querying on attribute of every entity.

![[Pasted image 20240130224443.png]] * Every entity(table) is a JSON in Document DB.
![[Pasted image 20240130225207.png]]

**Column Databases:-**
many questions come form this.
![[Pasted image 20240130225251.png]]
let's first understand how does relational databases store data internally? it will store each row one after the row.
Indexes reduces number of input output from the disk because disk access are slow so if we reduce the disk access our program would run faster.
![[Pasted image 20240131201504.png]]
option 1 will work faster because double array is also stored row after row
![[Pasted image 20240131201934.png]]every nearby data the i fetched was important for us
but int the following figure
![[Pasted image 20240131202117.png]]in first row amount is <= 100 so we unnecessarily fetched the whole row, so we did some useless work
![[Pasted image 20240131202231.png]]in first and last row userId != 2 yet we fetched them which was not necessary.
![[Pasted image 20240131205333.png]]we just needed one cell from first row yet we fetched whole row same for 2nd and for 3rd row.
so in above figure we data was stored in column rather than row wise then we would have much less useless accesses. see the figure below let's say in first disk access we fetched data till 100 and in next disk access we fetched till a, so only in two disk accesses we have all the data that we required.And if our database is so smart that it knows that value 100 start from 4th index then only in one disk access we can achieve the desired result.
![[Pasted image 20240131205651.png]]![[Pasted image 20240131205703.png]]
Insertion in such databases would be tough because we would have to add each column at the end of previous columns hence the reason column databases are rarely used as production database but for analytics they are very common.
In data analysis they do most of the read stuff.
![[Pasted image 20240131210804.png]]if we are storing the data column wise then we know column values can repeat , we can use this to our advantage by compacting the same values.
![[Pasted image 20240131210929.png]]now say if we have a query that want number of rows with value p, then only using one cell we can say we two such rows(2P).
https://www.youtube.com/watch?v=Vw1fCeD06YI

Recommendation systems use graph databases e.g neo4j
![[Pasted image 20240131211450.png]]
healthcare device like apple watch keep sending data to system after some interval. Server keep ingesting the data and later shows user the graph. so lot of data is coming and we want to store it sorted according to the time because recent data is more important to us.
queries like give me the number of steps Naman had taken between 1 pm to 2pm.

### CASE STUDIES 

 **Twitter-HashTag data storage**

Situation:

- With a hashtag, you store the most popular or latest tweets.
    
- Also, there is a need to fetch the tweets in incremental order, for example, first 10 tweets, then 20 tweets and so on. 
    
- As you scroll through the application, fetch requests are submitted to the database.
    
![[Pasted image 20240201003839.png]]
**RDBMS :-** for RDBMS writes are coming too fast, RDBMS has to store the data in disk as well.

**Key-Value DB** is not a good choice.

- The problem with Key-Value DB is that corresponding to a particular hashtag(key), all the tweets associated with that tweet will be fetched.e.g key hashtag India will fetch all the tweets related to it, but we want only the recent most popular tweets. Because key value pair does not allow query within the value hence can't fetch latest tweets.
    
- Even though the need is only 10 tweets, the entire 10000 tweets are fetched. This will lead to delay in loading tweets and eventually bad user experience.

**Document DB:-** data is structured here as all tweets will have same attributes.
    ![[Pasted image 20240201004346.png]]
**Column-Family** is a better choice
* Here writes are append only and column DB handles such types of writes very fast.

- Let’s make the tweet a sharding key. Now, there can be column families such as Tweets, Popular Tweets, etc.
    
- When the posts related to a tweet are required, you only need to query the first X entries of the tweets column family.
    
- Similarly, if more tweets are required, you can provide an offset, and fetch records from a particular point.


### Live scores of Sports/Matches

Situation:
- Given a recent event or match, you have to show only the ongoing score information.

![[Pasted image 20240201005239.png]]
**Key-Value DB** is the best choice

- In this situation, Key-Value DB is the best as we simply have to access and update the value corresponding to a particular match/key.
    
- It is very light weight as well.


### Current Location of Cab in Uber-like Application

Situation:

- Uber needs to show the live location of cabs. How to store the live location of cabs?

**If location history is needed:** Column-Family DB is the best choice

- We can keep the cab as a sharding key and a column family: Location.
    
- Now, we have to simply fetch the first few records of the Location column family corresponding to a particular cab.
    
- Also, new records need to be inserted into the Location column family.
    
**If location history is not needed:** Key-Value DB is the best choice:

- If only the current location is needed, Key-Value makes a lot more sense.
    
- Simply fetch and update the value corresponding to the cab (key).
    
