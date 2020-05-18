# Data Lake with Spark

## Why learn spark?
Spark is currently one of the most popular tools for big data analytics. You might have heard of other tools such as Hadoop. Hadoop is a slightly older technology although still in use by some companies. Spark is generally faster than Hadoop, which is why Spark has become more popular over the last few years.

There are many other big data tools and systems, each with its own use case. For example, there are database system like Apache Cassandra and SQL query engines like Presto. But Spark is still one of the most popular tools for analyzing large data sets.

Here is an outline of the topics we are covering in this lesson:
- What is big data?
- Review of the hardware behind big data
- Introduction to distributed systems
- Brief history of Spark and big data
- Common Spark use cases
- Other technologies in the big data ecosystem

### What is Big Data?
Instead of using a single machine is better to use multiple machines. Capabilities of modern software.
Numbers everyone should know

In the next few videos, you'll learn about four key hardware components. Understanding these components helps determine whether you are working on a "big data" problem or if it's easier to analyze the data locally on your own computer.

#### CPU (Central Processing Unit)
The CPU is the "brain" of the computer. Every process on your computer is eventually handled by your CPU. This includes calculations and also instructions for the other components of the compute.

The CPU is the brains of a computer. The CPU has a few different functions including directing other components of a computer as well as running mathematical calculations. The CPU can also store small amounts of data inside itself in what are called registers. These registers hold data that the CPU is working with at the moment.

For example, say you write a program that reads in a 40 MB data file and then analyzes the file. When you execute the code, the instructions are loaded into the CPU. The CPU then instructs the computer to take the 40 MB from disk and store the data in memory (RAM). If you want to sum a column of data, then the CPU will essentially take two numbers at a time and sum them together. The accumulation of the sum needs to be stored somewhere while the CPU grabs the next number.

This cumulative sum will be stored in a register. The registers make computations more efficient: the registers avoid having to send data unnecessarily back and forth between memory (RAM) and the CPU.

#### Memory (RAM)
When your program runs, data gets temporarily stored in memory before getting sent to the CPU. Memory is ephemeral storage - when your computer shuts down, the data in the memory is lost.

Beyond the fact that memory is expensive and ephemeral, we'll learn that for most use cases in the industry, memory and CPU aren't the bottleneck. Instead the storage and network, which you'll learn about in the next videos, slow down many tasks you'll work on in the industry.

#### Storage (SSD or Magnetic Disk)
Storage is used for keeping data over long periods of time. When a program runs, the CPU will direct the memory to temporarily load data from long-term storage.

#### Network (LAN or the Internet)
Network is the gateway for anything that you need that isn't stored on your computer. The network could connect to other computers in the same room (a Local Area Network) or to a computer on the other side of the world, connected over the internet.

Transfering data across computers is not fast, shuffling the data is the most expensive thing to do in Spark, minimizing this is the best for time speed

#### Other Numbers to Know?
You may have noticed a few other numbers involving the L1 and L2 Cache, mutex locking, and branch mispredicts. While these concepts are important for a detailed understanding of what's going on inside your computer, you don't need to worry about them for this course. If you're curious to learn more, check out [Peter Norvig's original blog post] from a few years ago, and an [interactive version] for today's current hardware.
![alt text][numberstoknow]

### Key Ratios
- CPU: 200x faster than memory
- Memory: 15x faster than SSD
- SSD: 20x faster than network
- Network: The slowest

### Pandas with "Big data"
If a dataset is larger than the size of your RAM, you might still be able to analyze the data on a single computer. By default, the Python pandas library will read in an entire dataset from disk into memory. If the dataset is larger than your computer's memory, the program won't work.

However, the Python pandas library can read in a file in smaller chunks. Thus, if you were going to calculate summary statistics about the dataset such as a sum or count, you could read in a part of the dataset at a time and accumulate the sum or count.

[Here] is an example of how this works.

