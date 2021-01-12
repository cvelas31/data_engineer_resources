# Data Streaming Udacity

## Understanding Stream Processing
In computing, a stream is typically thought of as a potentially unbounded sequence.

Stream Processing is the act of performing continual calculations on a potentially endless and constantly evolving source of data.

Stream Processing applications perform calculations on Data Streams. Data Streams consist of a potentially endless stream of immutable data.

Immutable data does not change -- once the data has been placed in the data stream it can never be updated. Another data entry can be placed in the stream that supersedes the previous data entry if necessary.

Data sent to data streams is typically small, less than 1MB in size.

The data throughput to data streams is highly variable. Some streams will receive thousands or tens of thousands of records per second, and some will receive one or two records per hour.

- Stream Processing acts on potentially endless and constantly evolving immutable data contained in data streams.
- Once data have been placed in a data stream, they cannot be modified. We must place a new record in the stream to override the existing data.
- Finally, data in data streams is typically less than 1MB in size and the data volume may vary from a few records an hour to thousands of requests per second.
- Stream processing allows companies to process data as it's generated and not hours after the fact as is common with batch processing.

### What is an event
- An immutable fact regarding something that occured within our software system

## Example of usages
- Log analysis - New Relic Example - APM, Failure Prediction and Debugging. How to process huge amount of data.
- Web Analytics - Mix Panel - Track user actions, clicks page views.
- Right sharing application - Real Time Pricing - Adjusts to environmental factors and instantaneous demand. (Real time ML and model pricing recommendation) Pricing according to demand, supply, events (soccer), weather, etc.
- Financial Analysis - Finance, tweets, news, etc.
- Finding patterns and meaningful data in disparate log messages in a microservices architecture
- Tracking user-engagement in real time with streaming website analytics
- Real-time pricing in ride-sharing applications based on demand and environmental conditions
- Stock buying/selling based on price, news, and social media sentiment

### Batch Processing
- Runs on a scheduled basis
- May run for a longer period of time and write results to a SQL-like store
- May analyze all historical data at once
- Typically works with mutable data and data stores

### Stream Processing
- Runs at whatever frequency events are generated
- Typically runs quickly, updating in-memory aggregates
- Stream Processing applications may simply emit events themselves, rather than write to an event store
- Typically analyzes trends over a limited period of time due to data volume
- Typically analyzes immutable data and data stores

**Batch and Stream processing are not mutually exclusive. Batch systems can create events to feed into stream processing applications, and similarly, stream processing applications can be part of batch processing analyses.**

## Components of a Stream Processing Solution

### Streaming Data Store
- May look like a message queue, as is the case with Apache Kafka
- May look like a SQL store, as is the case with Apache Cassandra
- Responsible for holding all of the immutable event data in the system
- Provides guarantee that data is stored ordered according to the time it was produced
- Provides guarantee that data is produced to consumers in the order it was received
- Provides guarantee that the events it stores are immutable and unchangeable

### Stream Processing Application and Framework
- Stream Processing applications sit downstream of the data store
- Stream Processing applications ingest real-time event data from one or more data streams
- Stream Processing applications aggregate, join, and find differences in data from these streams
- Common Stream Processing Application Frameworks in use today include:
  - Confluent KSQL
  - Kafka Streams
  - Apache Flink
  - Apache Samza
  - Apache Spark Structure Streaming
  - Faust Python Library

