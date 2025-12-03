---
title: "Databricks CheatSheet"
date: 2024-02-25T21:00:25+01:00
draft: false
tags: ['databricks', 'cheatsheets']
---

## Databricks Notebook Commands

| Command     | Purpose                                      | Example |
|-------------|----------------------------------------------|---------|
| %config     | Set configuration options for the notebook   | |
| %env        | Set environment variables                    | |
| %fs         | Interact with the Databricks file system     | %fs ls dbfs:/repo |
| %load       | Loads the contents of a file into a cell     | |
| %lsmagic    | List all magic commands                      | |
| %jobs       | Lists all running jobs                       | |
| %matplotlib | sets up the matplotlib backend               | |
| %md         | Write Markdown text                          | |
| %pip        | Install Python packages                      | |
| %python     | Executes python code                         | %python dbutils.fs.rm("/user/hive/warehouse/test/", True) |
| %r          | Execute R code                               | |
| %reload     | reloads module contents                      | |
| %run        | Executes a Python file or a notebook         | |
| %scala      | Executes scala code                          | |
| %sh         | Executes shell commands on the cluster nodes | %sh git clone https://github.com/repo/test |
| %sql        | Executes SQL queries                         | |
| %who        | Lists all the variables in the current scope | |

### Accessing Files
- /path/to/file
- dbfs:/path/to/file
- file:/path/to/file
- s3://path/to/file

### Copying Files
```
%fs cp file:/<path> /Volumes/<catalog>/<schema>/<volume>/<path>

%python dbutils.fs.cp("file:/<path>", "/Volumes/<catalog>/<schema>/<volume>/<path>")
%python dbutils.fs.cp("file:/databricks/driver/test", "dbfs:/repo", True)

%sh cp /<path> /Volumes/<catalog>/<schema>/<volume>/<path>
```

## SQL Statements (DDL)

### Create & Use Schema
```
CREATE SCHEMA test;
CREATE SCHEMA custom LOCATION 'dbfs:/custom';

USE SCHEMA test;
```

### Create Table
```
CREATE TABLE test(col1 INT, col2 STRING, col3 STRING, col4 BIGINT, col5 INT, col6 FLOAT);
CREATE TABLE test AS SELECT * EXCEPT (_rescued_data) FROM read_files('/repo/data/test.csv');
CREATE TABLE test USING CSV LOCATION '/repo/data/test.csv';
CREATE TABLE test USING CSV OPTIONS (header="true") LOCATION '/repo/data/test.csv';
CREATE TABLE test AS SELECT * EXCEPT (_rescued_data) FROM read_files('/repo/data/test.csv');
CREATE TABLE test AS ...
CREATE TABLE test USING ...

CREATE TABLE test(id INT, title STRING, col1 STRING, publish_time BIGINT, pages INT, price FLOAT)
COMMENT 'This is comment for the table itself';

CREATE TABLE test AS
SELECT * EXCEPT (_rescued_data)
FROM read_files('/repo/data/test.json', format => 'json');

CREATE TABLE test_raw AS
SELECT * EXCEPT (_rescued_data)
FROM read_files('/repo/data/test.csv', sep => ';');

CREATE TABLE custom_table_test LOCATION 'dbfs:/custom-table'
AS SELECT * EXCEPT (_rescued_data) FROM read_files('/repo/data/test.csv');

CREATE TABLE test PARTITIONED BY (col1)
AS SELECT * EXCEPT (_rescued_data) FROM read_files('/repo/data/test.csv')

CREATE TABLE users(
firstname STRING,
lastname STRING,
full_name STRING GENERATED ALWAYS AS (concat(firstname, ' ', lastname))
);

CREATE OR REPLACE TABLE test AS SELECT * EXCEPT (_rescued_data) FROM read_files('/repo/data/test.csv');
CREATE OR REPLACE TABLE test AS SELECT * FROM json.`/repo/data/test.json`;
CREATE OR REPLACE TABLE test AS SELECT * FROM read_files('/repo/data/test.csv');
```

