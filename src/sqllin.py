from sqllineage.runner import LineageRunner
import os

# Check in - 1
# Check in -2
# SQLLineage class
class sqllin:
    
    #Assign SQLLineage variables
    def __init__(self):
         self.sql        = "insert into db1.table11 select * from db2.table21 union select * from db2.table22;"

    # Get lineage summary
    def parse_input_sqlfile(self):
        # Run sqllineage parser
        result = LineageRunner(sql = self.sql,dialect="bigquery");
        
        # Print result
        print(result)

        # Draw the lineage as a graph
        result.draw()
        
class file_pre_processing:
    
    def __init__(self):
        self.input_path  = "/Users/ankit.gupta/venv/sqllin_ana/scripts" # Path of input sql files
        self.result_arry = []                                           # Store the parsed files as an array of tuples
        
    def process_input_sql_files(self):
        
        # Get all sql files in the input path
        sql_file_list = os.listdir(self.input_path)

        # for file in sql_file_list:
        #     with 


objRunner = sqllin()
objRunner.parse_input_sqlfile()

# FileName, SQLQuery, OperationType, SeqNo, SourceTable [Array], TargetTable

                                            # NULL, Tab1 --> L0
                                            # Tab1, Tab2 --> L0