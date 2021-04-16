# Data Streaming Udacity

## Timely decisions
- Data loses value quickly over time
- Real time analysis are way more productive
![time_value_data]

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

## Glossary
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
- **acks** - The number of broker acknowledgements that must be received from Kafka before a producer continues processing
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
### Optional Further Research in Kafka Topics
- [Kafka topic settings documentation](https://kafka.apache.org/documentation.html#topicconfigs)
- [Confluent blog post on Partitioning](https://www.confluent.io/blog/how-choose-number-topics-partitions-kafka-cluster)

### Kafka Producers
- Synchronously and asynchronously send data to Kafka
- Use key configuration options, such as batch size, client identifiers, compression, and acknowledgements
- Specify data serializers

#### Synchronous Producer
- Blocks producer program until the broker has confirmed receipt
- Make sure data was succefully delivered
- Not common usage

#### Asynchronous Producer
- Maximizes throughput
- Most common usage
- Use callbacks to know when an error occured

#### Message Serialization
- Data sent to Kafka should be serialized into a format
- Kafka client can assist serialization
- Formats include binary, string, csv, json, avro.
- **Never change serialization type without a new topic**

#### Producer Summary Configuration
- All available settings for the `confluent_kafka_python` library can be found in the [librdkafka](https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md) configuration options. `confluent_kafka_python` uses `librdkafka` under the hood and shares the exact configuration options in this document.
- It is a good idea to always set the `client.id` for improved logging, debugging, and resource limiting
- The `retries` setting determines how many times the producer will attempt to send a message before marking it as failed
- If ordering guarantees are important to your application and you’ve also enabled retries, make sure that you set `enable.idempotence` to true
- Producers may choose to compress messages with the ``compression.type`` setting
Options are none, `gzip`, `lz4`, `snappy`, and `zstd`
Compression is performed by the producer client if enabled
- If the topic has its own compression setting, it must match the producer setting, otherwise the broker will decompress and recompress the message into its configured format.
- The `acks` setting determines how many In-Sync Replica (ISR) Brokers need to have successfully received the message from the client before moving on
- A setting of `-1` or `all` means that all ISRs will have successfully received the message before the producer proceeds
- Clients may opt to set this to 0 for performance reasons
- The diagram below illustrates how the topic and producer may have different compression settings. However, the setting at the topic level will always be what the consumer sees. ![diagram_compression]

#### Batching Configuration
- A producer doesn't send all data inmediately, batches all data generated according to some conditions.
- Messages may be batched on one or more of: time, count or size
- Kafka clients allow configuration of these batch settings
- Batch settings can be critical for producer performance

**Set configuration carefully on the producer, particullarly on the buffer side**

#### Kafka Producers - Summary
Kafka Producers are rich in options and configuration. In this section you’ve seen how to adapt your producer code to a wide-variety of real world situations through configuration.

Remember, no one set of settings works in all scenarios. If your producer application isn’t performing the way you expect, it’s worth revisiting your producer configuration to ensure that the settings make sense for the throughput level you are hoping to achieve.

#### Optional Further Reading on Kafka Producers
- `confluent-kafka-python`/`librdkafka` [Configuration Options](https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md)
- [Apache Documentation on Producer Configuration](https://kafka.apache.org/documentation/#producerconfigs)
- `confluent-kafka-python` [Producer class](https://docs.confluent.io/current/clients/confluent-kafka-python/index.html?highlight=serializer#producer)

### Kafka Consumers

**Key Points**
- `client.id` is an optional setting which is useful in debugging and resource limiting
- Poll for data to read data from Kafka
  - poll
  - consume
- Consumrs subscribe to one or more topics
- Subscribing to a topic that does not exists will create it with default settings (Not recommended)

#### Consumer Offsets - Key Points
- Kafka keeps track of what data a consumer has seen with offsets
  - Kafka stores offsets in a private internal topic
  - Most client libraries automatically send offsets to Kafka for you on a periodic basis
  - You may opt to commit offsets yourself, but it is not recommended unless there is a specific use-case.
  - Offsets may be sent synchronously or asynchronously (Recommended asynchronously)
  - Committed offsets determine where the consumer will start up
    - If you want the consumer to start from the first known message, [set auto.offset.reset to earliest]
    - This will only work the first time you start your consumer. On subsequent restarts it will pick up wherever it left off
    - If you always want your consumer to start from the earliest known message, you must manually assign your consumer to the start of the topic on boot

#### Example:
- `auto.offset.reset`: How to connect to the topic, pick where it left or all messages, only works the first time a consumrs connects to a topic. You pick up were it left.
- `on_assign` Callback on suscribe cna change offset assignment on partitions

#### Consumer Groups
A group id parameters must be set on consumers
- Consumer groups are clients consuming from the same topic
- A consumer of a consumer group can only see specific partitions
- **REBALANCE IS EXPENSIVE** The consumers enter to a halt/sleep state where they do not consume. Avoid unnecessary rebalancing.
- All Kafka Consumers belong to a Consumer group
- The group.id [parameter](https://docs.confluent.io/current/installation/configuration/consumer-configs.html#) is required and identifies the globally unique consumer group
- Consumer groups consist of one or more consumers
- Consumer groups increase throughput and processing speed by allowing many consumers of topic data. However, only one consumer in the consumer group receives any given message.
- If your application needs to inspect every message in a topic, create a consumer group with a single member
- Adding or removing consumers causes Kafka to rebalance
  - During a rebalance, a broker group coordinator identifies a consumer group leader
  - The consumer group leader reassigns partitions to the current consumer group members
  - During a rebalance, messages may not be processed or consumed

#### Consumer Subscriptions
- You subscribe to a topic by specifying its name
  - If you wanted to subscribe to com.udacity.lesson.views, you would simply specify the full name as ”com.udacity.lesson.views”
  - Make sure to set allow.auto.create.topics to false so that the topic isn’t created by the consumer if it does not yet exist
- One consumer can subscribe to multiple topics by using a regular expression
  - The format for the regular expression is slightly different. If you wanted to subscribe to com.udacity.lesson.views.lesson1 and com.udacity.lesson.views.lesson2 you would specify the topic name as ”^com.udacity.lesson.views.*”
  - The topic name must be prefixed with ”^” for the client to recognize that it is a regular expression, and not a specific topic name
  - Use regexp to specify your regular expressions.
  - See the [confluent_kafka_python `subscribe()`](https://docs.confluent.io/current/clients/confluent-kafka-python/index.html?highlight=serializer#confluent_kafka.Consumer.subscribe) documentation for more information

#### Deserializers
- Remember to deserialize the data you are receiving from Kafka in an appropriate format
  - If the producer used JSON, you will need to deserialize the data using a JSON library
  - If the producer used bytes or string data, you may not have to do anything
- Consumer groups increase fault tolerance and resiliency by automatically redistributing partition assignments if one or more members of the consumer group fail.

#### Retrieving Data From Kafka
The consumer poll loop fetches data from Kafka
- Most Kafka Consumers will have a “poll” loop which loops infinitely and ingests data from Kafka
- Here is a sample poll loop:
```python
while True:
  message = consumer.poll(timeout=1.0)
  # messages = consumer.consume(5, timeout=1.0) # 5 messages at a time returns batch of messages
  if message is None:
    print("no message received by consumer")
  elif message.error() is not None:
    print(f"error from consumer {message.error()}")
    # Log error
    continue
  else:
    print(f"consumed message {message.key()}: {message.value()}")
```
- It is possible to use either poll or consume, but poll is slightly more feature rich
- Make sure to call close() on your consumer before exiting and to consume any remaining messages
- Failure to call close means the Kafka Broker has to recognize that the consumer has left the consumer group, which takes time and failed messages. Try to avoid this if you can. This will cause a rebalance

#### Optional Further Research
- [Consumer Configuration Options](https://kafka.apache.org/documentation/#consumerconfigs)
- `confluent_kafka_python` [Options](https://docs.confluent.io/current/clients/confluent-kafka-python/index.html?highlight=serializer#consumer)
- `librdkafka` [consumer options shared with `confluent_kafka_python`](https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md)

## Performance

### Metrics for consumer performance

#### Consumer
- **Consumer lag** measures how far behind consumer is: `Lag = Latest Topic Offset - Consumer Topic Offset`
  - Validate that the lag does not grow over time, consumer cant keep up
  - Will need aditional consumer processes
- Messages per second indicates throughput
- Kafka Java Metrics Explorer provides real-time metrics

#### Producer
- Measure latency to understand performance: `latency = time broker received - time produced`
  - Must be constant
  - Must be small
- High latency may indicate that your `acks` setting is too high and that too many `ISR` nodes must confirm message before returning
- High latency may indicate too many replicas
- **Producer response rate** tracks overall delivery rate (Messages delivered over time). Measure this number using producer delivery callbacks

#### Broker
- Track disc usage, high disk usage cause outages. It stores lots of data.
  - May cause data loss and high downtimes if not enough space
- Network usage may slow consume/produce
  - Avoid always network saturation
- Elections frequency. Should be infrequent
  - When Leadership elections occurs, it stops all consumers and producers. It is very disruptive
  - Frequent elections indicates broker instability (Cluster issues)

#### Summary
Monitoring Kafka Consumers, Producers, and Brokers for performance is an important part of using Kafka. There are many metrics by which to measure your Kafka cluster. Focus on these key metrics to get started:

- Consumer Lag: The difference between the latest offset in the topic and the most recently committed consumer offset
- Producer Response Rate: The rate at which the broker is responding to the producer indicating message status
- Producer Request Latency: The length of time a producer has to wait for a response from the broker after sending a message
- Broker Disk Space
- Broker Elections

### Further Research
- [DataDog blog post on monitoring Kafka](https://www.datadoghq.com/blog/monitoring-kafka-performance-metrics)
- [Confluent article on monitoring Kafka](https://docs.confluent.io/current/kafka/monitoring.html)
- [New Relic article on monitoring Kafka](https://blog.newrelic.com/engineering/new-relic-kafkapocalypse/)

## Data Privacy and Removing Records
Removing data from Kafka requires special planning and consideration, since it utilizes an append-only log. In this section you will learn about strategies and privacy regulations related to removing Kafka records.

- Message expiration, wait data after X time, or amount of data.
- Log compaction. Null messages in a compacted topic delete the data for that key.
  - Changing the value of a compacted topic into `null` wil cause all messages with that key to be dropped
  - Log compaction timing setting to be aware of
  - It may take to long for the data to be compacted and deleted
- User data may be spread through many topics and not always key on user_id

### Encrypted User Keys
- User data is encrypted with a special key per user
- The key is used to decrypt and access the data
- [Daniel Lebrero invented this way](https://danlebrero.com/2018/04/11/kafka-gdpr-event-sourcing/)
- Create a topic with an encryption key for every user, encrypt all other topic data for the user with that key
  
### Summary
- Privacy regulations like GDPR and CCPA are increasingly common and require applications to give users the right to be forgotten
- You can accomplish this with message expiration on topics that is of shorter duration than your requirement
- You may also use log compaction with null messages to delete data
- The best approach is to use [Daniel Lebrero’s Encrypted User Keys strategy](https://danlebrero.com/2018/04/11/kafka-gdpr-event-sourcing/)

### Further reading
- [Confluent blog post on GDPR and the right to be forgotten](https://www.confluent.io/blog/handling-gdpr-log-forget/)
- [Daniel Lebrero’s Encrypted User Keys strategy](https://danlebrero.com/2018/04/11/kafka-gdpr-event-sourcing/)


# Data Schemas
This section introduces the concept of data schemas and why they are a critical part of real world stream processing applications.

## What are Data Schemas
- Data schemas help us define:
  - The shape of the data
  - The names of fields
  - The expected types of values
  - Whether certain data fields are optional or required.
- Data schemas provide expectations for applications so that they can properly ingest or produce data that match that specification
- Data schemas are used for communication between software
- Data schemas can help us create more efficient representations with compression
- Data schemas help systems develop independently of each other
- Data schemas are critical in data systems and applications today
  - gRPC in Kubernetes
    - Protocol buffer schema languaga
  - Apache Avro in the Hadoop Ecosystem

## Glossary
- Data Schema - Define the shape of a particular kind of data. Specifically, data schemas define the expected fields, their names, and value types for those fields. Data schemas may also indicate whether fields are required or optional.
- Apache Avro - A data serialization framework which includes facilities for defining and communicating data schemas. Avro is widely used in the Kafka ecosystem and data engineering generally.
- Record (Avro) - A single encoded record in the defined Avro format
- Primitive Type (Avro) - In Avro, a primitive type is a type which requires no additional specification - null, boolean, int, long, float, double, bytes, string.
- Complex Type (Avro) - In Avro, a complex type models data structures which may involve nesting or other advanced functionality: records, enums, maps, arrays, unions, fixed.
- Schema Evolution - The process of modifying an existing schema with new, deleted, or modified fields.
- Schema Compatibility - Determines whether or not two given versions of a schema are usable by a given client
- Backward Compatibility - means that consumer code developed against the most recent version of an Avro Schema can use data using the prior version of a schema without modification.
- Forward Compatibility - means that consumer code developed against the previous version of an Avro Schema can consume data using the newest version of a schema without modification.
- Full Compatibility - means that consumers developed against the latest schema can consume data using the previous schema, and that consumers developed against the previous schema can consume data from the latest schema as well. In other words, full compatibility means that a schema change is both forward and backward compatible.
- None Compatibility - disables compatibility checking by Schema Registry.

## Data Streaming with Schemas
- Why they matter?
  - Data streams are constantly evolving
  - No schema = broken consumer on every data change
  - Schemas allow consumers to function without updates
  - Schemas provides independe and scalanbility
- Summary:
  - Data schemas help systems evolve independently from each other. This is beneficial at an application and an organizational level within our companies.
  - Data schemas describe the expected keys, value types, and whether certain keys are optional or required.
  - Data schemas can be used to create more efficient representations of our data models

## Apache Avro
Apache Avro is a widely used data schema system in the data engineering space, and especially in the Apache Kafka ecosystem. In this section, we’ll review key concepts as they relate to Avro and Stream Processing.

- Why not json?
  - Malformed is easily
  - Doesn't validate the type of fields
  - Is not binary (Latency and overhead added)

- Avro
  - Is a data serialization that uses binary compression
  - Can not be malformed
  - validate field types
  - Has lower latency and overhead
  - Avro is used widely in data engineering and the Kafka ecosystem
  - They get also the Avro instructions on how deserealize differentiate with gRPC and ProtocolBuffers

### Avro Schema key points
- Apache Avro records are defined in JSON.
- Avro records include a required name, such as "user"
- Avro records must include a type defined as record
- Avro records may optionally include a namespace, such as "com.udacity"
- Avro records are required to include an array of fields that define the names of the expected fields and their associated type. Such as "fields": [{"name": "age", "type": "int"}]
- Avro can support optional fields by specifying the field type as either null or some other type. Such as "fields": [{"name": "age", "type": [“null”, "int"]}]
- Avro records are made up of complex and primitive types
- Complex types are other records, arrays, maps, and others
- Please reference the[ Avro documentation](https://avro.apache.org/docs/1.8.2/spec.html#schemas) for full documentation and additional examples
- Here is what a stock ticker price change schema might look like: 
```json
{
  "type": "record",
  "name": "stock.price_change",
  "namespace": "com.udacity",
  "fields": [
      {"name": "ticker", "type": "string"},
      {"name": "prev_price", "type": "int"},
      {"name": "price", "type": "int"},
      {"name": "cause", "type": ["null", "string"]}
  ]
}
```

### Avro Data Types
- Full documentation is available on the [Avro website](https://avro.apache.org/docs/1.8.2/spec.html#schema_primitive)
- [Primitive Types](https://avro.apache.org/docs/1.8.2/spec.html#schema_primitive) should be familiar, as they closely mirror the built-in types for many programming languages.
  - null
  - boolean
  - int
  - long
  - float
  - double
  - bytes
  - string
- [Complex Types](https://avro.apache.org/docs/1.8.2/spec.html#schema_complex) allow nesting and advanced functionality.
  - records
  - enums
  - maps
  - arrays
  - unions
  - fixed

### Optional Further Research into Apache Avro
- [Python fastavro Library](https://fastavro.readthedocs.io/en/latest/index.html)
- [Apache Avro Specification](https://avro.apache.org/docs/1.8.2/spec.html#Maps)

## Apache Avro and Kafka
The Apache Kafka development community decided early on to incorporate [support for Avro into Kafka and Kafka ecosystem tools](https://www.confluent.io/blog/avro-kafka-data/). In this section, you will learn how to use Avro with Kafka.

**Apache Avro and Kafka - Helpful Documentation**
- `confluent_kafka_python` [Avro Producer](https://docs.confluent.io/current/clients/confluent-kafka-python/index.html?highlight=partition#confluent_kafka.avro.AvroProducer)
- `confluent_kafka_python` [Avro Consumer](https://docs.confluent.io/current/clients/confluent-kafka-python/index.html?highlight=partition#confluent_kafka.avro.AvroConsumer)

## Schema Registry
[Confluent Schema Registry](https://docs.confluent.io/current/schema-registry/index.html) is an open-source tool that provides centralized Avro Schema storage. In this section, you’ll learn how Schema Registry can improve your Kafka Stream Processing applications.

- Sending the schema on the run for each message will increase latency, size of files and networking overhead
- Schema Registry stores state in Kafka itself
- Schemas only need to be sent to Schema Registry once
- Clients fetch schemas as needed from the registry
- Does not support deletes
- Has an HHTP REST Interface
- May use with any application, not just Kafka

**Schema Registry Architecture**
- Built in Scala and Java, runs on the JVM
- high Portable, runs on every OS
- Stores all of its state in Kafka topics, not a database
- Exposes and HTTP web-server with a REST APU
- Can run standalone or clustered many nodes
- Uses Zookeeper to choose leader in cluster mode
![schemaRegistry]

### Schema Registry - Summary
- Provides an HTTP REST API for managing Avro schemas
- Many Kafka clients natively support Schema Registry interactions for you
- Reduces network overhead, allowing producers and consumers to register schemas one time
- Simplifies using Avro, reducing the barrier to entry for developers
- Uses a Kafka topic to store state
- Deployed as one or more web servers, with one leader
- Uses ZooKeeper to manage elections

### Schema Registry - Optional Further Research
- `confluent_kafka_python` [Avro and Schema Registry support](https://docs.confluent.io/current/clients/confluent-kafka-python/index.html?highlight=partition#module-confluent_kafka.avro)
- [Schema Registry Overview](https://docs.confluent.io/current/schema-registry/index.html)
- [Schema Registry HTTP API Documentation](https://docs.confluent.io/current/schema-registry/develop/api.html)

## Schema Evolution and Compatibility
Schemas change over time with new requirements. This process of schema change is known as Schema Evolution.
In this section, you will see how Avro and Schema Registry can aid in the process of Schema Evolution.
We’ll also discuss in this series of concepts how evolving schemas can be forward or backward compatible with previous versions.

**Schema Evolution**
The process of changing the schema of a given dataset is referred to as schema evolution. Modifying, adding or removing a field are all forms of a schema evolution


### Schema Compatibility
Schema registry tracks compatibility between schema versions
- If the schema is compatible, the consumer continues consumption
- If the schema is incompatible, the consumer will cease consumption
- Prevents miss process data and validation
- Schema Compatibility


- The process of schema change is known as Schema Evolution
- Schema Evolution is caused by a modification to an existing data schema
  - Adding or removing a field
  - Making a field optional
  - Changing a field type
- Schema Registry can track schema compatibility between schemas
  - Compatibility is used to determine whether or not a particular schema version is usable by a data consumer
  - Consumers may opt to use this compatibility information to preemptively refuse to process data that is incompatible with its current configuration
  - Schema Registry supports four categories of compatibility
  - Backward / Backward Transitive
  - Forward / Forward Transitive
  - Full / Full Transitive
  - None
- Managing compatibility requires both producer and consumer code to determine the compatibility of schema changes and send those updates to Schema Registry

#### Backward compatibility
- [Backward compatibility](https://docs.confluent.io/current/schema-registry/avro.html#backward-compatibility) means that consumer code developed against the most recent version of an Avro Schema can use data using the prior version of a schema without modification.
  - The deletion of a field or the addition of a new optional field is backward compatible changes.
  - Update consumers before updating producers to ensure that consumers can handle the new data type
- The `BACKWARD` compatibility type indicates compatibility with the current version (`N`) and the immediately prior version (`N-1`)
  - Unless you specify otherwise, Schema Registry always assumes that changes are BACKWARD compatible
- The `BACKWARD_TRANSITIVE` compatibility type indicates compatibility with all **prior versions** (`1 → N`)
- **If Producer making backward compatible, need consumers to update to the lastest version of the schema before we realease the new schema**

#### Forward compatibility
- [Forward compatibility](https://docs.confluent.io/current/schema-registry/avro.html#forward-compatibility) means that consumer code developed against the previous version of an Avro Schema can consume data using the newest version of a schema without modification
  - The deletion of an optional field or the addition of a new field is forward compatible changes
  - Producers need to be updated before consumers
- The `FORWARD` compatibility type indicates that data produced with the latest schema (`N`) is usable by consumers using the previous schema version (`N-1`)
- The `BACKWARD_TRANSITIVE` compatibility type indicates that data produced with the latest schema (N) is usable by all consumers using any previous schema version (`1 → N-1`)
-----------------------------------------------------------------------------------------
# Kinesis
AWS Streaming. Based on **shards**.
Has producer and consumers.
A shard is the throughput unit, a single shard can handle 1Mb/sec or 1000 requests per second.

## Recommendations:
- Shard can be dynamically. You can add more sahrds easily, but you cannot reduce them easily.
- Uses partition keys (Always have more partition keys than shards) to send the data.
- Sends data accordning to the partition key.
- Make sure it is evenly distributed, will help.

## Best Practices
- Aggregate records
- Compress the data
- Keys should be perfectly balanced (Randomized, like an ID or somethign similar)
- Method to split and merge shards
- Max acceptable latency [AWS Best practices talk](https://www.youtube.com/watch?v=jKPlGznbfZ0)
- [Kinesis Shard Calculator](https://comcastsamples.github.io/KinesisShardCalculator/)

### Producers
You can produce with the aws API with put_records or put_record.

### Consumers
Kinesis library
Event based using Lambda, may be useful to process it and sent it to another service with lambda.

## Appendix

### Messages compression types table
| Algorithm | Pros                                     | Cons                                                   |
| --------- | ---------------------------------------- | ------------------------------------------------------ |
| lz4       | fast compression and decompression       | not a high compression ratio                           |
| snappy    | fast compression and decompression       | not a high compression ratio                           |
| zstd      | high compression ratio                   | not as fast as lz4 or snappy                           |
| gzip      | widely-supported, high compression ratio | cpu-intensive, significantly slower than lz4 or snappy |


## Additional Resources Kinesis
- [Reading Data from Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/building-consumers.html)
- [Best practices for consuming Amazon Kinesis Data Streams using AWS Lambda](https://aws.amazon.com/blogs/big-data/best-practices-for-consuming-amazon-kinesis-data-streams-using-aws-lambda/)
- [AWS Streaming Data Solution for Amazon Kinesis](https://aws.amazon.com/solutions/implementations/aws-streaming-data-solution-for-amazon-kinesis/?did=sl_card&trk=sl_card)
- [How to replay in a stream data pushed to S3 from AWS Firehose?](https://stackoverflow.com/questions/53745384/how-to-replay-in-a-stream-data-pushed-to-s3-from-aws-firehose)



  
[//]: <> (Links and some external resources.)
[Quora]: https://www.quora.com/What-is-the-difference-between-the-ETL-and-ELT
[kafka-partitions]: ./Images/Kafka_partitions.png "airflow-diagram"
[topic_ordering]: ./Images/topic_ordering.png "how-airflow-works"
[time_value_data]: ./Images/DataLoseValue.png "Data time value"
[diagram_compression]: ./Images/CompressionDiagram.png "Compression"
[schemaRegistry]: ./Images/SchemaRegistry.png "Schema Registry"