### Create View
```
CREATE VIEW view_test
AS SELECT * FROM test WHERE col1 = 'test';

CREATE VIEW view_test
AS SELECT col1, col1
FROM test
JOIN test2 ON test.col2 == test2.col2;

CREATE TEMP VIEW temp_test
AS SELECT * FROM test WHERE col1 = 'test';

CREATE TEMP VIEW temp_test
AS SELECT * FROM read_files('/repo/data/test.csv');

CREATE GLOBAL TEMP VIEW view_test
AS SELECT * FROM test WHERE col1 = 'test';
SELECT * FROM global_temp.view_test;

CREATE TEMP VIEW jdbc_example USING JDBC
OPTIONS (
url "<jdbc-url>",
dbtable "<table-name>",
user '<username>',
password '<password>');

CREATE OR REPLACE TEMP VIEW test AS SELECT * FROM delta.`<logpath>`;

CREATE VIEW event_log_raw AS SELECT * FROM event_log("<pipeline-id>");

CREATE OR REPLACE TEMP VIEW test_view
AS SELECT test.col1 AS col1 FROM test_table
WHERE col1 = 'value1' ORDER BY timestamp DESC LIMIT 1;
```

### Drop
```
DROP TABLE test;
```

### Describe
```
SHOW TABLES;

DESCRIBE EXTENDED test;
```

## SQL Statements (DML)

