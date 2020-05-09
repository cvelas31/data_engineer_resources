# Cloud Data Warehouses
## Introduction
### What Is A Data Warehouse? A Business Perspective
You are in charge of a retailer’s data infrastructure. Let’s look at some business activities.

- Customers should be able to find goods & make orders
- Inventory Staff should be able to stock, retrieve, and re-order goods
- Delivery Staff should be able to pick up & deliver goods
- HR should be able to assess the performance of sales staff
- Marketing should be able to see the effect of different sales channels
- Management should be able to monitor sales growth
Ask yourself: Can I build a database to support these activities? Are all of the above questions of the same nature?
Let's take a closer look at details that may affect your data infrastructure.

- Retailer has a nation-wide presence → Scale?
- Acquired smaller retailers, brick & mortar shops, online store → Single database? Complexity?
- Has support call center & social media accounts → Tabular data?
- Customers, Inventory Staff and Delivery staff expect the system to be fast & stable → Performance
- HR, Marketing & Sales Reports want a lot information but have not decided yet on everything they need → Clear Requirements?
Ok, maybe one single relational database won’t suffice

### Data warehouse
The data warehouse is a system which includes the processes, the technologies and data representations that enables us to support the analytical processes.
- A data warehouse is a copy of transactions data specifically structured for query and analysis.
- A data warehouse is a subject oriented, integrated, and time-variant collection of data in support of management decisions
- Is a system that retrieves and consolidates data periodically from the source systems into a dimensional or normalized data store. It usually keeps years of history and is queried for business intelligence or other analytical activities. It is typically updated in batches, not every time a transaction happens in the source system.

#### Goals
- Simple to understand
- Performant
- Quality Assured
- Handles new questions well
- Secure

### Dimensional Modelling
- Easy to understand
- Fast analytical query performance

3rd normal form has expensive joins and not really well

Star schema might be the appropiate way joins with dimensions only. Good for OLAP not OLTP

#### Facts and Dimensions
**Fact Tables**
-  Record business events, like an order, a phone call, a book review.
- Fact tables columns record events recorded in quantifiable metrics like quantity of an item, duration of a call, a book rating.

**Dimension Tables**
- Record the context of the business events, e. g. who, what, where, why, etc.
- Dimension tables columns contain attributes like the store at which an item is purchased, or the customer who made the call, etc.

####  Facts or Dimension Dilemma
- For facts, if you're unsure if a column is factor or dimension, the simplest rule is that a fact is usually: **Numeric & Additive**

- Example facts: 
    - A comment on an article represents an event but we can not easily make a statistic out of its content per se (Not a good fact)
    - Invoice number is numeric but adding it does not make sense (Not a good fact)
    - Total amount of an invoice could be added to compoute total sales (A good fact)
- Example dimensions:
    - Data & Time are always a dimension
    - Physical locations and their attirbutes are good candidates dimensions
    - Human roles like customers and staff always good candidates for dimensions
    - Goods sold always good candidates for dimensions
 
 ##### DVD Rental Sample Database
 - To master the art of dimensional modelling, one needs to see lots of schemas and think  about how to design facts & dimensions from them
 - We will start by a relatively small example for a classical database sample for a DVD rentals shop (prior to the age of Netflix), called the Sakila sample database.
 - Q1: How easy is it for you to understand this database schema?
 - Q2: Can you spot candidates for fact tables
 - Q3: Can you spot candidates for dimension tables
 
 Star Schema is easier to understand.

 #### Naive ETL: From 3NF to ETL
 - Query the 3NF DB
    - Join tables togetehr
    - Change types
    - Add new columns
- Loading
    - Insert into facts and dimension tables

### DWH Architecture

#### Kimballs'Bus Architecture
![alt text][kimball]

#### Independetn Data Marts
![alt text][marts]
Data Marts. Has Facts and Dimension focus on one department or business process.
Independent ETL proccesses & dimensional models.
Problems is that with different ETLs it may not be consistent across departments.

#### Inmo's Corporate Information Factory (CIF)
![alt text][cif]
A big enterprise warehouse cleaned and organized.
Then create Data Marts from it. But as the source is same it is consistent.
There are 2 ETL process. Data Marts are mostly aggregated.

#### Hybrid Kimball Bus & Inmon CIF
![alt text][hybrid_cif]
Combined Kimballs and CIF. Not Data Marts. It would be Dimensions.

### OLAP CUBES
Aggregation acroos one or more dimensions of the facts.

Do grouping by Each Dimension using cubes in order to have almos all posible ways of searching, slicing, dicing, slicing, etc

Do roll ups and Dill downs (Move do aggreagtes or disaggretaes, example Day, Week, Month, District, City, Country)
OLAP cubes is a very convenient way for slicing, dicing and drilling down.
- How to serve it?
    - Pre-aggreagte the OLAP cubes and saves them on a special purpose non-relational databse (MOLAP)
    - Compute teh OLAP cubes on the fly from the existing relational databases where the dimensional model resides (ROLAP) (Popular way)

- Column format in ROLAP is faster!

