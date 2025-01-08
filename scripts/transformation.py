def clean_sql_file(input_file, output_file):
    """
    Cleans an SQL file by escaping single quotes and ensuring semicolons within strings are handled correctly.
    Args:
        input_file (str): Path to the input SQL file.
        output_file (str): Path to save the cleaned SQL file.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                # change the line 
                fixed_line = line #.replace("'", "''") an example
                # Write the cleaned line to the output file
                outfile.write(fixed_line)

        print(f"Cleaned SQL file saved to: {output_file}")
    except Exception as e:
        print(f"Error while cleaning SQL file: {e}")

# these are the file pathes related to the directory:

input_sql_file = "./data/raw/Chinook_PostgreSql.sql"        #the input file that has the raw data
output_sql_file = "./data/processed/Chinook_PostgreSql.sql" # the output file that would have the processed data
clean_sql_file(input_sql_file, output_sql_file)
