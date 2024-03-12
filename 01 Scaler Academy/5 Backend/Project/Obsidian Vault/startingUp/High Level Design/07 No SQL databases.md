![[Pasted image 20240128175421.png]]

https://docs.google.com/document/d/1CfwsMMw8NTn2zavVokiYG08EH648Gsd1zJ7aAM7NvS4/edit
# SQL Database
SQL databases are relational databases which consist of tables related to each other and every table has a fixed set of columns. You can query across tables to retrieve related information.

Features of SQL Databases:
## Normalization

One of the requirements of SQL databases is to store the data in normalized form to avoid data redundancy and achieve consistency across tables. For example, let’s assume two tables are storing a particular score and one of the scores gets changed due to an update operation. Now, there will be two different scores at two different tables leading to confusion as to which score should be used.

Hence, the data should be normalized to avoid this data redundancy and trust issue.
(In sql we won't have duplicate data so consistency in ACID is different from consistency of CAP because in distributes systems it's ok to have duplication of the data)
![[Pasted image 20240128175736.png]]
## ACID Transactions

ACID stands for Atomicity, Consistency, Isolation and Durability.

- Atomicity means that either a transaction must be all or none. There should not be any partial states of execution of a transaction. Either all statements of a transaction are completed successfully or all of them are rolled back.
    
- Consistency refers to the property of a database where data is consistent before and after a transaction is executed. It may not be consistent while a transaction is being executed, but it should achieve consistency eventually.
    
- Isolation means that any two transactions must be independent of each other to avoid problems such as dirty reads.
    
- Durability means that the database should be durable, i.e. the changes committed by a transaction must persist even after a system reboot or crash.
    

Let’s understand this with the help of an example. 

Let’s say Rohit wants to withdraw Rs 1000 from his bank account. This operation depends on the condition that Rohit’s bank balance is greater than or equal to 1000 INR. Hence the withdrawal essentially consists of two operations:

- Check if the bank balance is greater than or equal to 1000 INR.
    
- If yes, perform a set operation: Balance = Balance - 1000 and disperse cash.
    
Now, imagine these operations are done separately in an app server. Let’s assume that Rohit’s bank balance is 1500 INR. And the first operation was completed successfully with a yes. Now, when the second operation is performed, there are chances that some other withdrawal request of 1000 INR has already changed Rohit’s bank balance to 500 INR.

Now, if the second operation is performed, it would set Rohit’s bank balance to -500 which does not make sense. Hence, if the database does not guarantee atomicity and isolation, these kinds of problems can happen when multiple requests attempt to access (and modify) the same node.

Now, when Rohit makes a request to withdraw 1000 INR from his account, both these operations represent a single transaction. The transaction either succeeds completely or fails. There won’t be any race conditions between two transactions. This is guaranteed by a SQL database.

![[Pasted image 20240128181000.png]]
* Redis do not have D of ACID(because it is storing in in-memory) that's how it is able to achieve both fast writes and fast reads.
* Mongo-DB has all the ACID properties that's why it is slow. 
* SQL databases are designed to work upon a single machines

*NoSQL databases are essentially databases that diverge from traditional SQL databases by intentionally omitting certain ACID properties(constraints). They are optimized to operate efficiently in distributed systems, offering flexibility and scalability for handling large volumes of data and diverse data models.*
# Shortcomings of SQL Databases

**Fixed Schema might not fit every use case**

Let’s design the schema for an e-commerce website and just focus on the Product table. There are a couple of pointers here:

- Every product has a different set of attributes. For example, a t-shirt has a collar type, size, color, neck-type, etc.. However, a MacBook Air has RAM size, HDD size, HDD type, screen size, etc. 
    
- These products have starkly different properties and hence couldn’t be stored in a single table. If you store attributes in the form of a string, filtering/searching becomes inefficient.
    
- However, there are almost 100,000 types of products, hence maintaining a separate table for each type of product is a nightmare to handle. 

* And even if we have only one big table then most of the attribute values would be NULL.
![[Pasted image 20240128182404.png]]
SQL is designed to handle millions of records within a few tables and not millions of tables itself.

Hence, there is a requirement of a flexible schema to include details of various products in an efficient manner.

