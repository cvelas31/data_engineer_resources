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

### Kafka History
- Created at Linkedin to service internal stream processing needs
- Kafka is one of the Apache Foundation’s most popular projects
- Used widely in production. Some famous users include Uber, Apple, and Airbnb
- Creators of Kafka left LinkedIn to found Confluent, which now acts as the owner and leader of the Kafka project
- Jay Kreps, one of the core authors of Apache Kafka, named the system after Czech author Franz Kafka. Kreps, who enjoys Kafka’s work, thought the name was a good fit because Kafka was built to be a “system optimized for writing.”

### Kafka in Industry
- The term source is sometimes used to refer to Kafka clients which are producing data into Kafka, typically in reference to another data store
- The term sink is sometimes used to refer to Kafka clients which are extracting data from Kafka, typically in reference to another data store

How Uber uses Kafka:
- [The Uber Engineering Tech Stack Part 1](https://eng.uber.com/tech-stack-part-one/)
- [The Uber Engineering Tech Stack Part 2](https://eng.uber.com/tech-stack-part-one/)

# Kafka in Action

## Kafka Topics
- Used to organize and segment datasets, similar to SQL database tables
- Unlike SQL database tables, Kafka Topics are not queryable.
- May be created programmatically, from a CLI (Command Line Interface), or automatically
- Consist of key-value data in binary format

## Kafka Producers
- Send event data into Kafka topics
- Integrate with client libraries in languages like Java, Python, Go, as well as many other languages

## Kafka Consumers
- Pull event data from one or more Kafka Topics
- Integrate with Kafka via a Client Library written in languages like Python, Java, Go, and more
- By default only consume data that was produced after the consumer first connected to the topic. Historical data will not be consumed by default.

# Kafka CLI

## Commands:
- `kafka-topics`: Create delete describe or change a topic
  - `--create`: Create topic
  - `--delete`: 
  - `--describe`
  - `--list`
  - `--zookeeper`: **REQUIRED** Keeps configuration for the Kafka Cluster
  - `--partitions`:
  - `--replication-factor`:
  - `--alter`: Alter the number of partition of a topic
- `kafka-console-producer`: Connects to a data broker. Then you can send messages
  - `broker-list`: **REQUIRED** The Broker list string Ex: localhost:9092 (URL of Kafka Broker different from zookeeper)
  - `topic`: **REQUIRED** Topic id to produce messages to
- `kafka-console-consumer`: Connects to a data broker. By default would only read messages produced after it was created.
  - `topic`: **REQUIRED** Topic id to consume
  - `--bootstrap-server`: **REQUIRED** The broker list string. Ex: localhost:9092 (URL of Kafka Broker different from zookeeper). Also could be: PLAINTEXT://localhost:9092
  - `--from-beginning`: Would get all the messages from a topic

## Kafka in Action - Summary
- A Kafka Topic is how Kafka organizes and segments datasets
- A Kafka Producer is an application that emits event data into a Kafka Topic
- A Kafka Consumer is an application that pulls event data from one or more Kafka Topics
- How to use the Kafka CLI Tools, such as ``kafka-topics``, ``kafka-console-producer``, and ``kafka-console-consumer``
- How to use the ``confluent-kafka-python`` library to create a topic, producer, and consumer


# Lesson 2 - Apache Kafka in depth

## Glosary
- **Broker (Kafka)** - A single member server of the Kafka cluster
- **Cluster (Kafka)** - A group of one or more Kafka Brokers working together to satisfy Kafka production and consumption
- **Node** - A single computing instance. May be physical, as in a server in a datacenter, or virtual, as an instance might be in AWS, GCP, or Azure.
- **Zookeeper** - Used by Kafka Brokers to determine which broker is the leader of a given partition and topic, as well as track cluster membership and configuration for Kafka
- **Access Control List (ACL)** - Permissions associated with an object. In Kafka, this typically refers to a user’s permissions with respect to production and consumption, and/or the topics themselves.
- **JVM - The Java Virtual Machine** - Responsible for allowing host computers to execute the byte-code compiled against the JVM.
- **Data Partition (Kafka)** - Kafka topics consist of one or more partitions. A partition is a log which provides ordering guarantees for all of the data contained within it. Partitions are chosen by hashing key values.
- **Data Replication (Kafka)** - A mechanism by which data is written to more than one broker to ensure that if a single broker is lost, a replicated copy of the data is available.
- **In-Sync Replica (ISR)** - A broker which is up to date with the leader for a particular broker for all of the messages in the current topic. This number may be less than the replication factor for a topic.
- **Rebalance** - A process in which the current set of consumers changes (addition or removal of consumer). When this occurs, assignment of partitions to the various consumers in a consumer group must be changed.
- **Data Expiration** - A process in which data is removed from a Topic log, determined by data retention policies.
- **Data Retention** - Policies that determine how long data should be kept. Configured by time or size.
- **Batch Size** - The number of messages that are sent or received from Kafka
acks - The number of broker acknowledgements that must be received from Kafka before a producer continues processing
- **Synchronous Production** - Producers which send a message and wait for a response before performing additional processing
- **Asynchronous Production** - Producers which send a message and do not wait for a response before performing additional processing
- **Avro** - A binary message serialization format
- **Message Serialization** - The process of transforming an applications internal data representation to a format suitable for interprocess communication over a protocol like TCP or HTTP.
- **Message Deserialization** - The process of transforming an incoming set of data from a form suitable for interprocess communication, into a data representation more suitable for the application receiving the data.
- **Retries (Kafka Producer)** - The number of times the underlying library will attempt to deliver data before moving on
- **Consumer Offset** - A value indicating the last seen and processed message of a given consumer, by ID.
- **Consumer Group** - A collection of one or more consumers, identified by group.id which collaborate to consume data from Kafka and share a consumer offset.
- **Consumer Group Coordinator** - The broker in charge of working with the Consumer Group Leader to initiate a rebalance
- **Consumer Group Leader** - The consumer in charge of working with the Group Coordinator to manage the consumer group
- **Topic Subscription** - Kafka consumers indicate to the Kafka Cluster that they would like to consume from one or more topics by specifying one or more topics that they wish to subscribe to.
- **Consumer Lag** - The difference between the offset of a consumer group and the latest message offset in Kafka itself
- **CCPA** - California Consumer Privacy Act
- **GDPR** - General Data Protection Regulation

## Kafka Architecture
- Kafka servers are referred to as brokers
- All of the brokers that work together are referred to as a cluster
- Clusters may consist of just one broker, or thousands of brokers
- Apache Zookeeper is used by Kafka brokers to determine which broker is the leader of a given partition and topic
- Zookeeper keeps track of which brokers are part of the Kafka cluster
- Zookeeper stores configuration for topics and permissions (Access Control Lists - ACLs)
- ACLs are Permissions associated with an object. In Kafka, this typically refers to a user’s permissions with respect to production and consumption, and/or the topics themselves.
- Kafka nodes may gracefully join and leave the cluster
- Kafka runs on the Java Virtual Machine (JVM)

## Kafka Clustering
- Kafka servers are referred to as brokers and organized into clusters.
- Kafka uses Apache Zookeeper to keep track of topic and ACL(Permission) configuration, as well as determine leadership and cluster management.
- Usage of ZooKeeper means that Kafka brokers can typically seamlessly join and leave clusters, allowing Kafka to grow easily as its usage increases or decreases.
- Kafka stores data according to the topic as multiple text log files
- Kafka partitions (Higlighted are leaders of a partition) it has some replications
![kafka-partitions]
**Partitions Takeaways**
- Partitions are unit of parallelism
- Consumers may parallelize data from each partition
- Producers may paralelize data from each partition
- Partition assignment is done by hashing to distribute them evenly
- Reduces bottlenecks by involving multiple brokers

### Data Replication
- Data written in many brokers
- Partition leaders are the ones who handles petitions or requests, when a leader fails another broker is selected to be the leader
- Can't have more replicas than you have brokers
- Data replication incurs overhead
- Always enable replication if you can in a Production Cluster

### How Kafka Works - Summary
- A Kafka Broker is an individual Kafka server
- A Kafka Cluster is a group of Kafka Brokers
- Kafka uses Zookeeper to elect topic leaders and store its own configuration
- Kafka writes log files to disk on the Kafka brokers themselves
- How Kafka achieves scale and parallelism with topic partitions
- How Kafka provides resiliency and helps prevent data loss with data replication

## Kafka Topic in Depth
Kafka Topics are rich in configuration options. To get the most out of Kafka you will need to develop a strong understanding of how these options impact performance. This will include understanding how to replicate topics in Kafka.

### Topic configuration
- Data replication can be set on a per-topic basis
- A broker must be an "In Sync Replica" (ISR) to become leader
- Desired number of ISRs can be set on topics

### Partitioning Topics Tips and Equation
- The “right” number of partitions is highly dependent on the scenario.
- The most important number to understand is desired throughput. How many MB/s do you need to achieve to hit your goal?
- You can easily add partitions at a later date by modifying a topic.
- Partitions have performance consequences. They require additional networking latency and potential rebalances, leading to unavailability.
- Determine the number of partitions you need by dividing the overall throughput you want by the throughput per single consumer partition or the throughput per single producer partition. Pick the larger of these two numbers to determine the needed number of partitions.
  - ``# Partitions = Max(Overall Throughput/Producer Throughput, Overall Throughput/Consumer Throughput)``
  - Example from video, with 3 Producers and 5 Consumers, each operating at 10MB/s per single producer/consumer partition: Max(100MBs/(3 * 10MB/s), 100MBs/(5 * 10MB/s)) = Max(2) ~= *4 partitions needed*
- [Considerations in choosing the number of partitions](https://www.confluent.io/blog/how-choose-number-topics-partitions-kafka-cluster)
![topic_ordering]

### Naming Conventions
- No official or idiomatic pattern defined
- Kafka requires names <256 chars, [a-zA-Z0-9.-_]
- Name topics according to some consistent strategy
- Consistent naming leads to simpler consumption
- Naming conventions can help reduce confusion, save time, and even increase reusability.
- Recommendation:
<domain>.<model>.<event_type>
Ex: com.udacity.data_stream.lesson2.quiz.result
The important thing is to be consistent across all topics

### Data Management
- Data retention determines how long Kafka stores data in a topic.
  - [The retention.bytes, retention.ms settings control retention policy](https://kafka.apache.org/documentation.html#topicconfigs)
- When data expires it is deleted from the topic.
  - [This is true if cleanup.policy is set to delete](https://kafka.apache.org/documentation.html#topicconfigs)
- Retention policies may be time based. Once data reaches a certain age it is deleted.
  - [The retention.ms setting controls retention policy on time](https://kafka.apache.org/documentation.html#topicconfigs)
- Retention policies may be size based. Once a topic reaches a certain age the oldest data is deleted.
  - [The retention.bytes setting controls retention policy on time](https://kafka.apache.org/documentation.html#topicconfigs)
- Retention policies may be both time- and size-based. Once either condition is reached, the oldest data is deleted.
- Alternatively, topics can be compacted in which there is no size or time limit for data in the topic.
  - [This is true if cleanup.policy is set to compact](https://kafka.apache.org/documentation.html#topicconfigs)
- Compacted topics use the message key to identify messages uniquely. If a duplicate key is found, the latest value for that key is kept, and the old message is deleted.
- Kafka topics can use compression algorithms to store data. This can reduce network overhead and save space on brokers. Supported compression algorithms include: lz4, ztsd, snappy, and gzip.
  - [compression.type controls the type of message compression for a topic](https://kafka.apache.org/documentation.html#topicconfigs)
- Kafka topics should store data for **ONE type of event**, not multiple types of events. Keeping multiple event types in one topic will cause your topic to be hard to use for downstream consumers.

### Topic Creation
- **DO NOT CREATE AUTOMATIC TOPICS**
- Create them manually with the things as needed
- Write code to check if the desired topic exists
- Use bash scripts o terraform to create your topics.
#### Example:
```python
config={
  "cleanup.policy": "compact", # What to do with old logs. Delete old topics. Other option is compact
  "compression.type": "lz4", # Compression type for topics
  "delete.retention.ms": 100, # Marked for deletion how mucho to wait to delete
  "file.delete.delay.ms": 100, # Time to wait for delteing file in filesystem
  ...
}
```


# Kinesis
AWS Streaming. Based on **shards**.
Has producer and consumers.
A shard is the throughput unit, a single shard can handle 1Mb/sec or 1000 requests per second.

## Recommendations:
- Shard can be dynamically. You can add more sahrds easily, but you cannot reduce them easily.
- Uses partition keys (Always have more partition keys than shards) to send the data.
- Sends data accordning to the partition key.
- Make sure it is evenly distributed, will help.

### Producers
You can produce with the aws API with put_records or put_record.

### Consumers
Kinesis library
Event based using Lambda, may be useful to process it and sent it to another service with lambda.



### Optional Further Research in Kafka Topics
- [Kafka topic settings documentation](https://kafka.apache.org/documentation.html#topicconfigs)
- [Confluent blog post on Partitioning](https://www.confluent.io/blog/how-choose-number-topics-partitions-kafka-cluster)


  
[//]: <> (Links and some external resources.)
[Quora]: https://www.quora.com/What-is-the-difference-between-the-ETL-and-ELT
[kafka-partitions]: ./Images/Kafka_partitions.png "airflow-diagram"
[topic_ordering]: ./Images/topic_ordering.png "how-airflow-works"
