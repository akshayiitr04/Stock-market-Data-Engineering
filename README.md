# 📈 End-to-End Stock Market Data Engineering Pipeline

## Overview

This project demonstrates a production-style Data Engineering pipeline that ingests stock market data, stores it in a cloud data lake, transforms it using dbt, orchestrates workflows with Apache Airflow, and loads analytics-ready data into Snowflake for business intelligence and reporting.

The goal is to simulate a real-world financial data platform used by investment firms, trading desks, and analytics teams.

---

## Business Problem

Financial data arrives continuously from multiple sources and must be processed efficiently before analysts can use it for reporting and decision-making.

This project solves the challenge by:

- Automating stock market data ingestion
- Building a scalable ELT pipeline
- Transforming raw market data into analytics-ready tables
- Creating a single source of truth in Snowflake
- Enabling downstream dashboarding and reporting

---

## Architecture

```text
Finnhub Stock API
    │
    ▼
 Kafka
    │
    ▼
Minio
    │
    ▼
Apache Airflow
    │
    ▼
Snowflake Raw Layer
    │
    ▼
dbt Transformations
    │
    ▼
Snowflake Analytics Layer
    │
    ▼
Power BI Dashboard
```
---

## Tech Stack

| Layer | Technology |
|---------|------------|
| Language | Python |
| Data Lake | Minio |
| Data Warehouse | Snowflake |
| Transformation | dbt |
| Orchestration | Apache Airflow |
| Visualization | Power BI |
| Containerization | Docker |
| Version Control | Git & GitHub |

---

## Data Pipeline Workflow

### Step 1: Data Extraction

- Fetch stock market data from APIs
- Collect historical and market-related information
- Validate incoming records

### Step 2: Data Lake Storage

- Store raw files in Minio Storage bucket
- Maintain immutable raw datasets
- Enable historical tracking

### Step 3: Workflow Orchestration

Apache Airflow DAGs automate:

- Data ingestion
- File movement
- Snowflake loading
- dbt execution
- Data quality checks

### Step 4: Data Warehousing

Data is loaded into Snowflake:

#### Raw Layer
Stores source data without modifications.

#### Staging Layer
Performs cleaning and standardization.

#### Analytics Layer
Business-ready tables optimized for reporting.

### Step 5: Transformation with dbt

dbt models perform:

- Data cleaning
- Type conversions
- Null handling
- Business logic implementation
- Fact and dimension table creation

---

## Repository Structure

```text
Stock-market-Data-Engineering/

├── airflow/
│   ├── dags/
│   └── plugins/
│
├── dbt/
│   ├── models/
│   ├── snapshots/
│   ├── seeds/
│   └── tests/
│
├── snowflake/
│   ├── sql/
│   └── scripts/
│
├── ingestion/
│   ├── api_extract.py
│   └── upload_to_minio.py
│
├── dashboards/
│   └── powerbi/
│
├── docker/
│
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## Key Features

✅ Automated Stock Data Ingestion

✅ Cloud Data Lake Architecture

✅ Airflow Workflow Orchestration

✅ Snowflake Data Warehousing

✅ dbt Data Transformations

✅ Data Quality Validation

✅ Analytics-Ready Data Models

✅ Business Intelligence Reporting

---

## Example Airflow DAG Flow

```text
Extract Stock Data
        ↓
Upload to minio
        ↓
Load into Snowflake
        ↓
Run dbt Models
        ↓
Run dbt Tests
        ↓
Publish Analytics Tables
```

---

## Dashboard Metrics

The reporting layer includes:

- Open Price
- Close Price
- High Price
- Low Price
- Trading Volume
- Daily Returns
- Moving Averages
- Historical Performance Trends

---

## Learning Outcomes

This project demonstrates:

- Modern Data Stack
- ELT Pipeline Design
- Data Lake Architecture
- Cloud Data Engineering
- Workflow Scheduling
- Analytics Engineering
- Data Modeling
- Financial Data Processing

---

## Future Enhancements

- Kafka Streaming
- Real-Time Processing
- CI/CD with GitHub Actions
- Data Lineage Tracking
- Great Expectations Data Quality Checks
- Multi-Source Market Data Integration

---

## Author

### Akshay Vishwakarma

- GitHub: https://github.com/akshayiitr04
---

## Acknowledgements
If you found this project useful, please consider giving it a ⭐.
