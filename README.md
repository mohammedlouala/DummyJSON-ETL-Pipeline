# DummyJSON ETL Pipeline

An end-to-end ETL pipeline that extracts data from the [DummyJSON API](https://dummyjson.com/), transforms the data using Pandas, and loads the result into PostgreSQL.

## Project Overview

This project was built to practice the fundamentals of data engineering and to understand how a simple ETL pipeline works from API extraction to database loading.

The pipeline follows three main steps:

```text
DummyJSON API
      ↓
   Extract
      ↓
  Transform
      ↓
     Load
      ↓
 PostgreSQL
```

## Technologies

* Python
* Pandas
* Requests
* SQLAlchemy
* PostgreSQL
* python-dotenv
* Git / GitHub

## Data Sources

The pipeline extracts data from the following DummyJSON endpoints:

* Products
* Users
* Carts
* Posts

Nested data is also transformed into separate datasets, such as cart items and tags.

## Project Structure

```text
DummyJSON-ETL-Pipeline/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
│
├── sql/
│
└── src/
    ├── __init__.py
    ├── extract.py
    ├── transform.py
    ├── load.py
    └── main.py
```

### `src/extract.py`

Handles data extraction from the DummyJSON API.

The API responses are converted into Pandas DataFrames.

### `src/transform.py`

Cleans and transforms the extracted data.

Main transformations include:

* Selecting required columns
* Renaming columns
* Checking missing values
* Checking duplicate values
* Checking empty strings
* Checking negative values
* Flattening nested JSON data
* Using `explode()` for nested lists
* Creating separate datasets for cart items and tags

### `src/load.py`

Loads transformed DataFrames into PostgreSQL using SQLAlchemy.

The data is loaded into the `silver` schema.

### `src/main.py`

Orchestrates the complete ETL pipeline.

It executes the transformation and loading steps for each dataset.

## Database Tables

The pipeline produces the following datasets:

```text
products
users
carts
cart_items
posts
tags
```

These datasets are loaded into the PostgreSQL `silver` schema.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/mohammedlouala/DummyJSON-ETL-Pipeline.git
cd DummyJSON-ETL-Pipeline
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file from `.env.example`:

```text
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
```

Do not commit the `.env` file to GitHub.

### 5. Run the pipeline

From the project root:

```bash
python -m src.main
```

The pipeline will:

1. Extract data from DummyJSON.
2. Transform and clean the data.
3. Load the transformed datasets into PostgreSQL.

## Data Quality Checks

During the transformation phase, the project checks for common data quality issues:

* Missing values
* Duplicate rows
* Duplicate IDs
* Empty strings
* Leading/trailing spaces
* Negative numeric values

## Learning Goals

This project focuses on practicing:

* REST API data extraction
* JSON handling
* Pandas DataFrame transformations
* Nested JSON normalization
* `explode()`
* Data quality checks
* Environment variables
* SQLAlchemy
* PostgreSQL
* ETL pipeline structure
* Git and GitHub workflow

## Future Improvements

Possible improvements for future versions:

* Add logging
* Add error handling and retries
* Add incremental loading
* Add database constraints
* Add automated tests
* Add Docker
* Add an orchestration tool such as Airflow
* Add a data warehouse layer

## Author

**Mohammed**

This project is part of my Data Engineering learning journey.
