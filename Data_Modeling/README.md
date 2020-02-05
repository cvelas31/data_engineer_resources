# Data Modeling
## Relational Databases
Organize data into one or more tables (or relations) of columns and rows. with a unique key identifying each row. Relational Database Management Systems (RDBMS)

SQL most used language
Ex: Oracly, Teradata, MySQL, PostgreSQL, SQlite 
*Database/Schema:** Collection of tables
*Tables/Relation:*  A groups of rows sharing the same labeled elements.
*Columsn/Attribute:* Labeled element

*Rows/Tuple:* Single Item

**Advantages**
- Easy to use
- Ability to do JOINS
- Ability to do aggregations and analytics
- Smaller Data Volumes
- Easier to change business requirements
- Flexibility for queries
- Modeling the data not modeling queries!
- Secondary Indexes (For quick searching)
- ACID Transactions -- data integrity
    - ACID Properties
        - ACID Transactions
        - Properties of database transactions intended to guarantee validity even in the event of errors or power failures.
        - Atomicity: The whole transaction is processed or nothing is processed. A commonly cited example of an atomic transaction is money transactions between two bank accounts. The transaction of transferring money from one account to the other is made up of two operations. First, you have to withdraw money in one account, and second you have to save the withdrawn money to the second account. An atomic transaction, i.e., when either all operations occur or nothing occurs, keeps the database in a consistent state. This ensures that if either of those two operations (withdrawing money from the 1st account or saving the money to the 2nd account) fail, the money is neither lost nor created. Source Wikipedia for a detailed description of this example.
        - Consistency: Only transactions that abide by constraints and rules are written into the database, otherwise the database keeps the previous state. The data should be correct across all rows and tables. Check out additional information about consistency on Wikipedia.
        - Isolation: Transactions are processed independently and securely, order does not matter. A low level of isolation enables many users to access the data simultaneously, however this also increases the possibilities of concurrency effects (e.g., dirty reads or lost updates). On the other hand, a high level of isolation reduces these chances of concurrency effects, but also uses more system resources and transactions blocking each other. Source: Wikipedia
        - Durability: Completed transactions are saved to database even in cases of system failure. A commonly cited example includes tracking flight seat bookings. So once the flight booking records a confirmed seat booking, the seat remains booked even if a system failure occurs. Source: Wikipedia.

**Disadvantages**
- Have large amounts of data: Relational Databases are not distributed databases and because of this they can only scale vertically by adding more storage in the machine itself. You are limited by how much you can scale and how much data you can store on one machine. You cannot add more machines like you can in NoSQL databases.
- Need to be able to store different data type formats: Relational databases are not designed to handle unstructured data.
- Need high throughput -- fast reads: While ACID transactions bring benefits, they also slow down the process of reading and writing data. If you need very fast reads and writes, using a relational database may not suit your needs.
- Need a flexible schema: Flexible schema can allow for columns to be added that do not have to be used by every row, saving disk space.
- Need high availability: The fact that relational databases are not distributed (and even when they are, they have a coordinator/worker architecture), they have a single point of failure. When that database goes down, a fail-over to a backup system occurs and takes time.
- Need horizontal scalability: Horizontal scalability is the ability to add more machines or nodes to a system to increase performance and space for data.

**PostgreSQL**
Open Source and uses SQL. 
-----

## No-Relational Databases or NoSQL Database
Simpler design, Simpler horizontal scaling and Finer control of availability. Data structures used are different than those in relational Database awhich make some operations faster

NoSQL means Not Only SQL and there are various types. Created to deal with the issues of relational ones. 

Common types:
- **Apache cassandra (Partition Row store):** Distributed by partitions and organized in rows columns
- **MongoDB (Document store):** Addition to key value look ups, retirves documents on its content
- **DynamDB (Key-Value store):** Collection of key value pairs
- **Apache HBAse (Wide Column Store):** Similar to tables but format of the column can vary fro row to row. Flexible schema
- **Neo4J (Graph Database):** Relationships between entities is more the focus, represented as nodes and edges.

### Apache Cassandra

#### Basics
- Keyspace: Collection of tables (Kind of database)
- Table: Group of partitions
- Rows: A single item
- Partition: Fundamental unit of acces;: Collection of rows, How data is distributed
- Primary Key: Primary key is made up of a partition key and clsutering columns
- Columns: *Clustering* and Data Columns, Labeled Element

Provides scalability and high availability without compromising performance. Linear Scalability and proven fault-tolerance on commodity hardware or cluod. Perfect platform for mission-critical data. Uses own query language CQL. (since Apache Cassandra is optimized for writes).

**When to use NoSQL Database**
- Large amount of data
- Need Horizontal scalability
- Need high throghput --fast reads
- Need a flexible schema
- Need high availability
- Different data types and formats
- users are distributed --low latency
- Built for Big Data

**When NOT to use a NoSQL Database?**
- When you have a small dataset: NoSQL databases were made for big datasets not small datasets and while it works it wasn’t created for that.
- When you need ACID Transactions: If you need a consistent database with ACID transactions, then most NoSQL databases will not be able to serve this need. NoSQL database are eventually consistent and do not provide ACID transactions. However, there are exceptions to it. Some non-relational databases like MongoDB can support ACID transactions.
- When you need the ability to do JOINS across tables: NoSQL does not allow the ability to do JOINS. This is not allowed as this will result in full table scans.
- If you want to be able to do aggregations and analytics
- If you have changing business requirements : Ad-hoc queries are possible but difficult as the data model was done to fix particular queries
- If your queries are not available and you need the flexibility : You need your queries in advance. If those are not available or you will need to be able to have flexibility on how you query your data you might need to stick with a relational database

**Caveats to NoSQL and ACID Transactions**
There are some NoSQL databases that offer some form of ACID transaction. As of v4.0, MongoDB added multi-document ACID transactions within a single replica set. With their later version, v4.2, they have added multi-document ACID transactions in a sharded/partitioned deployment.