### The Hadoop Ecosystem
#### Hadoop Vocabulary
Here is a list of some terms associated with Hadoop. You'll learn more about these terms and how they relate to Spark in the rest of the lesson.
- **Hadoop** - an ecosystem of tools for big data storage and data analysis. Hadoop is an older system than Spark but is still used by many companies. The major difference between Spark and Hadoop is how they use memory. Hadoop writes intermediate results to disk whereas Spark tries to keep data in memory whenever possible. This makes Spark faster for many use cases.
- **Hadoop MapReduce** - a system for processing and analyzing large data sets in parallel.
- **Hadoop YARN** - a resource manager that schedules jobs across a cluster. The manager keeps track of what computer resources are available and then assigns those resources to specific tasks.
- **Hadoop Distributed File System (HDFS)** - a big data storage system that splits data into chunks and stores the chunks across a cluster of computers.

As Hadoop matured, other tools were developed to make Hadoop easier to work with. These tools included:

- **Apache Pig** - a SQL-like language that runs on top of Hadoop MapReduce
- **Apache Hive** - another SQL-like interface that runs on top of Hadoop MapReduce
Oftentimes when someone is talking about Hadoop in general terms, they are actually talking about Hadoop MapReduce. However, Hadoop is more than just MapReduce. In the next part of the lesson, you'll learn more about how MapReduce works.

#### How is Spark related to Hadoop?
Spark, which is the main focus of this course, is another big data framework. Spark contains libraries for data analysis, machine learning, graph analysis, and streaming live data. Spark is generally faster than Hadoop. This is because Hadoop writes intermediate results to disk whereas Spark tries to keep intermediate results in memory whenever possible.

The Hadoop ecosystem includes a distributed file storage system called HDFS (Hadoop Distributed File System). Spark, on the other hand, does not include a file storage system. You can use Spark on top of HDFS but you do not have to. Spark can read in data from other sources as well such as Amazon S3.

#### Streaming Data
Data streaming is a specialized topic in big data. The use case is when you want to store and analyze data in real-time such as Facebook posts or Twitter tweets.

Spark has a streaming library called Spark Streaming although it is not as popular and fast as some other streaming libraries. Other popular streaming libraries include **Storm** and **Flink**. Streaming won't be covered in this course, but you can follow these links to learn more about these technologies.

## SPARK
### Spark Use Cases and Resources
Here are a few resources about different Spark use cases:
- Data Analytics (Spark SQL)
- Machine Learning (Spark Mllib)
- Streaming (Spark Streaming)
- Graph Analytics (Spark GraphX)

### You Don't Always Need Spark
Spark is meant for big data sets that cannot fit on one computer. But you don't need Spark if you are working on smaller data sets. In the cases of data sets that can fit on your local computer, there are many other options out there you can use to manipulate data such as:

- AWK - a command line tool for manipulating text files
- R - a programming language and software environment for statistical computing
- Python PyData Stack, which includes pandas, Matplotlib, NumPy, and scikit-learn among other libraries
Sometimes, you can still use pandas on a single, local machine even if your data set is only a little bit larger than memory. Pandas can read data in chunks. Depending on your use case, you can filter the data and write out the relevant parts to disk.

If the data is already stored in a relational database such as MySQL or Postgres, you can leverage SQL to extract, filter and aggregate the data. If you would like to leverage pandas and SQL simultaneously, you can use libraries such as SQLAlchemy, which provides an abstraction layer to manipulate SQL tables with generative Python expressions.

The most commonly used Python Machine Learning library is scikit-learn. It has a wide range of algorithms for classification, regression, and clustering, as well as utilities for preprocessing data, fine tuning model parameters and testing their results. However, if you want to use more complex algorithms - like deep learning - you'll need to look further. TensorFlow and PyTorch are currently popular packages.

### Spark's Limitations
Spark has some limitation.

Spark Streaming’s latency is at least 500 milliseconds since it operates on micro-batches of records, instead of processing one record at a time. Native streaming tools such as Storm, Apex, or Flink can push down this latency value and might be more suitable for low-latency applications. Flink and Apex can be used for batch computation as well, so if you're already using them for stream processing, there's no need to add Spark to your stack of technologies.

Another limitation of Spark is its selection of machine learning algorithms. Currently, Spark only supports algorithms that scale linearly with the input data size. In general, deep learning is not available either, though there are many projects integrate Spark with Tensorflow and other deep learning tools.

