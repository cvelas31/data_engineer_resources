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

-----------

# Relational Databases

**SUMMARY:** 
What we learned:
What makes a database a relational database and Codd’s 12 rules of relational database design
The difference between different types of workloads for databases OLAP and OLTP
The process of database normalization and the normal forms.
Denormalization and when it should be used.
Fact vs dimension tables as a concept and how to apply that to our data modeling
How the star and snowflake schemas use the concepts of fact and dimension tables to make getting value out of the data easier.

## Definitions
- Database: Set of related data and is organized
- Database Management System: Acces to the data is provided by this software. proveides access to database.

### Rule 1: The information rule:
All information in a relational database is represented explicitly at the logical level and in exactly one way – by values in tables.


## Importance of Relational Databases:
- Standardization of data model: Once your data is transformed into the rows and columns format, your data is standardized and you can query it with SQL
- Flexibility in adding and altering tables: Relational databases gives you flexibility to add tables, alter tables, add and remove data.
- Data Integrity: Data Integrity is the backbone of using a relational database. Data typing and formats
- Structured Query Language (SQL): A standard language can be used to access the data with a predefined language.
- Simplicity : Data is systematically stored and modeled in tabular format.
- Intuitive Organization: The spreadsheet format is intuitive but intuitive to data modeling in relational databases.

### Online Analytical Processing (OLAP):
Databases optimized for these workloads allow for complex analytical and ad hoc queries, including aggregations. These type of databases are optimized for reads.

### Online Transactional Processing (OLTP):
Databases optimized for these workloads allow for less complex queries in large volume. The types of queries for these databases are read, insert, update, and delete.

The key to remember the difference between OLAP and OLTP is analytics (A) vs transactions (T). If you want to get the price of a shoe then you are using OLTP (this has very little or no aggregations). If you want to know the total stock of shoes a particular store sold, then this requires using OLAP (since this will require aggregations).

Ex: 

Agreggations and analytics -- OLAP queries

Price or gather infromation -- OLTP queries

## Structuring Database
### Normalization
To reduce data redundancy and increase data integrity. The answer of a query is the correct answer (Integrity)
Feels natural. Reduce copies. Able to update data only in one place.

**Objective**
- To free the database from unwanted insertions, updates and deletion dependencies. (Update data only in just one place)
- To reduce the need for refactoring the database as new types of data are introduced. If new columns or data. Only add a table with a foreign key.
- To make the relational model more informative to users. (Real life concepts, intuitive)
- To make the database neutral to the query statistics. Not design tables for particular queries. Just have properly the information.

**Process**
- How to reach First Normal Form (1NF):
    - Atomic values: each cell contains unique and single values
    - Be able to add data without altering tables
    - Separate different relations into different tables
    - Keep relationships between tables together with foreign keys
- Second Normal Form (2NF):
    - Have reached 1NF
    - All columns in the table must rely on the Primary Key
- Third Normal Form (3NF):
    - Must be in 2nd Normal Form
    - No transitive dependencies
    - Remember, transitive dependencies you are trying to maintain is that to get from A-> C, you want to avoid going through B.
- When to use 3NF:
    - When you want to update data, we want to be able to do in just 1 place. We want to avoid updating the table in the Customers Detail table (in the example in the lecture slide).

### Denormalisation
Must be done in read heavy workloads to increase performance. 
Not natural. Duplicate copies of the data for performance reasosns. This tables are going to be focused according to the query

JOINS on the database allow for outstanding flexibility but are extremely slow. If you are dealing with heavy reads on your database, you may want to think about denormalizing your tables. You get your data into normalized form, and then you proceed with denormalization. So, denormalization comes after normalization.

**Logical Design Change**
- The designer is incharge of keeping data consistent
- Reads will be faster (select)
- Writes will be slower (Insert, update, delete)

## Fact and Dimension Tables
The following image shows the relationship between the fact and dimension tables for the example shown in the video. As you can see in the image, the unique primary key for each Dimension table is included in the Fact table.

**Fact tables**
Fact tables constists of the measurements, metrics or facts of a business process. Ex: Consumer ID

**Dimension table**
A structure that categorizes facts and measures in order to enable users to answer business questions. Dimensios are people, products, place and time.

In this example, it helps to think about the Dimension tables providing the following information:

- Where the product was bought? (Dim_Store table)
- When the product was bought? (Dim_Date table)
- What product was bought? (Dim_Product table)
The Fact table provides the metric of the business process (here Sales).
- How many units of products were bought? (Fact_Sales table)

![Imagen1][fact_dimension]

If you are familiar with Entity Relationship Diagrams (ERD), you will find the depiction of STAR and SNOWFLAKE schemas in the demo familiar. The ERDs show the data model in a concise way that is also easy to interpret. ERDs can be used for any data model, and are not confined to STAR or SNOWFLAKE schemas. Commonly available tools can be used to generate ERDs. However, more important than creating an ERD is to learn more about the data through conversations with the data team so as a data engineer you have a strong understanding of the data you are working with.

