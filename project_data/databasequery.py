import sqlite3

import pandas

db_filename = "../database/data.db"
conn = sqlite3.connect(db_filename)

sql_text = """
                SELECT t1.file_id, t1.section_id, t1.url, t1.heading_text, t2.content_text_w_o_tags, 
                t1.abstracted_heading_text || ' ' || t2.content_text_w_o_tags AS abstracted_heading_plus_content, 
                t1.section_code
                FROM section_overview_75pct t1 
                JOIN section_content_75pct t2 ON t1.file_id=t2.file_id AND t1.section_id=t2.section_id
                """

sql_text = """
        SELECT t1.file_id, t1.section_id, t1.url, t1.local_readme_file, t1.heading_markdown, t1.abstracted_heading_markdown,
        t1.heading_text, t1.abstracted_heading_text, t1.heading_level, t2.content_text_w_o_tags, 
        t1.abstracted_heading_text || ' ' || t2.content_text_w_o_tags AS abstracted_heading_plus_content
        FROM target_section_overview t1 
        JOIN target_section_content t2 
        ON t1.file_id=t2.file_id AND t1.section_id=t2.section_id
        ORDER BY t1.file_id, t1.section_id
        """

sql_text = """
        SELECT *
        FROM target_section_overview t1 
        
        """

df_target_section_overview = pandas.read_sql_query(con=conn, sql=sql_text)
sql_text = """
        SELECT *
        FROM target_section_content t2 

        """

df_target_section_content = pandas.read_sql_query(con=conn, sql=sql_text)
print("Target Section Overview Table:")
print(df_target_section_overview.head())

print("Target Section Content Table:")
print(df_target_section_content.head())