### Hadoop versus Spark
The Hadoop ecosystem is a slightly older technology than the Spark ecosystem. In general, Hadoop MapReduce is slower than Spark because Hadoop writes data out to disk during intermediate steps. However, many big companies, such as Facebook and LinkedIn, started using Big Data early and built their infrastructure around the Hadoop ecosystem.

While Spark is great for iterative algorithms, there is not much of a performance boost over Hadoop MapReduce when doing simple counting. Migrating legacy code to Spark, especially on hundreds of nodes that are already in production, might not be worth the cost for the small performance boost.

### Beyond Spark for Storing and Processing Big Data
Keep in mind that Spark is not a data storage system, and there are a number of tools besides Spark that can be used to process and analyze large datasets.

Sometimes it makes sense to use the power and simplicity of SQL on big data. For these cases, a new class of databases, know as NoSQL and NewSQL, have been developed.

For example, you might hear about newer database storage systems like HBase or Cassandra. There are also distributed SQL engines like Impala and Presto. Many of these technologies use query syntax that you are likely already familiar with based on your experiences with Python and SQL.

In the lessons ahead, you will learn about Spark specifically, but know that many of the skills you already have with SQL, Python, and soon enough, Spark, will also be useful if you end up needing to learn any of these additional Big Data tools.

## Data Wrangling with Spark

### Functional Programming
Perfect for distributed systems, spark uses it

### DAG (Directed Acyclical Graph)
Lazy evaluation and build the grpah of operations, kind of recipe.
Multi steps combo are called stages.

### Maps
Maps simply make a copy of the input data, and transform that copy according to some function

### Data Formats
CSV, JSON, HTML, XML
Difficulty dealing with HTML or XML is that elements cabn be nested, so while we process the files, we need to keep track of opening tags

### Distributed data stores
HDFS split files in 64Mb or 128Mb blocks across the cluster and replicates blocks across the cluster. Data Fault tolerant, and digesteble in chunks.

AWS S3 to store and retrieve

### Spark Session
First the spark context is necessary. Connects cluster with the application.
To create a spark context we need a saprk configuration. Its name and the masters IP Adress.

To spark sql, use SparkSession builder  
```python
from pyspark.swl import SparkSession

spark = SparkSession.builder.appName("Example").getOrCreate()

spark.sparkContext.getConf().getAll() # See all the parameters
```

### Functions
In the previous video, we've used a number of functions to manipulate our dataframe. Let's take a look at the different type of functions and their potential pitfalls.

### General functions
We have used the following general functions that are quite similar to methods of pandas dataframes:

- select(): returns a new DataFrame with the selected columns
- filter(): filters rows using the given condition
- where(): is just an alias for filter()
- groupBy(): groups the DataFrame using the specified columns, so we can run aggregation on them
- sort(): returns a new DataFrame sorted by the specified column(s). By default the second parameter 'ascending' is True.
- dropDuplicates(): returns a new DataFrame with unique rows based on all or just a subset of columns
- withColumn(): returns a new DataFrame by adding a column or replacing the existing column that has the same name. The first parameter is the name of the new column, the second is an expression of how to compute it.

### Aggregate functions
Spark SQL provides built-in methods for the most common aggregations such as count(), countDistinct(), avg(), max(), min(), etc. in the pyspark.sql.functions module. These methods are not the same as the built-in methods in the Python Standard Library, where we can find min() for example as well, hence you need to be careful not to use them interchangeably.

In many cases, there are multiple ways to express the same aggregations. For example, if we would like to compute one type of aggregate for one or more columns of the DataFrame we can just simply chain the aggregate method after a groupBy(). If we would like to use different functions on different columns, agg()comes in handy. For example agg({"salary": "avg", "age": "max"}) computes the average salary and maximum age.

### User defined functions (UDF)
In Spark SQL we can define our own functions with the udf method from the pyspark.sql.functions module. The default type of the returned variable for UDFs is string. If we would like to return an other type we need to explicitly do so by using the different types from the pyspark.sql.types module.

