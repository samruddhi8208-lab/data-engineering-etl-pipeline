# data-engineering-etl-pipeline
ETL and Data Processing Pipeline using Python, SQL, Pandas and PySpark
# Data Engineering ETL & Data Processing Pipeline

## 📌 Project Overview

This project demonstrates an end-to-end ETL and data processing pipeline using Python, Pandas, SQL, and PySpark.

The pipeline processes employee and order data, performs data cleaning and transformation, applies SQL-based analysis, and generates structured summary outputs.

## 🎯 Objectives

* Build a practical ETL pipeline
* Process structured CSV data
* Clean and transform datasets
* Perform SQL-based analysis
* Use PySpark for data processing
* Generate department-level summaries
* Store processed data in structured formats

## 🛠️ Technologies

* Python
* Pandas
* SQL
* SQLite
* PySpark
* CSV
* Parquet
* GitHub

## 🔄 ETL Architecture

```text
             Raw CSV Data
                  |
                  v
              Extract
                  |
                  v
          Data Cleaning
                  |
                  v
           Transformation
                  |
                  v
            SQL Analysis
                  |
                  v
         PySpark Processing
                  |
                  v
             Aggregation
                  |
                  v
         Processed Outputs
            /           \
           v             v
         CSV          Parquet
```

## 📂 Project Structure

```text
data-engineering-etl-pipeline/
│
├── data/
│   ├── raw/
│   │   ├── employees.csv
│   │   └── orders.csv
│   │
│   └── processed/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── sql/
│   ├── queries.sql
│   └── analysis.sql
│
├── screenshots/
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## 📊 Dataset

### Employees

The employee dataset contains:

* Employee ID
* Name
* Department
* City
* Salary

### Orders

The order dataset contains:

* Order ID
* Employee ID
* Product
* Quantity
* Price

## 🔹 ETL Process

### 1. Extract

Data is extracted from CSV files using Python and Pandas.

### 2. Transform

The transformation stage includes:

* Duplicate removal
* Missing-value handling
* Data type conversion
* Total order amount calculation
* Employee and order dataset joining

The order amount is calculated using:

```text
total_amount = quantity × price
```

### 3. SQL Processing

SQL is used for:

* Filtering employees by salary
* Department-wise salary analysis
* Employee-order JOIN
* Department-wise order aggregation
* Identifying top employees based on order value

### 4. PySpark Processing

PySpark is used for scalable data processing.

The pipeline can perform:

* CSV data reading
* Data transformation
* Dataset JOIN
* Grouping
* Aggregation

### 5. Load

Processed data can be stored in:

* CSV
* Parquet

## 📈 Key Operations

* ETL pipeline development
* Data cleaning
* Data transformation
* SQL JOIN
* SQL aggregation
* PySpark processing
* Department-wise analysis
* Structured data storage

## ▶️ How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python src/pipeline.py
```

## 📁 Output

The pipeline generates processed summary data for further analysis.

Typical output includes:

* Department-wise total order amount
* Employee-level order summary
* Processed CSV data
* Parquet data

## 📚 Learning Outcomes

This project provided practical experience with:

* ETL workflow design
* Python data processing
* Pandas
* SQL
* PySpark
* Data cleaning
* Data transformation
* JOIN operations
* Aggregation
* CSV and Parquet data processing
* GitHub project documentation

## 🚀 Future Improvements

* Add Apache Airflow for workflow orchestration
* Add AWS S3 as cloud storage
* Add AWS Glue for managed ETL
* Add automated testing
* Add GitHub Actions for CI/CD
* Add Power BI dashboard for visualization

## 👩‍💻 Author

**Samruddhi More**

B.Tech – Electronics Engineering (VLSI Design & Technology)
