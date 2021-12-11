# author    Bhavyai Gupta
# purpose   exports the results of SQL command to CSV

import sqlite3
from sqlite3 import Error
import pandas as pd

# set the input db file
db_filename = "database/data.db"

# set the input SQL command to run
sql_text = """
            SELECT t1.file_id, t1.section_id, t1.url, t1.heading_text, t2.content_text_w_o_tags,
            t1.abstracted_heading_text || ' ' || t2.content_text_w_o_tags AS abstracted_heading_plus_content,
            t1.section_code
            FROM section_overview_75pct t1
            JOIN section_content_75pct t2 ON t1.file_id=t2.file_id AND t1.section_id=t2.section_id
            """

# set the output CSV file
csv_filename = "sqlite_dump.csv"


# make the sqlite connection to the db file
conn = sqlite3.connect(db_filename)


# read the SQL query results in the dataframe
df = pd.read_sql_query(con=conn, sql=sql_text)


# export the dataframe into CSV
df.to_csv(path_or_buf=csv_filename, header=True, index=False, encoding='utf-8')