### Further Optional Reading on Message Queues
- [RabbitMQ](https://www.rabbitmq.com/)
- [ActiveMQ](https://activemq.apache.org/)

## Benefits of Stream Processing
- *Good Aplications focus on event generation, rather than data flow o r something similar. This is done to isolate and be agnostic on what is going to be done.*
- Faster for scenarios where a limited set of recent data is needed
- More scalable due to distributed nature of storage
- Provides a useful abstraction that decouples applications from each other
- Allows one set of data to satisfy many use-cases which may not have been predictable when the dataset was originally created
- Built-in ability to replay events and observe exactly what occurred, and in what order, provides more opportunities to recover from error states or dig into how a particular result was arrived at

## Glosary
- **Stream** - An unbounded sequence of ordered, immutable data
- **Stream Processing** - Continual calculations performed on one or more Streams
- **Immutable Data** - Data that cannot be changed once it has been created
- **Event** - An immutable fact regarding something that has occurred in our system.
- **Batch Processing** - Scheduled, periodic analysis of one or more groups of related data.
- **Data Store** - A generic place that holds data of some kind, like a message queue or data store
- **Stream Processing Application** - An application which is downstream of one or more data streams and performs some kind of calculation on incoming data, typically producing one or more output data streams
- **Stream Processing Framework** - A set of tools, typically bundled as a library, used to construct a Stream Processing Application
- **Real-time** - In relation to processing, this implies that a piece of data, or an event, is processed almost as soon as it is produced. Strict time-based definitions of real-time are controversial in the industry and vary widely between applications. For example, a Computer Vision application may consider real-time to be 1 millisecond or less, whereas a data engineering team may consider it to be 30 seconds or less. In this class when the term "real-time" is used, the time-frame we have in mind is seconds.
- **Append-only Log** - files in which incoming events are written to the end of the file as they are received
- **Change Data Capture (CDC)** - The process of capturing change events, typically in SQL database systems, in order to accurately communicate and synchronize changes from primary to replica nodes in a clustered system.
- **Log-Structured Storage** - Systems built on Append-Only Logs, in which system data is stored in log format.
- **Merge (Log Files)** - When two or more log files are joined together into a single output log file
- **Compact (Log Files)** - When data from one or more files is deleted, typically based on the age of data
- **Source (Kafka)** - A term sometimes used to refer to Kafka clients which are producing data into Kafka, typically in reference to another data store
- **Sink (Kafka)** - A term sometimes used to refer to Kafka clients which are extracting data from Kafka, typically in reference to another data store
- **Topic (Kafka)** - A logical construct used to organize and segment datasets within Kafka, similar to how SQL databases use tables
- **Producer (Kafka)** - An application which is sending data to one or more Kafka Topics.
- **Consumer (Kafka)** - An application which is receiving data from one or more Kafka Topics.

## Key concepts to remember about stream processing
- Stream processing applications consist of a stream data store and a stream processing application framework
- Stream processing solutions do not operate on a scheduled basis
- Stream processing solutions provide real-time insights based on event data
- Stream processing solutions are built around generic data events, allowing for flexibility in data processing and highly scalable applications
- Batch and stream processing solutions can coexist and feed into each other

## Data Streams are Append-Only Logs
### Append-only logs
- Append-only logs are text files in which incoming events are written to the end of the log as they are received.
- This simple concept -- of only ever appending, or adding, data to the end of a log file -- is what allows stream processing applications to ensure that events are ordered correctly even at high throughput and scale.
- We can take this idea a step farther, and say that in fact, streams are append-only logs.

### Log-structured streaming
- Log-structured streams build upon the concept of append-only logs. One of the hallmarks of log-structured storage systems is that at their core they utilize append-only logs.
- Common characteristics of all log-structured storage systems are that they simply append data to log files on disk.
- These log files may store data indefinitely, for a specific time period, or until a specific size is reached.
- There are typically many log files on disk, and these log files are merged and compacted occasionally.
- When a log file is merged it means that two or more log files are joined together into one log file.
- When a log file is compacted it means that data from one or more files is deleted. Deletion is typically determined by the age of a record. The oldest records are removed, while the newest stay.
- Examples of real world log-structured data stores: [Apache HBase](https://hbase.apache.org/), [Apache Cassandra](http://cassandra.apache.org/), [Apache Kafka](https://kafka.apache.org/)

### Log-Structured Storage
One of the key innovations over the past decade in computing has been the emergence of log-structured storage as a primary means of storing data.

# Kafka: A Stream Processing Tool
## Apache Kafka as a Stream Processing Tool
- Kafka is one of the most popular streaming data platforms in the industry today.
- Provides an easy-to-use message queue interface on top of its append-only log-structured storage medium
- Kafka is a log of events
- In Kafka, an event describes something that has occurred, as opposed to a request for an action to be performed
- Kafka is distributed by default
- Fault tolerant by design, meaning it is hard to lose data if a node is suddenly lost
- Kafka scales from 1 to thousands of nodes
- Kafka provides ordering guarantees for data stored within it, meaning that the order in which data is received is the order in which data will be produced to consumers
- Commonly used data store for popular streaming tools like Apache Spark, Flink, and Samza

[//]: <> (Links and some external resources.)
[Quora]: https://www.quora.com/What-is-the-difference-between-the-ETL-and-ELT
[airflow-diagram]: ./Images/airflow-diagram.png "airflow-diagram"
[how-airflow-works]: ./Images/how-airflow-works.png "how-airflow-works"
