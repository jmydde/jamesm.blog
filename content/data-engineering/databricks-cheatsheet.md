---
title: "Databricks CheatSheet"
date: 2026-04-04T20:44:25+01:00
draft: false
tags: ['databricks', 'cheatsheet', 'pyspark', 'sql', 'delta-lake']
description: "Quick reference guide for Databricks notebooks, SQL DDL/DML, PySpark API, and production patterns"
cover:
  image: images/data.jpg
  alt: Databricks CheatSheet
---

## Quick Start

This cheatsheet covers essential Databricks notebook commands, SQL operations, PySpark transformations, and optimization techniques for the lakehouse platform.

## Databricks Notebook Commands

Magic commands provide shortcuts for common operations in Databricks notebooks:

| Command     | Purpose                                      | Use Case |
|-------------|----------------------------------------------|---------| 
| %python     | Executes python code (default language)      | PySpark transformations, data processing |
| %sql        | Executes SQL queries                         | Querying tables and views |
| %scala      | Executes scala code                          | Spark API operations, JVM access |
| %r          | Execute R code                               | Statistical analysis and visualization |
| %sh         | Shell commands on cluster nodes              | Git operations, system utilities |
| %fs         | Databricks file system operations            | File management, DBFS interactions |
| %md         | Markdown text formatting                     | Documentation and cell titles |
| %pip        | Install Python packages                      | Adding Python dependencies |
| %env        | Set environment variables                    | Configuration and secrets |
| %config     | Notebook configuration options               | Display settings, execution parameters |
| %jobs       | Lists all running jobs                       | Job monitoring |
| %load       | Load external file contents                  | Include external code |
| %reload     | Reload Python modules                        | Refresh imports |
| %run        | Execute another notebook                     | Code reuse and modularization |
| %lsmagic    | List all available magic commands            | Discovery |
| %who        | List variables in current scope              | Debugging and variable inspection |
| %matplotlib | Configure matplotlib backend                 | Visualization setup |

### Notebook Widgets
```
# Create widgets
dbutils.widgets.text("param_name", "default_value", "label")
dbutils.widgets.dropdown("param_name", "default", ["option1", "option2"])
dbutils.widgets.multiselect("param_name", "default", ["option1", "option2"])
dbutils.widgets.combobox("param_name", "default", ["option1", "option2"])

# Get widget values
param_value = dbutils.widgets.get("param_name")

# Remove widget
dbutils.widgets.remove("param_name")
dbutils.widgets.removeAll()
```

### Secrets Management
```
# Create secret scope
dbutils.secrets.createScope("scope_name")

# Store secret
dbutils.secrets.put("scope_name", "secret_key", "secret_value")

# Retrieve secret
secret_value = dbutils.secrets.get("scope_name", "secret_key")

# List secrets
dbutils.secrets.list("scope_name")

# Delete secret
dbutils.secrets.delete("scope_name", "secret_key")
```

### Accessing Files
- /path/to/file (local)
- dbfs:/path/to/file (DBFS)
- file:/path/to/file (driver filesystem)
- s3://path/to/file (S3)
- /Volumes/catalog/schema/volume/path (Unity Catalog Volumes)

### Copying Files
```
%fs cp file:/<path> /Volumes/<catalog>/<schema>/<volume>/<path>

%python dbutils.fs.cp("file:/<path>", "/Volumes/<catalog>/<schema>/<volume>/<path>")
%python dbutils.fs.cp("file:/databricks/driver/test", "dbfs:/repo", True)

%sh cp /<path> /Volumes/<catalog>/<schema>/<volume>/<path>
```

## SQL Statements

### DDL - Data Definition Language (Schema & Table Operations)

#### Create & Use Schema
```
CREATE SCHEMA test;
CREATE SCHEMA custom LOCATION 'dbfs:/custom';

USE SCHEMA test;
```

### Unity Catalog (UC)
```
-- Create catalog
CREATE CATALOG my_catalog COMMENT "Production catalog";

-- Create schema in UC
CREATE SCHEMA my_catalog.my_schema;
USE CATALOG my_catalog;
USE SCHEMA my_schema;

-- Create volume (for files)
CREATE VOLUME my_catalog.my_schema.my_volume;
ALTER VOLUME my_catalog.my_schema.my_volume OWNER TO `team@company.com`;

-- List catalogs, schemas, volumes
SHOW CATALOGS;
SHOW SCHEMAS IN my_catalog;
SHOW VOLUMES IN my_catalog.my_schema;

-- Grant permissions
GRANT USAGE ON CATALOG my_catalog TO `user@company.com`;
GRANT READ_VOLUME ON VOLUME my_catalog.my_schema.my_volume TO `user@company.com`;
```

#### Create Table
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

#### Create View
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

#### Drop & Describe
```
DROP TABLE test;

SHOW TABLES;
DESCRIBE EXTENDED test;
```

### DML - Data Manipulation Language (Data Operations)

