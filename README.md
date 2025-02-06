# ***digital audio store Data warehouse***

this project was made based on the chinook-database, and it's about a digital store that sells music online
it has customers,employees, and tracks to sell

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
