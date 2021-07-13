# Execution
- Start Zookeper:
  - `zookeeper-server-start /etc/kafka/zookeeper.properties`
  - Other terminal: `kafka-server-start /etc/kafka/server.properties`
- Connector Validation:
  - Connector can only have strings
  - `curl localhost:8083/connectors`
  - Connect to postgres: `psql postgres://cta_admin:chicago@localhost:5432/cta`
  - [Topic from connect](https://docs.confluent.io/platform/current/connect/references/restapi.html#topics)
- Topic validation
  - `kafka-topics --list --zookeeper localhost:2181`
- Delete topics
  - `kafka-topics --delete --topic "topic_name" --zookeeper localhost:2181`
- Consume topic
  - `kafka-console-consumer --topic "topic_name" --bootstrap-server PLAINTEXT://localhost:9092 --from-beginning`
  - `kafka-avro-console-consumer --topic "topic_name" --bootstrap-server PLAINTEXT://localhost:9092 --from-beginning`

`spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0,org.apache.kafka:kafka-clients:2.3.0 solution_ingest_kafka_data.py`


`spark.sparkContext.setLogLevel("WARN")`