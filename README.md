# ***digital audio store Data warehouse***

this project was made based on the chinook-database, and it's about a digital store that sells music online
it has customers,employees, and tracks to sell

<p align="center">
  <img src="https://github.com/user-attachments/assets/e5f9961a-2bba-4851-a53a-e68f07be9e99" alt="Sublime's custom image"/>
</p>


## about the data

[Data Link on GitHub](https://github.com/lerocha/chinook-database)

the original data ERD:
![The Data ERD](https://github.com/user-attachments/assets/97cfcdb2-00da-4fa0-a6ec-358bb13b17f0)
the data warehouse
![Data Warehouse snowflake schema](https://github.com/user-attachments/assets/762307a3-4ef8-447d-bb81-e8df669686ab)

### tables

there is 11 tables that has many features as the following:

- **album**         ➡ has the album details
- **artist**        ➡ artist details
- **customer**      ➡ the customer details
- **employee**      ➡ the employees details
- **genre**         ➡ genre id and name
- **invoice**       ➡ has the invoice details
- **invoice_line**  ➡ each track that was billed in the invoice
- **media_type**    ➡ media type id, the type name
- **playlist**      ➡ the play lists details
- **playlist_track**➡ playlist id and all of the tracks ids in it
- **track**         ➡ track details

## Project structure

```plaintext
data-warehousing-project/
├── README.md              # Project overview and setup instructions
├── .gitignore             # Ignored files and directories
├── requirements.txt       # Python dependencies for the project
├── data/                  # Raw and processed data
│   ├── raw/               # Downloaded or ingested raw data files
│   └── processed/         # Cleaned and transformed data files
├── scripts/               # Python scripts for ETL and modeling
│   ├── ingestion.py       # Script for data ingestion
│   ├── modeling.py        # Script for DW schema creation
│   └── stats.py           # Script to generate stats and insights
├── sql/                   # SQL scripts for schema creation and queries
│   ├── dw_schema.sql      # SQL for data warehouse schema
│   └── queries.sql        # Example queries for stats
├── notebooks/             # Optional Jupyter notebooks for exploration
│   └── exploration.ipynb  # Data exploration notebook
└── reports/               # Generated reports and analysis
    └── stats_report.md    # Summary of findings and insights
```

## Use Cases:
This project aims to provide a central data source that improves performance by:
- Tracking sales and time trends.
- Evaluating employee performance and identifying appropriate promotions.
- Analyzing customer behavior.
- Managing artist and album data.
- Improving operational process.
- Predicting future trends based on historical sales data.

## Query example:  
Evaluating sales performance by calculating total revenue per genre.

**Without DWH:**
```sql
SELECT g.name, SUM(il.quantity * il.unit_price) AS TotalSales
FROM public.invoice_line il
JOIN public.track t ON il.track_id = t.track_id
JOIN public.genre g ON t.genre_id = g.genre_id
JOIN public.invoice i ON il.invoice_id = i.invoice_id
GROUP BY g.name
ORDER BY TotalSales DESC;
```
- **Arithmetic operations:** performs a multiplication operation for each row (quantity * unit_price).
- **JOINs count:** 3 JOINs
- **Query performance:** lower performance due to reduced speed and increased complexity
- **Scalability:** struggles with large datasets.

**With DWH:**
```sql
SELECT t.genre_name, SUM(id.total) AS TotalSales
FROM dw_schema.invoice_details id
JOIN dw_schema.track t ON id.track_id = t.track_id
GROUP BY t.genre_name
ORDER BY TotalSales DESC;
```
- **Arithmetic operations:** uses pre-aggregated value (total).
- **JOINs count:** 1 JOIN
- **Query performance:** higher performance due to greater speed and reduced complexity
- **Scalability:** efficiently handles large-scale data.

## Executing steps:
1. Install all requirements:
    - Code editor (e.g. Visual Studio Code)
    - Libraries in requirements.py file
    - Database management system (e.g. PostgreSQL)
    - A tool to implement sql queries (e.g. pgAdmin)
2. Check for database configuration in files:  
   ingestion.py, modeling.py and stats.py.
3. Run scripts:  
python python ingestion.py &#8594; python modeling.py &#8594; python stats.py  
When running these scripts, it will:  
    - Clean row data.
    - Connect to the PostgreSQL server.
    - Create a new database named digital_store_DWH (if it doesn't already exist).
    - Create a new schema named public and populate it with data.
    - Create a new schema named dw_schema and populate it with data.
4. Run exploration.ipynb file to see project insights.