#### Select
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

#### Insert
```
INSERT OVERWRITE test SELECT * FROM read_files('/repo/data/test.csv');

INSERT INTO test(col1, col2) VALUES ('value1', 'value2');
```

#### Merge Into
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

#### Copy Into
```
COPY INTO test
FROM '/repo/data'
FILEFORMAT = CSV
FILES = ('test.csv')
FORMAT_OPTIONS('header' = 'true', 'inferSchema' = 'true');
```

## Spark DataFrame API

PySpark is the Python API for Apache Spark, enabling distributed data processing on the Databricks platform.

### Read Data
```python
# Read CSV
df = spark.read.format("csv").option("header", "true").load("/path/to/file.csv")
df = spark.read.csv("/path/to/file.csv", header=True)

# Read Parquet
df = spark.read.parquet("/path/to/file.parquet")

# Read JSON
df = spark.read.json("/path/to/file.json")

# Read Delta table
df = spark.read.table("my_table")
df = spark.read.format("delta").load("/path/to/delta/table")

# Read from Volumes
df = spark.read.csv("/Volumes/catalog/schema/volume/file.csv", header=True)
```

### Write Data
```python
# Write modes: overwrite, append, ignore, error
df.write.mode("overwrite").format("parquet").save("/path/to/output")
df.write.mode("overwrite").option("mergeSchema", "true").format("delta").save("/path/to/delta")

# Write to table
df.write.mode("overwrite").saveAsTable("my_table")
df.write.mode("overwrite").option("path", "/path").saveAsTable("my_table")

# Write to Volume
df.write.mode("overwrite").parquet("/Volumes/catalog/schema/volume/output")
```

### Common Transformations
```python
# Select columns
df.select("col1", "col2")
df.select(df.col1, df.col2)

# Filter/Where
df.filter(df.col1 > 10)
df.where("col1 > 10")

# GroupBy and aggregations
df.groupBy("col1").agg({"col2": "sum", "col3": "count"})
from pyspark.sql.functions import sum, count, avg
df.groupBy("col1").agg(sum("col2"), count("col3"))

# Joins
df1.join(df2, on="col1", how="inner")
df1.join(df2, (df1.col1 == df2.col1) & (df1.col2 == df2.col2), how="left")

# Distinct/Dedup
df.distinct()
df.dropDuplicates(["col1", "col2"])

# Sort
df.sort("col1", ascending=False)
df.orderBy(df.col1.desc())
```


## Performance Optimization

### Delta Lake Optimization
```sql
-- Optimize table (compacts small files)
OPTIMIZE my_table;
OPTIMIZE my_table ZORDER BY col1, col2;

-- Check table stats
ANALYZE TABLE my_table COMPUTE STATISTICS;
ANALYZE TABLE my_table COMPUTE STATISTICS FOR COLUMNS col1, col2;

-- View statistics
DESCRIBE EXTENDED my_table;
```

### Partitioning Strategy
```python
# Write with partitioning
df.write \
  .mode("overwrite") \
  .partitionBy("date", "region") \
  .format("delta") \
  .save("/path/to/table")

# Partition pruning (applied automatically)
# SELECT * FROM table WHERE date = '2024-01-01' AND region = 'US'
```

### Query Performance
```python
# Enable adaptive query execution
spark.conf.set("spark.sql.adaptive.enabled", "true")

# Enable vectorized execution
spark.conf.set("spark.sql.execution.arrow.enabled", "true")

# Set shuffle partitions
spark.conf.set("spark.sql.shuffle.partitions", "200")

# Monitor query plans
df.explain(mode="extended")
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

## Lakeflow Declarative Pipelines (formerly Delta Live Tables)

In 2026, Databricks rebranded Delta Live Tables to [Lakeflow Declarative Pipelines](https://docs.databricks.com/gcp/en/ldp/concepts). The syntax below still works, but prefer `STREAMING TABLE` and `MATERIALIZED VIEW` over the older `LIVE TABLE` framing for new pipelines.

```
CREATE OR REFRESH STREAMING TABLE test_raw
AS SELECT * FROM cloud_files('/repo/data/', 'json');

CREATE OR REFRESH STREAMING TABLE test
AS SELECT * FROM STREAM read_files('/repo/data/test*.json');

CREATE OR REFRESH MATERIALIZED VIEW test_cleaned
AS SELECT col1, col2, col3, col4 FROM test_raw;

CREATE OR REFRESH MATERIALIZED VIEW recent_test
AS SELECT col1, col2 FROM test2 ORDER BY creation_time DESC LIMIT 10;

-- Legacy syntax (still supported)
CREATE OR REFRESH LIVE TABLE test_raw
AS SELECT * FROM json.`/repo/data/test.json`;
```

## Functions
```
CREATE OR REPLACE FUNCTION test_function(temp DOUBLE)
RETURNS DOUBLE
RETURN (col1 - 10);