### Window functions
Window functions are a way of combining the values of ranges of rows in a DataFrame. When defining the window we can choose how to sort and group (with the partitionBy method) the rows and how wide of a window we'd like to use (described by rangeBetween or rowsBetween).

For further information see the Spark SQL, DataFrames and Datasets Guide and the Spark Python API Docs.

## Spark SQL
[Spark SQL built-in functions]
- Creating views to use same SQL queries.
- UDF needs to be registered, so it can look at it.

**INSIDE SPARK WHEN USING IMPERATIVE AND SQL IT USES A QUERY OPTIMIZER ON THE INSIDE**

## Debugging and optimization in Spark
Spark provides 3 methods to mamage clusters
- Standalone Mode
- MESOS: Sharing cluster across team
- YARN: Sharing cluster across team

## Using AWS with Spark
[Step by step]

# AWS CLI for EMR
LOOK  AT  THE COURSE. THIS PART WAS ADDED

**Why use AWS CLI?**
AWS CLI enables you to run commands that allow access to currently available AWS Services. We can also use AWS CLI to primarily create and check the status of our EMR instances. Mostly during your work, you would normally create clusters that are similar in sizes and functionalities, and it can get tedious when you use the AWS console to create a cluster. If you have a pre-generated script to generate EMR saved to your text editor, you can re-run as often as you’d like to generate new clusters. This way we can bypass setting security groups and roles through AWS console. You can embed all these features, including selecting number of cores, applications to install, and even custom script to execute at the time of cluster launch by using a pre-generated script.

**How to use AWS CLI?**
We’ll be using AWS CLI to create an EMR cluster.
Check to see if you have Python 3.6 or above
You can check the Python version using the command line: $ python --version
Install AWS CLI using pip install awscli.
Check if AWS CLI is installed correctly by typing aws into your terminal.
If you see the image below, you have installed AWS CLI correctly.

## EMR
- Create  SSH Key Pair on EC2 screen
- Go to EMR and Create cluster
- Use cluster launch mode (lont term cluster). (Step execution turn down the cluster once the spark job finishes)
- Select EMR-5.20.0, with Spark 2.4.0 YARN mode, Hadoop Ganglia and Zeppelin.
- Select instances (Most common m5) Fifth generation comes with SSD

### Deployed on a script
Logged into the Hadoop EMR, using ssh. (This may be done to the master node on the EC2 instance, with the Master public DNS on the summary of the cluster)
Using ssh and getting into the cluster.

Create the script (.py):
- Need to import all the things (pyspark or things like that)
- Create the session `spark = SparkSession.`
- The saprk context is not accessible as sc at the beggining it has to be run as `spark.sparkContext.`
- Explictly say to the spark session to stop `spark.stop()`

To submit your code you do:
- spark-submit
- to find it use the linux tool: which spark-submit and shows the path
- The you do: 
```bash
/usr/bin/spark-submit --master yarn {path-of-script}
```
- Recommended to write an output file to look at it.

### Storing and retrieving data on the cloud
#### S3 Buckets
With the convenient AWS UI, we can easily mistake AWS S3 (Simple Storage Service) equivalent as Dropbox or even Google Drive. This is not the case for S3. S3 stores an object, and when you identify an object, you need to specify a bucket, and key to identify the object. For example 
```
df = spark.read.load(“s3://my_bucket/path/to/file/file.csv”)
```
From this code, s3://my_bucket is the bucket, and path/to/file/file.csv is the key for the object. Thankfully, if we’re using spark, and all the objects underneath the bucket have the same schema, you can do something like below.
```
df = spark.read.load(“s3://my_bucket/”)
```
This will generate a dataframe of all the objects underneath the my_bucket with the same schema. Pretend some structure in s3 like below:
```
my_bucket
  |---test.csv
  path/to/
     |--test2.csv
     file/
       |--test3.csv
       |--file.csv
```
If all the csv files underneath my_bucket, which are test.csv, test2.csv, test3.csv, and file.csv have the same schema, the dataframe will be generated without error, but if there are conflicts in schema between files, then the dataframe will not be generated. As an engineer, you need to be careful on how you organize your data lake.

