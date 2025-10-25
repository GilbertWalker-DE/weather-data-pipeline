🌦️ Weather Data Pipeline Project

🚀 Beginner | End-to-End Data Engineering Pipeline (Python, PostgreSQL, Airflow, dbt, Superset, Docker)

🧩 Project Overview

This project demonstrates the creation of a modern data pipeline that ingests weather data from an external API, stores it in a PostgreSQL database, transforms it using dbt, orchestrates workflows via Apache Airflow, and visualizes insights in Apache Superset — all within a containerized environment using Docker.

⚙️ This project was developed as a hands-on learning exercise following a guided walkthrough by Tech With Tim’s YouTube tutorial
.
While the walkthrough provided general guidance, the majority of Python scripts, SQL models, configuration files, and debugging were completed manually. The process was highly instructive and required extensive troubleshooting and problem-solving across multiple tools.

🧠 Objectives

Build an ETL data pipeline from API to dashboard

Practice data orchestration and automation using Apache Airflow

Learn data transformation principles using dbt

Deploy open-source analytics tools (Superset) within Docker

Strengthen understanding of end-to-end data engineering workflows

🏗️ Tech Stack
Layer	Tool	Purpose
Data Source	Weatherstack API
	Real-time weather data
Programming	Python	API requests and data ingestion
Storage	PostgreSQL	Data warehouse
Transformation	dbt (Data Build Tool)	SQL-based modeling
Orchestration	Apache Airflow	DAG automation
Visualization	Apache Superset	Data visualization
Infrastructure	Docker & Docker Compose	Containerized deployment
Environment	WSL2 (Ubuntu) + VS Code	Local development
🔄 Workflow Summary

Extract:

Fetch live weather data from Weatherstack API using Python.

Store raw data in PostgreSQL via psycopg2.

Transform (dbt):

Create staging and analytics models to clean, aggregate, and prepare data.

Build models for metrics like daily averages and weather summaries.

Orchestrate (Airflow):

Define DAGs for ingestion, transformation, and dependency management.

Automate end-to-end flow between extract → transform → load.

Visualize (Superset):

Connect to PostgreSQL models and visualize trends.

Example: temperature and weather condition dashboards.

📁 Project Structure
weather-data-project/
│
├── dags/
│   ├── ingest_weather_data.py        # Python script for API ingestion
│   ├── transform_data_set.py         # Executes dbt transformations
│   └── orchestrator.py               # Defines task dependencies
│
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   │   └── stg_weather_data.sql  # Cleans and structures raw data
│   │   └── analytics/
│   │       ├── daily_average.sql     # Aggregates daily metrics
│   │       └── weather_report.sql    # Builds summary-level report
│   └── dbt_project.yml               # dbt configuration file
│
├── docker-compose.yml                # Multi-container setup
├── requirements.txt                  # Python dependencies
├── images/
│   └── AirflowDAGProcess_Weather.png # Airflow DAG success screenshot
└── README.md

📸 Sample Output

Airflow DAG Execution:
![Airflow DAG](images/AirflowDAGProcess_Weather.png)


🧩 Lessons Learned

Configuring Docker containers to network across multiple services (Postgres, Airflow, dbt, Superset)

Troubleshooting permissions, authentication, and pathing issues within WSL2

Managing DAG dependencies and execution order in Apache Airflow

Writing modular SQL transformations within dbt

Setting up Superset to connect to live database tables for visualization

✍️ Personal Note

This was my first full data engineering project built from the ground up.
While I followed a structured walkthrough, much of the implementation — including Python ingestion scripts, SQL model development, debugging, and Docker environment setup — was manually completed.
It was a highly tedious yet rewarding process that deepened my understanding of real-world data engineering workflows.

⚙️ Setup Instructions

Follow these steps to run the project locally:

1️⃣ Clone the Repository
git clone https://github.com/GilbertWalker-DE/weather-data-pipeline.git
cd weather-data-pipeline

2️⃣ Set Up Your Virtual Environment
python -m venv .venv
# Activate the environment
# Windows:
source .venv/Scripts/activate
# Linux/Mac:
source .venv/bin/activate

3️⃣ Install Required Dependencies
pip install -r requirements.txt

4️⃣ Configure PostgreSQL Database

Create a new PostgreSQL database named weather_db.

Run the SQL script below to create the table structure:

psql -U your_username -d weather_db -f sql/create_weather_table.sql


Update your Airflow connection (or .env file, if applicable) with the correct database credentials.

5️⃣ Start Apache Airflow

Initialize Airflow and start the web server and scheduler:

airflow db init
airflow webserver --port 8080
airflow scheduler


Then visit: http://localhost:8080

6️⃣ Trigger the DAG

In the Airflow UI, locate the DAG named weather_dag.

Turn it on and run it manually or let it schedule automatically.

7️⃣ Verify Successful Execution

Open the Graph View or Logs tab in Airflow to confirm all tasks succeeded.

You should see results in your PostgreSQL table and a completed DAG run.

🏁 Next Steps

Expand dbt models with more advanced transformations (joins, rollups, CTEs)

Introduce data validation and quality checks

Deploy the full pipeline in a cloud environment (AWS RDS + MWAA)

Improve Superset dashboard interactivity and design

📚 Acknowledgment

🎥 Tutorial Reference: End-to-End Data Engineering Project with Docker, Airflow, dbt, and Superset

👤 Author

Gilbert Walker
Data Conversion Specialist | Aspiring Data Engineer
📍 Bethlehem, Georgia
🔗 GitHub: GilbertWalker-DE


## 📸 Sample Output  
**Airflow DAG Execution:**  
![Airflow DAG](images/AirflowDAGProcess_Weather.png)