### Implementing different schemas
- **STAR SCHEMA**: Is the simplest style of data mart schema. Consists of one or more fact tables referencing any number of dimension tables.
    - Star shape
    - A fact table is at its center. 
    - Dimension table surrounds the fact table representing the star's points.
    - **Benefits**:
        - Denormalized
        - Simplifies queries
        - Fast aggregations
    - **Drawbacks**:
        - Issues that come with denormalization
        - Data integrity
        - Decrease query flexibility
        - Many to many relationship

- **SNOWFLAKE SCHEMA**: Logical arrangement of tables in a multidimensional database represented by centralized fact tables which are connected to multiple dimensions.

### Snowflake vs Star
- Star Schema is a special, simplified case of the snowflake schema
- Star schema doen not allow for one to many relationships while snowflake schema does
- Snowflake schema is more normalized than Star schema but only in 1NF or 2NF

# Data Definitions and Constraints
The CREATE statement in SQL has a few important constraints that are highlighted below

## NOT NULL
The NOT NULL constraint indicates that the column cannot contain a null value.
Here is the syntax for adding a NOT NULL constraint to the CREATE statement:

```sql
CREATE TABLE IF NOT EXISTS customer_transactions (
    customer_id int NOT NULL, 
    store_id int, 
    spent numeric
);
```
You can add NOT NULL constraints to more than one column. Usually this occurs when you have a COMPOSITE KEY, which will be discussed further below.

Here is the syntax for it:
```sql
CREATE TABLE IF NOT EXISTS customer_transactions (
    customer_id int NOT NULL, 
    store_id int NOT NULL, 
    spent numeric
);
```

## UNIQUE
The UNIQUE constraint is used to specify that the data across all the rows in one column are unique within the table. The UNIQUE constraint can also be used for multiple columns, so that the combination of the values across those columns will be unique within the table. In this latter case, the values within 1 column do not need to be unique.

Let's look at an example
```sql
CREATE TABLE IF NOT EXISTS customer_transactions (
    customer_id int NOT NULL UNIQUE, 
    store_id int NOT NULL UNIQUE, 
    spent numeric 
);
```
Another way to write a UNIQUE constraint is to add a table constraint using commas to separate the columns.
```sql
CREATE TABLE IF NOT EXISTS customer_transactions (
    customer_id int NOT NULL, 
    store_id int NOT NULL, 
    spent numeric,
    UNIQUE (customer_id, store_id, spent)
);
```

## PRIMARY KEY
The PRIMARY KEY constraint is defined on a single column, and every table should contain a primary key. The values in this column uniquely identify the rows in the table. If a group of columns are defined as a primary key, they are called a composite key. That means the combination of values in these columns will uniquely identify the rows in the table. By default, the PRIMARY KEY constraint has the unique and not null constraint built into it.

Let's look at the following example:
```sql
CREATE TABLE IF NOT EXISTS store (
    store_id int PRIMARY KEY, 
    store_location_city text,
    store_location_state text
);
```
Here is an example for a group of columns serving as composite key.
```sql
CREATE TABLE IF NOT EXISTS customer_transactions (
    customer_id int, 
    store_id int, 
    spent numeric,
    PRIMARY KEY (customer_id, store_id)
);
```

More in the [PostgreSQL documentation](https://www.postgresql.org/docs/9.4/ddl-constraints.html)

## UPSERT
In RDBMS language, the term upsert refers to the idea of inserting a new row in an existing table, or updating the row if it already exists in the table. The action of updating or inserting has been described as "upsert".

The way this is handled in PostgreSQL is by using the INSERT statement in combination with the ON CONFLICT clause.

## INSERT
The INSERT statement adds in new rows within the table. The values associated with specific target columns can be added in any order.

Let's look at a simple example. We will use a customer address table as an example, which is defined with the following CREATE statement:
```sql
CREATE TABLE IF NOT EXISTS customer_address (
    customer_id int PRIMARY KEY, 
    customer_street varchar NOT NULL,
    customer_city text NOT NULL,
    customer_state text NOT NULL
);
```

Let's try to insert data into it by adding a new row:

```sql
INSERT into customer_address (
VALUES
    (432, '758 Main Street', 'Chicago', 'IL'
);
```

Now let's assume that the customer moved and we need to update the customer's address. However we do not want to add a new customer id. In other words, if there is any conflict on the customer_id, we do not want that to change.

This would be a good candidate for using the ON CONFLICT DO NOTHING clause.

```sql
INSERT INTO customer_address (customer_id, customer_street, customer_city, customer_state)
VALUES
 (
 432, '923 Knox Street', 'Albany', 'NY'
 ) 
ON CONFLICT (customer_id) 
DO NOTHING;
```

Now, let's imagine we want to add more details in the existing address for an existing customer. This would be a good candidate for using the ON CONFLICT DO UPDATE clause.

```sql
INSERT INTO customer_address (customer_id, customer_street)
VALUES
    (
    432, '923 Knox Street, Suite 1' 
) 
ON CONFLICT (customer_id) 
DO UPDATE
    SET customer_street  = EXCLUDED.customer_street;
```

-----



[fact_dimension]: ./images/facts_dimension_tables.png