### Differences between HDFS and AWS S3
Since Spark does not have its own distributed storage system, it leverages using HDFS or AWS S3, or any other distributed storage. Primarily in this course, we will be using AWS S3, but let’s review the advantages of using HDFS over AWS S3.

Although it would make the most sense to use AWS S3 while using other AWS services, it’s important to note the differences between AWS S3 and HDFS.

AWS S3 is an object storage system that stores the data using key value pairs, namely bucket and key, and HDFS is an actual distributed file system which guarantees fault tolerance. HDFS achieves fault tolerance by having duplicate factors, which means it will duplicate the same files at 3 different nodes across the cluster by default (it can be configured to different numbers of duplication).

HDFS has usually been installed in on-premise systems, and traditionally have had engineers on-site to maintain and troubleshoot Hadoop Ecosystem, which cost more than having data on cloud. Due to the flexibility of location and reduced cost of maintenance, cloud solutions have been more popular. With extensive services you can use within AWS, S3 has been a more popular choice than HDFS.

Since AWS S3 is a binary object store, it can store all kinds of format, even images and videos. HDFS will strictly require a certain file format - the popular choices are avro and parquet, which have relatively high compression rate and which makes it useful to store large dataset.

#### Hadoop file system in EMR
- Create directory
`hdfs dfs -mkdir {path-directory}`
- Copy from local
hdfs dfs -copyFromLocal {file} {hdfs_directory}

## Debugging and optimization
Debugging in Spark is really hard!!!

### Data Errors
- Missing data and weird unicode chars
- Print is not recommended, it sends the statement to each node, so each node has a copy of the print statement. Isntead use accumulators

#### Accumulators
As the name hints, accumulators are variables that accumulate. Because Spark runs in distributed mode, the workers are running in parallel, but asynchronously. For example, worker 1 will not be able to know how far worker 2 and worker 3 are done with their tasks. With the same analogy, the variables that are local to workers are not going to be shared to another worker unless you accumulate them. Accumulators are used for mostly sum operations, like in Hadoop MapReduce, but you can implement it to do otherwise.

For additional deep-dive, here is the [Spark documentation on accumulators] if you want to learn more about these.

```python
incorrect_records = SparkContext.accumulator(0, 0)
incorrect_records.value # 0

def add_incorrect_record():
    global incorrect_records
    incorrect_records +=1

from pyspark.sql.functions import udf
correct_ts = udf(lambda x: 1 if x.isdigit() else add_incorrect_record())

ddf = df.where(df["corrupt"].isNull().withColumn("ts_digit", correct_ts(df.ts)))

# Needs to collect
```
Careful as they are not idempotent so can keep collecting

#### Spark Broadcast
Spark Broadcast variables are secured, read-only variables that get distributed and cached to worker nodes. This is helpful to Spark because when the driver sends packets of information to worker nodes, it sends the data and tasks attached together which could be a little heavier on the network side. Broadcast variables seek to reduce network overhead and to reduce communications. Spark Broadcast variables are used only with Spark Context.

```python
from pyspark import SparkContext

sc = SparkContext('local[*]', 'pyspark')

my_dict = {"item1": 1, "item2": 2, "item3": 3, "item4": 4} 
my_list = ["item1", "item2", "item3", "item4"]

my_dict_bc = sc.broadcast(my_dict)

def my_func(letter):
    return my_dict_bc.value[letter] 

my_list_rdd = sc.parallelize(my_list)

result = my_list_rdd.map(lambda x: my_func(x)).collect()

print(result)
```

### Spark Web UI
Is really good for diagnosis and monitoring the cluster
Provides:
- DAG, breaks in STages andd those Stages in Tasks.
    - Tasks are the steps that the individual worker nodes are assignedd
    - In each stage the worker noed divides up the input data and runs the task for that stage
- Cluster conifguration

The web UI only shows pages relatedd to current Spark jobs that are running

#### How to connect to Spark Web UI
- Port that uses Master noed to communicate with Slaves is 7077
- Jupyter port 8888
- Port 4040 shows active spark jobs.
- Web UI on port 8080, shows astatus of cluster andd recent jobs
- In local mode us e the docker host as the ip

