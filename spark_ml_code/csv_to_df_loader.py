import spark

def read_CSV_to_DF(filepath):
  """
  Reads a csv file into a spark dataframe
  """
  df = (spark.read
        .option("multiline", "true")
        .option("quote", '"')
        .option("header", "true")
        .option("escape", "\\")
        .option("escape", '"')
        .csv(filepath)
        )

  return df


# importing files from DBFS
df = read_CSV_to_DF('/FileStore/project/sqlite_dump.csv')

# cast the some column to int
df = df.withColumn("file_id", df["file_id"].cast("int"))
df = df.withColumn("section_id", df["section_id"].cast("int"))