CREATE OR REPLACE FUNCTION add_numbers(a INT, b INT)
RETURNS INT
RETURN a + b;
```

## Useful dbutils Functions

### File System Operations
```python
# List files
dbutils.fs.ls("dbfs:/path")
dbutils.fs.ls("/Volumes/catalog/schema/volume")

# Get file info
dbutils.fs.getStatus("dbfs:/path/file.txt")

# Move/Rename
dbutils.fs.mv("dbfs:/old/path", "dbfs:/new/path")

# Remove files
dbutils.fs.rm("dbfs:/path", recurse=True)

# Create directory
dbutils.fs.mkdirs("dbfs:/new/directory")

# Copy files
dbutils.fs.cp("dbfs:/source", "dbfs:/dest", recurse=True)

# Head (preview file)
dbutils.fs.head("dbfs:/path/file.txt", 1000)
```

### Notebook Context
```python
# Get notebook path
dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

# Get current user
dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()

# Exit notebook
dbutils.notebook.exit("Exit message")

# Run another notebook
dbutils.notebook.run("./other_notebook", timeout_seconds=3600, arguments={"param1": "value1"})
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

In 2026, prefer [`AUTO CDC`](https://docs.databricks.com/gcp/en/ldp/cdc) over the older `APPLY CHANGES INTO` for new pipelines.

```
-- 2026 recommended syntax
CREATE OR REFRESH STREAMING TABLE target;

CREATE FLOW target_cdc AS
AUTO CDC INTO target
FROM stream(cdc_source)
KEYS (col1)
APPLY AS DELETE WHEN col2 = "DELETE"
SEQUENCE BY col3
COLUMNS * EXCEPT (col)
STORED AS SCD TYPE 2;

-- Legacy syntax (still supported)
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

REVOKE <privilege> ON <object_type> <object_name> FROM `test@gmail.com`;

-- UC Specific
GRANT USAGE ON CATALOG my_catalog TO `user@company.com`;
GRANT CREATE ON SCHEMA my_catalog.my_schema TO `team@company.com`;
GRANT READ_VOLUME ON VOLUME my_catalog.my_schema.my_volume TO `user@company.com`;
GRANT WRITE_VOLUME ON VOLUME my_catalog.my_schema.my_volume TO `user@company.com`;
```

## Jobs and Workflows
```python
# List running jobs
%jobs

# Submit job via API
from databricks.sdk import WorkspaceClient
w = WorkspaceClient()
job = w.jobs.create(
    name="my_job",
    tasks=[{
        "task_key": "task1",
        "notebook_task": {"notebook_path": "/Users/me/notebook"},
        "new_cluster": {"spark_version": "14.3.x-scala2.12", "num_workers": 2, "node_type_id": "i3.xlarge"}
    }]
)
```

## Links
- **Official Databricks Documentation**
  - [Databricks Docs Home](https://docs.databricks.com/)
  - [SQL Language Reference](https://docs.databricks.com/en/sql/language-manual/index.html)
  - [Python API Reference (PySpark)](https://docs.databricks.com/en/dev-tools/python-sql-connector.html)
  
- **Core Features**
  - [Delta Lake Documentation](https://docs.databricks.com/en/delta/index.html)
  - [Unity Catalog Guide](https://docs.databricks.com/en/data-governance/unity-catalog/index.html)
  - [Databricks SQL Endpoints](https://docs.databricks.com/en/sql/admin/sql-endpoints.html)
  - [Serverless SQL](https://docs.databricks.com/en/sql/admin/serverless.html)

- **Cheat Sheets**
  - [Compute Creation](https://docs.databricks.com/en/cheat-sheet/compute.html)
  - [Platform Administration](https://docs.databricks.com/en/cheat-sheet/administration.html)
  - [Production Job Scheduling](https://docs.databricks.com/en/cheat-sheet/jobs.html)

- **Best Practices**
  - [Delta Lake Best Practices](https://docs.databricks.com/en/delta/best-practices.html)
  - [Unity Catalog Best Practices](https://docs.databricks.com/en/data-governance/unity-catalog/best-practices.html)
  - [Cluster Configuration Best Practices](https://docs.databricks.com/en/compute/cluster-config-best-practices.html)
  - [MLOps Workflow](https://docs.databricks.com/en/machine-learning/mlops/mlops-workflow.html)

- **Tools & APIs**
  - [Databricks Python SDK](https://databricks-py.readthedocs.io/)
  - [Databricks CLI](https://docs.databricks.com/en/dev-tools/cli/index.html)
  - [Terraform Provider](https://registry.terraform.io/providers/databricks/databricks/latest/docs)

- **Community Resources**
  - [Databricks Cheat Sheet - Medium](https://mayur-saparia7.medium.com/databricks-cheat-sheet-1-a0d3e0f70065)
  - [Notebook Markdown Cheat Sheet](https://grabngoinfo.com/databricks-notebook-markdown-cheat-sheet/)