![[Pasted image 20240128183206.png]]

if you are building a system where you do not have the requirement to do joins across different machines then SQL is the goto choice .

what if data is huge ?
**NORMALIZATION** where we try to put the data in such a way that every data is present across one machine , every data is present at one place. but if the size of the data is huge then it's not possible to fit it inside single machine :- Ideally we would try to split data in a way that SQL DBs could still work and we know we use Sharding key to split our data , so in further section we will try to come up with good practices of selecting a sharding key.

![[Pasted image 20240128183709.png]]
**Massenger application (FB, whatsApp)** :- let's say we have Massenger application (FB, whatsApp), now let's say we have to store information about the messages so we will have a table called Messages.
![[Pasted image 20240128184734.png]]now say we have lot of message so we would have to divide the data , so which of the above columns can be chosen as the sharding key ?

**SenderId :-** All of the messages that are sent by Naman and Rohit to anyone are in machine A and by Megha, Prakash and Ashish are in B and so on.

now let's say Naman has opened his whatsApp he will see all of the messages that are sent to him. but what is the cost of this according to our sharding key? according to our key Naman can receive messages from B,C,D.. means we would have to query multiple machines because receiver Naman is in machine A while Sender can be in any other machine

now let's say Naman is chatting with Megha , now all the messages that are sent by Naman would be in machine A and by Megha would be in B , so we would have to query across two different machines.

so Sender Id is obviously not a good sharding key.

**Time :-** All the messages sent today are inside A , yesterday are in B and so on...

One big problem with this is we would have to move the data daily, and another is the load on different DBs is not uniform,  if Naman open his chats he would see chats received today not the day before yesterday etc 

so we should chose a Sharding key :- 
* Makes our query fast , ideally only one DB machine yo go to.
* The load across the shards should be uniform.
![[Pasted image 20240129205759.png]]
* For each pair(Sender , Receiver) or conversation we create an ID say conversationID , then all the messages of that conversation would be inside the single machine. Thus all of the messages of the particular conversation can be found in one machine
* The other good option can be Composite key of SenderId and ReceiverId

To make loading all of the chats from Sender Naman we can have a separate table called Conversations where for every conversation we have an id , senderId and receiverId . *we can use different sharding keys for different tables.* 

![[Pasted image 20240129211135.png]]
Just focus on the messages table for now, rest we will cover later in FB case study.

**BANK SYSTEM** :- let's say we have the Account table with following attributes and the type of operations shown in figure.
![[Pasted image 20240129211719.png]]

1. To get the balance of an account i should know in which shard particular account reside so in my sharding key accountId will be there in some capacity or else we would have to check all the machines to check which machine contains the information about the account. so accountId seems natural choice.
2. To get the history of transaction of an account it would be better if all the transaction of particular account are present inside the same machine.Thus here again accountId is good idea.

**UBER :-**
![[Pasted image 20240130000314.png]]

is Lat and long good choice for Sharding key ? **NO** because it can be possible that two cars that are close to each other will surely have different Lat and Long and they might go in different machines.
**CITY_ID** if all of the cars of a city are present in the same machine then i can goto that particular shard and find the nearest car to the user.

*Google maps and Uber works the same way as tinder works*

**Slack :-**
![[Pasted image 20240130011956.png]]

**Workspace** cannot be the option because workspace can be too big to fit in one machine cause it can contain too many messages.It may overflow the DB itself.
*Sharding key should not overflow a DB*
**groupId** This is exactly same as conversationId of whatsApp

**IRCTC :-**
![[Pasted image 20240130012312.png]]

* if two ticket ids are same then number of people corresponding to that will also be same like ticket id 123456 has 4 people then ticket id 123456 will also have 4 people because it is the same ticket xd. so 4th option reduces to trainId + ticketId; so now our 4th option is saying all tickets with same trainId and same ticketId are in one machine. so it may happen that for same train one ticket is present in machine A and other on machine B. rather we want all tickets of same train to be together.

* 3rd option cannot be uniform Delhi railway station may overflow also.

* 2nd option is good but 1st option is even better. it means for all the tickets if train t1 on particular date those all tickets will be present in one machine.

## Types of No SQL DBs

![[Pasted image 20240130014424.png]]