### Select
```
SELECT * FROM csv.`/repo/data/test.csv`;
SELECT * FROM read_files('/repo/data/test.csv');
SELECT * FROM read_files('/repo/data/test.csv', format => 'csv', header => 'true', sep => ',')
SELECT * FROM json.`/repo/data/test.json`;
SELECT * FROM json.`/repo/data/*.json`;
SELECT * FROM test WHERE year(from_unixtime(test_time)) > 1900;
SELECT * FROM test WHERE title LIKE '%a%'
SELECT * FROM test WHERE title LIKE 'a%'
SELECT * FROM test WHERE title LIKE '%a'
SELECT * FROM test TIMESTAMP AS OF '2024-01-01T00:00:00.000Z';
SELECT * FROM test VERSION AS OF 2;
SELECT * FROM test@v2;
SELECT * FROM event_log("<pipeline-id>");

SELECT count(*) FROM VALUES (NULL), (10), (10) AS example(col);
SELECT count(col) FROM VALUES (NULL), (10), (10) AS example(col);
SELECT count_if(col1 = 'test') FROM test;
SELECT from_unixtime(test_time) FROM test;
SELECT cast(test_time / 1 AS timestamp) FROM test;
SELECT cast(cast(test_time AS BIGINT) AS timestamp) FROM test;
SELECT element.sub_element FROM test;
SELECT flatten(array(array(1, 2), array(3, 4)));

SELECT * FROM (
  SELECT col1, col2 FROM test
) 
PIVOT (
  sum(col1) for col2 in ('item1','item2')
);

SELECT *, CASE
WHEN col1 > 10 THEN 'value1'
ELSE 'value2'
END
FROM test;

SELECT * FROM test ORDER BY (CASE
WHEN col1 > 10 THEN col2
ELSE col3
END);

WITH t(col1, col2) AS (SELECT 1, 2)
SELECT * FROM t WHERE col1 = 1;

SELECT details:flow_definition.output_dataset as output_dataset,
       details:flow_definition.input_datasets as input_dataset
FROM   event_log_raw, latest_update
WHERE  event_type = 'flow_definition' AND origin.update_id = latest_update.id;
```

### Insert
```
INSERT OVERWRITE test SELECT * FROM read_files('/repo/data/test.csv');

INSERT INTO test(col1, col2) VALUES ('value1', 'value2');
```

### Merge Into
```
MERGE INTO test USING test_to_delete
ON test.col1 = test_to_delete.col1
WHEN MATCHED THEN DELETE;

MERGE INTO test USING test_to_update
ON test.col1 = test_to_update.col1
WHEN MATCHED THEN UPDATE SET *;

MERGE INTO test USING test_to_insert
ON test.col1 = test_to_insert.col1
WHEN NOT MATCHED THEN INSERT *;
```

### Copy Into
```
COPY INTO test
FROM '/repo/data'
FILEFORMAT = CSV
FILES = ('test.csv')
FORMAT_OPTIONS('header' = 'true', 'inferSchema' = 'true');
```


## Delta Lake Statements
```
DESCRIBE HISTORY test;
DESCRIBE HISTORY test LIMIT 1;

INSERT INTO test SELECT * FROM test@v2 WHERE id = 3;

OPTIMIZE test;
OPTIMIZE test ZORDER BY col1;

RESTORE TABLE test TO VERSION AS OF 0;

SELECT * FROM test TIMESTAMP AS OF '2024-01-01T00:00:00.000Z';
SELECT * FROM test VERSION AS OF 2;
SELECT * FROM test@v2;

VACUUM test;
VACUUM test RETAIN 240 HOURS;

%fs ls dbfs:/user/hive/warehouse/test/_delta_log
%python spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", "false")
```

## Delta Live Table Statements
```
CREATE OR REFRESH LIVE TABLE test_raw
AS SELECT * FROM json.`/repo/data/test.json`;

CREATE OR REFRESH STREAMING TABLE test
AS SELECT * FROM STREAM read_files('/repo/data/test*.json');

CREATE OR REFRESH LIVE TABLE test_cleaned
AS SELECT col1, col2, col3, col4 FROM live.test_raw;

CREATE OR REFRESH LIVE TABLE recent_test
AS SELECT col1, col2 FROM live.test2 ORDER BY creation_time DESC LIMIT 10;
```

## Fuctions
```
CREATE OR REPLACE FUNCTION test_function(temp DOUBLE)
RETURNS DOUBLE
RETURN (col1 - 10);
```

## Auto Loader
```
%python

spark.readStream.format("cloudFiles")\
  .option("cloudFiles.format", "json")\
  .option("cloudFiles.schemaLocation", "/autoloader-schema")\
  .option("pathGlobFilter", "test*.json")\
  .load("/repo/data")\
  .writeStream\
  .option("mergeSchema", "true")\
  .option("checkpointLocation", "/autoloader-checkpoint")\
  .start("demo")

%fs head /autoloader-schema/_schemas/0

CREATE OR REFRESH STREAMING TABLE test
AS SELECT * FROM
cloud_files(
'/repo/data',
'json',
map("cloudFiles.inferColumnTypes", "true", "pathGlobFilter", "test*.json")
);

CONSTRAINT positive_timestamp EXPECT (creation_time > 0)
CONSTRAINT positive_timestamp EXPECT (creation_time > 0) ON VIOLATION DROP ROW
CONSTRAINT positive_timestamp EXPECT (creation_time > 0) ON VIOLATION FAIL UPDATE
```

## CDC Statements
```
APPLY CHANGES INTO live.target
  FROM stream(live.cdc_source)
  KEYS (col1)
  APPLY AS DELETE WHEN col2 = "DELETE"
  SEQUENCE BY col3
  COLUMNS * EXCEPT (col);
```

## Security Statements
```
GRANT <privilege> ON <object_type> <object_name> TO <user_or_group>;
GRANT SELECT ON TABLE test TO `databricks@degols.net`;

REVOKE <privilege> ON <object_type> <object_name> FROM `test@gmail.com';
```

## Links
- [Databricks](https://docs.databricks.com/en/index.html)
  - [SQL Language Reference](https://docs.databricks.com/en/sql/language-manual/index.html)
  - [Cheat Sheets](https://docs.databricks.com/en/getting-started/best-practices.html)
    - [Compute creation cheat sheet](https://docs.databricks.com/en/cheat-sheet/compute.html)
    - [Platform administration cheat sheet](https://docs.databricks.com/en/cheat-sheet/administration.html)
    - [Production job scheduling cheat sheet](https://docs.databricks.com/en/cheat-sheet/jobs.html)
  - [Best Practices](https://docs.databricks.com/en/getting-started/best-practices.html)
    - [Delta Lake best practices](https://docs.databricks.com/en/delta/best-practices.html)
    - [Hyperparameter tuning with Hyperopt](https://docs.databricks.com/en/machine-learning/automl-hyperparam-tuning/hyperopt-best-practices.html)
    - [Deep learning in Databricks](https://docs.databricks.com/en/machine-learning/train-model/dl-best-practices.html)
    - [Recommendations for MLOps](https://docs.databricks.com/en/machine-learning/mlops/mlops-workflow.html)
    - [Unity Catalog best practices](https://docs.databricks.com/en/data-governance/unity-catalog/best-practices.html)
    - [Cluster configuration best practices](https://docs.databricks.com/en/compute/cluster-config-best-practices.html)
    - [Instance pool configuration best practices](https://docs.databricks.com/en/compute/pool-best-practices.html)
- Other
  - [Databricks Cheat Sheet 1](https://mayur-saparia7.medium.com/databricks-cheat-sheet-1-a0d3e0f70065)
  - [Databricks Notebook Markdown Cheat Sheet](https://grabngoinfo.com/databricks-notebook-markdown-cheat-sheet/)