## Data Warehouses on AWS

### On premise
- Think about heterogeneity, scalability, elasticity (grow and shrink amount of resources) of tools, technologies and processes.
- Need for diverse IT staff skills & multiple locations
- Cost of ownership

### Cloud
- Lower barrier entry
- May add as you need - it's ok to change your opinion
- Scalability & elasticity out of the box
- Operational cost might be high and heterogeneity/complexity won't disappear.

#### Dimensional model storage
- **Cloud managed** (Amazon RDS, Amazon DynamoDB, Amazon S3)
    - Re use of expertise
    - Way less IT staff for security, upgrades, etc. and way less OpEx
    - Deal with complexity with technqiues like infrastructure as code
    - SQL (AWS RDS, Amazon Redshift)
    - NO SQL
    - Files (S3)
- **Self-managed** (EC2 + Posytgresql, EC2 +  Cassandra, EC2 + Unix FS)
    - Always "catch-all" option is needed

#### Amazon REDSHIFT
## Implementing Data Warehouses on AWS
- **Data Sources**
Different types, skill sets, upgrades, locations, etc (High heterogeneity) (OLTP)
- **ETL**
Many process - a grid of machines with schedules and pipeline to copy data to DImensional Model
- **Dimensional Model (DWH)**
More resources need to be added as data increases. We have different workloads; some need one machine  and some many
- **BI apps and visualizations**
Hybrid environment

## Redshift technology
Cluster with Leader Node (Communication, optimizes queries), and compute nodes (Own cpu, memory and disk, divided into slices). A cluster with n slices, can process n partitions of tables simultaneoulsy.
Each slice is al least 1 cpu with dedicated storage and memory for the slice.
- Column oriented storage
- Best suited for storing OLAP workloads, summin over a long history
- Internally, it's a modified Postgresql
- Most relational databases execute multiple queries in parallel if they have access to many cores/servers
- However, every query is always executed on a single CPU of a single machine
- Acceptable for OLTP, mostly updates and few rows retrieval.   
- Massively parallel processing (MPP) databases parallelize the execution of one query on multiples CPUs/machines
- How? A table is partitioned and partitions are processes in parallel
- Amazon REDSHIFT is a cloud-managed, column-oriented, MPP databas
- Other examples include Teradata Aster, Oracle ExaData and Azure SQL


##### Architecture
Redshift cluster: 1 leader node 1+ compute nodes.
- Leader node:
    - Coordinates compute nodes
    - Handles external communication
    - Optimizes query execution
- Compute node:
    - Each with own CPU, memory and disk (determined by node type)
    - Scale up: get more powerful nodes
    - Scale out: get more nodes
- Node Slices:
    - Each compute node us logically divided into a number of slices
    - A cluster with n slices can process n partitions of tables simultanously. Ex: If we have a Redshift cluster with 4 nodes, each containing 8 slices, i.e. the cluster collectively offers 32 slices. What is the maximum number of partitions per table? R/ 32

**Example node types & slices**
*Computer optimized nodes*
- dc1 or dc2 those are fast. (NVMe-SD is almost same latency as Memory) Are for CPU and RAM
*Storage optimized nodes*
- ds2 instances. They are large in capacity. TB to PB.

Watch out for the cost it is per hour

## SQL To SQL ETL
![alt text][etl]
- To copy the results of a query to another table (e.g facts or dimension table) in the same database, we can easily use SELECT INTO.
```sql
SELECT fact_1, fact2
INTO newFactTable
FROM table X, Y
WHERE X.id=Y.fid x.v<>nul
GROUP BY Y.d
```
- But what do we do if we want to copy the results of a query to another table on a totally different database server?
```sql
SELECT fact_1, fact2
INTO OtherServer.newFactTable
FROM table X, Y
WHERE X.id=Y.fid x.v<>nul
GROUP BY Y.d
```
- If both servers are running the same RDBMS, that might be po  ssible, but harder between two completely different RDBMSs.
- And even if we can, we probably need to do some transformations, cleaning governance, etc.
- A general solution is putting an ETL server on the middle. An ETL server can:
    -  Talk to the source server and runs a SELECT query on the source DB server.
    - Stores the results in CSV files Needs Large Storage!!
    - INSERT/COPY the results in the destination DB server.
    ![alt text][awsetl]

## Redshift & ETL in Context
![alt text][etlcontext]
- To transfer data from S3 staging area to redshift use the copy command
- Inserting row by row is really really slow
- If the file is large:
    - It is better to break it up to multiple files
    - Ingest in Parallel
        - Either using a common prefix
        - Or a minifest file
- Other considerations
    - Better to ingest from the same AWS region (Same region for all)
    - Better to compress the all csv files
- One can also specifiy the delimiter to be used

