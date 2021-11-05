# Run TPC-DS with Spark

This project is highly derived from the following projects.

* [databricks/spark-sql-perf](https://github.com/databricks/spark-sql-perf)
* [brownsys/tpcds](https://github.com/brownsys/tpcds)

## Highlights

- Support TPC-DS v2.3.0
- Tool for the input data
- Tool for executing queries, which are included in src/main/resources/queries

## Libraries included

- Spark 2.1.0
- Scala 2.11.8
- ScalaTest 2.2.4
- ScalaCheck 1.12.2

## How to prepare data for the benchmark

First, you should compile and package applications.

```
$ ./activator clean assembly
```

Then, you can see target/scala-2.11/spark-tpcds-assembly-0.1.0-SNAPSHOT.jar.

**Important**

This application uses "dsdgen" tool of official data generator of TPC-DS,
so that you should download sources of tools from 
[Official TPC Donwload site](http://www.tpc.org/tpc_documents_current_versions/current_specifications.asp)
and compile them to create executable binaries.

In this document, we assume that "dsdgen" tool is located in /usr/local/tpc-ds/default/tools directory.
You can execute the application with the following command.

```
$ spark-submit --class net.dobachi.tpcds.gendata.GenerateTpcdsData target/scala-2.11/spark-tpcds-assembly-0.1.0-SNAPSHOT.jar /tmp/tpcds --databaseName tpcds --partitionNum 1 --enableOverwrite --writeAsTable
```

If your dsdgen tool is located in other places, you can use "--toolDir" option
to specify the location of the tool directory.

e.g.

```
--toolDir /usr/local/tpc-ds/default/tools
```

As a result of the above command,
several tables exists in your Hive databases.
This is because, "--writeAsTable" option is used.

If you want to create raw Parquet files instead of Hive tables,
please run the application without --writeAsTable option.
In this case, data is generated into the output directory which you specified
as an command-line argument.

## Execute queries

After preparing data, you can execute TPC-DS queries by the following command.

```
$ spark-submit --class net.dobachi.tpcds.execute.ExecuteQueries target/scala-2.11/spark-tpcds-assembly-0.1.0-SNAPSHOT.jar spark 
```

This project holds multiple types of queries in src/main/resources/queries directory
and you can specify queries to be executed by the command line argument.
In the above case, we use queries in "src/main/resources/queries/spark",
which are a little different version of TPC-DS official queries for netezza dialect.

This application holds the execution time of each query,
and display them after executing all queries.

e.g.

```
17/02/26 17:07:51 INFO execute.ExecuteQueries$: /queries/spark/query01.sql: 2388 msec
17/02/26 17:07:51 INFO execute.ExecuteQueries$: /queries/spark/query02.sql: 791 msec
17/02/26 17:07:51 INFO execute.ExecuteQueries$: /queries/spark/query03.sql: 460 msec
17/02/26 17:07:51 INFO execute.ExecuteQueries$: /queries/spark/query04.sql: 708 msec
17/02/26 17:07:51 INFO execute.ExecuteQueries$: /queries/spark/query05.sql: 1145 msec
(snip)
```

## Difference from original queries of TPC-DS

Queries in this projects for Spark is modified version of TPC-DS queries for netezza dialect.
The main modifications are

* Use concat instead of ||
* Remove spaces from "as" expressions
* Add "()" to the back and forth of "union all"

## ToDo

- Add other kinds of benchmarks

## Author
- dobachi (dobachi1983oss@gmail.com)
