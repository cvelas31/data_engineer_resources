"""
SELECT 
date_trunc('week', "ts") AS "week",
start_reserved_location_id,
SUM(CASE WHEN "status"='AVAILABLE' THEN "time_fraction" ELSE 0 END) AS "time_available",
SUM(CASE WHEN ("status"='COMPLETED' AND "type"='TIPO_2') THEN "time_fraction" ELSE 0 END) AS "time_used"
FROM "example-ts"."ts_example" 
WHERE "date">'2021-03-04' AND "service_id"=1
GROUP BY date_trunc('week', "ts"), start_reserved_location_id
ORDER BY "week";
"""

"""
CREATE EXTERNAL TABLE ts_example (
  `id` int,
  `ts` timestamp,
  `user_id` int,
  `status` string,
  `type` string,
  `service_id` int,
  `duration_h` double,
  `time_fraction` double
) PARTITIONED BY (
  `date` string
)
STORED AS parquet
LOCATION 's3://bucket/prefix/'
TBLPROPERTIES (
  'has_encrypted_data'='false',
  "projection.enabled" = "true",
  "projection.date.type" = "date",
  "projection.date.range" = "NOW-6MONTHS,NOW",
  "projection.date.format" = "yyyy-MM-dd",
  "projection.date.interval" = "1",
  "projection.date.interval.unit" = "DAYS",
  "storage.location.template" = "s3://bucket/prefix/date=${date}",
  "parquet.compression"="GZIP"
);
"""