**Prefix structure**
```sql
COPY target_table FROM 's3://bucket_name/key_prefix'
CREDENTIALS 'aws_iam_role=arn:aws:iam::45345452:role/dwhRole'
gzip DELIMITER ';' REGION 'us-west-2';
```
**Manifest file**
```json
{
    "entries": [
        {"url":"s3://bucket_name/path/2013-10-04-custdata", "mandatory":true},
        {"url":"s3://bucket_name/path/2013-10-05-custdata", "mandatory":true},
        {"url":"s3://bucket_name/path/2013-10-06-custdata", "mandatory":true},
        {"url":"s3://bucket_name/path/2013-10-07-custdata", "mandatory":true}
    ]
}
```
```sql
COPY customer FROM 's3://bucket_path/cust.manifest'
IAM_ROLE 'arn:aws:iam::45345452:role/dwhRole'
manifest;
```

### Redshift ETL Automatic Compression Optimization
- The optimal compression strategy for each column type is different, this is done in  the schema
- redshift gives the user control over the compression of each column
- The COPY command makes automatic best-effort compression decisons for each column

### ETL from Other Sources
- It is also possible to ingest directly using ssh from EC2 machines
- Other than that:
    - S3 needs to be used as a staging area
    - Usually and EC2 ETL worker needs to run the ingestion jobs orchestrated by a dataflow product like Airflow, Luigi, Nifi, StreamSet or AWS Data Pipeline

### ETL out of Redshift
- Redshift is accesible, like any relational databse, as a JDBC/ODBC source
    - Naturally used by BI apps
- However, we may need to extract data out of Redshift to preaggregated OLAP Cubes
```
UNLOAD ('select * from venue limit 10')
to 's3://mybucket/venue_pipe_'
iam_role 'arn:aws:iam::232083023283:role/MyRole
```
There are write credentials
Sometimes in other languages is COPY TO instead of UNLOAD

## Building A Redshift Cluster
- Look for Redshift
- Quick launch
- Type of machine used, select number of nodes
- Fill info. and create cluster.
- Go to query editor, tehre you can do the SQL statements or queries
- We need to set up a Role (Who  is the  one accessing S3) and we need to open Port to have access from outside.
- The cluster is only accesible from the VPC

### Infrastructe as code (IaC)
- Create infrastructure from code
- Lets automate things
- IaC is border line between dataEng/devOps
- aws-cli: Like bash
- aws sdk (Using python or programming languages)
- Amazon Cloud Formation: using json os config files. Stack of things. If stack launches it worked. Atomicity 

### Optimizing table design
- When a table is partitioned up into many  pieces and distributed across slices in differnete machines, this is done blindly
- If  one has  an idea about the frequent access pattern of  a table, one  can  choose a more clever strategy
- The 2 possible strategies are:
    - Distribution Style
    - Sorting Key

#### Distribution Style
- **Even Distribution:**
![alt text][disteven]
    - Round-robin over all slices to achieve load-balancing
    - Good if a table won't be joined
    - Split table into N chunks according to number of cpus
    - When joining needs lot of shuffling (Like spark)
- **All Distribution:**
![alt text][distall]
    - Small tables could be replicated on all slices to speed up joins
    - Used frequently for Dimension tables
    - AKA broadcasting
    - Same table in all cpus
- **Auto Distribution:**
    - Leave decision to redshift
    - "Small enough" tables are distributed with an ALL strategy
    - Large  tables are distributed even strategy
- **Key Distribution:**
![alt text][distkey]
    - Rows having similar values (keys) are placed in the  same slice
    - Not evenly  distributed (depends on keys)
    - This can lead to skewed distribution according to frequency
    - However, very useful when a dimension table is too big to be distributed with ALL strategy. In that case, we distribute both the fact  table and the dimension table using same dist key.
    - If two tables are distributed on the joining keys, redshift collocates the rows from both tables on the  same slices.
    - Useful when dimension table is too big.
    - Reduces the  memory used when coopying.
    - Need sintax  with `distkey`
- **Sorting key:**
![alt text][sortkey]
    - One can define its columns as sort key
    - Upon loading, rows  are sorted before distribution to slices.
    - Minimizes the query time  since each nodde already has contiguos ranges of rows based on the sorting key
    - Useful for columns that are used  frequently  in sorting like the date dimension and its corresponding foreign key in the fact table
    - Need sintax  with `sortkey` (Can have both sort and dist keys)

# Conslusion
- The data   flow tools deserve  a little bit more focused attention
- Table design, ETL, context, DWH on AWS, Redshift




[//]: <> (Links and some external resources.)
[kimball]: ./Images/Kimballs_Architecture.png "Kimballs"
[marts]: ./Images/Independent_data_marts_architecture.png "Marts"
[cif]: ./Images/CIF.png "CIF"
[hybrid_cif]: ./Images/Hybrid_cif.png "hybrid_cif"
[etl]: ./Images/ArchitectureETL.png "General Architecture"
[awsetl]: ./Images/AWSETL.png "AWS ETL"
[etlcontext]: ./Images/RedshiftETL.png "Redshift ETL"
[disteven]: ./Images/disteven.png "EVEN Distribution"
[distall]: ./Images/distall.png "ALL Distribution"
[distkey]: ./Images/distkey.png "DISTKEY"
[sortkey]: ./Images/sortkey.png "SORTKEY"