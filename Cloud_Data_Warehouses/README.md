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
The data warehouse is a system which includes the processes, the technologies and data representations that enables us tio support the analytical processes.
- A data warehouse is a copy of transactions data specifically structured for query and analysis.
- A data warehouse is a subject orientedm, integrated, and time-variant collection of data in support of management decisions
- Is a system that retrieves and consolidates data periodically from the source systems into a dimensional or normalized data store. It usually keeps years of history and is queried for busjiness intelligence or other analytical activities. It is typically updated in batches, not every time a transaction happens in the source system.

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

Star schema might be the appropiate way joins with dimensions onluy. Good for OLAP not OLTP

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








[//]: <> (Links and some external resources.)
[kimball]: ./Images/Kimballs_Architecture.png "Kimballs"