- **Environment**
Different configuration parameters, version, name of application
- **Executors**
Gives information about executors, what resources, task ran succesfully
- **Storage**
Store cache rdds
- **Jobs**
As many actions regarding the code, an action can be take some records, saving, jobs are broken into stages, can be parallelized, then you can look the task, series of transformationrs ran in parallel
- **Stages**
Visualization of the DAG

Using log files is hard. they are splitted across different nodes

On executors  we will have std error and str out logs.
We can set log leverl erros, as logging. For ex:
`spark.sparkContext.setLogLevel("INFO") # "ERROR, etc`

Further Optional Study on Log Data
For further information please see the [Configuring Logging] section of the Spark documentation.

### Code Optimization
#### Dataset
**Introduction to Dataset**

In the real world, you’ll see a lot of cases where the data is skewed. Skewed data means due to non-optimal partitioning, the data is heavy on few partitions. This could be problematic. Imagine you’re processing this dataset, and the data is distributed through your cluster by partition. In this case, only a few partitions will continue to work, while the rest of the partitions do not work. If you were to run your cluster like this, you will get billed by the time of the data processing, which means you will get billed for the duration of the longest partitions working. This isn’t optimized, so we would like to re-distribute the data in a way so that all the partitions are working.
- Data Skew: Distribution of data is not uniform, a worker gets a lot of info when reducing. Pareto principle (80% of data comes from 20% of users). Knowing your data, change way of partition or get more partitions.

Let’s recap what we saw in the video
In order to look at the skewness of the data:

Check for MIN, MAX and data RANGES
Examine how the workers are working
Identify workers that are running longer and aim to optimize it.

#### Optimizing skewness
**Use Cases in Business Datasets**

Skewed datasets are common. In fact, you are bound to encounter skewed data on a regular basis. In the video above, the instructor describes a year-long worth of retail business’ data. As one might expect, retail business is likely to surge during Thanksgiving and Christmas, while the rest of the year would be pretty flat. Skewed data indicators: If we were to look at that data, partitioned by month, we would have a large volume during November and December. We would like to process this dataset through Spark using different partitions, if possible. What are some ways to solve skewness?
- Data preprocess
- Broadcast joins
- Salting

**So how do we solve skewed data problems?**
The goal is to change the partitioning columns to take out the data skewness (e.g., the year column is skewed).

1. Use Alternate Columns that are more normally distributed:
E.g., Instead of the year column, we can use Issue_Date column that isn’t skewed.

2. Make Composite Keys:
For e.g., you can make composite keys by combining two columns so that the new column can be used as a composite key. For e.g, combining the Issue_Date and State columns to make a new composite key titled Issue_Date + State. The new column will now include data from 2 columns, e.g., 2017-04-15-NY. This column can be used to partition the data, create more normally distributed datasets (e.g., distribution of parking violations on 2017-04-15 would now be more spread out across states, and this can now help address skewness in the data.

3. Partition by number of Spark workers:
Another easy way is using the Spark workers. If you know the number of your workers for Spark, then you can easily partition the data by the number of workers df.repartition(number_of_workers) to repartition your data evenly across your workers. For example, if you have 8 workers, then you should do df.repartition(8) before doing any operations.

[//]: <> (Links and some external resources.)
[Peter Norvig's original blog post]: http://norvig.com/21-days.html
[interactive version]: http://people.eecs.berkeley.edu/~rcs/research/interactive_latency.html
[Here]: http://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-chunking
[Spark SQL built-in functions]: https://spark.apache.org/docs/latest/api/sql/index.html
[Step by step]: http://insight-data-labs-sd.webflow.io/blog/spinning-up-an-apache-spark-cluster-step-by-step
[Spark documentation on accumulators]: https://spark.apache.org/docs/2.2.0/rdd-programming-guide.html#accumulators
[Configuring Logging]: https://spark.apache.org/docs/latest/configuration.html
[numberstoknow]: ./Images/numberstoknow.png "Numbers to Know"
