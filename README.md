# 🌦️ Weather Data Pipeline Project  
🚀 Beginner | End-to-End Data Engineering Pipeline (Python, PostgreSQL, Airflow, dbt, Superset, Docker)

---

## 🧩 Project Overview  
This project demonstrates the creation of a **modern data pipeline** that ingests weather data from an external API, stores it in a PostgreSQL database, transforms it using dbt, orchestrates workflows via Apache Airflow, and visualizes insights in Apache Superset — all within a containerized environment using Docker.

> ⚙️ This project was developed as a hands-on learning exercise following a guided walkthrough by [Tech With Tim’s YouTube tutorial](https://youtu.be/vMgFadPxOLk?si=WK15RGHJkvRZsKP7).  
> Some code and configurations were provided in the walkthrough. However, I independently handled setup, troubleshooting (Docker, Airflow, dbt, and PostgreSQL connections), and project execution in **WSL2 (Ubuntu)** with **VS Code**.

---

## 🧠 Objectives
- Build an **ETL data pipeline** from API to dashboard  
- Practice **data orchestration and automation** using Apache Airflow  
- Learn **data transformation** principles using dbt  
- Deploy **open-source analytics tools** (Superset) within Docker  
- Strengthen understanding of **end-to-end data engineering workflows**

---

## 🏗️ Tech Stack
| Layer | Tool | Purpose |
|-------|------|----------|
| Data Source | [Weatherstack API](https://weatherstack.com/) | Real-time weather data |
| Programming | Python | API requests and data ingestion |
| Storage | PostgreSQL | Data warehouse |
| Transformation | dbt (Data Build Tool) | SQL-based modeling |
| Orchestration | Apache Airflow | DAG automation |
| Visualization | Apache Superset | Data visualization |
| Infrastructure | Docker & Docker Compose | Containerized deployment |
| Environment | WSL2 (Ubuntu) + VS Code | Local development |

---

## 🔄 Workflow Summary
1. **Extract:**  
   - Fetch live weather data from Weatherstack API using Python.  
   - Store raw data in PostgreSQL via `psycopg2`.

2. **Transform (dbt):**  
   - Create staging and analytics models to clean, aggregate, and prepare data.  
   - Build models for metrics like daily averages and weather summaries.

3. **Orchestrate (Airflow):**  
   - Define DAGs for ingestion, transformation, and dependency management.  
   - Automate end-to-end flow between extract → transform → load.

4. **Visualize (Superset):**  
   - Connect to PostgreSQL models and visualize trends.  
   - Example: temperature and humidity dashboards.

---

## 🖥️ Project Structure
weather-data-project/
│
├── dags/
│ ├── ingest_weather_data.py
│ ├── transform_data_set.py
│ └── orchestrator.py
│
├── dbt/
│ ├── models/
│ │ ├── staging/
│ │ │ └── stg_weather_data.sql
│ │ └── analytics/
│ │ ├── daily_average.sql
│ │ └── weather_report.sql
│ └── dbt_project.yml
│
├── docker-compose.yml
├── requirements.txt
├── screenshots/
│ └── airflow_success_dag.png
└── README.md

yaml
Copy code

---

## 📸 Sample Output  
**Airflow DAG Execution:**  
![Airflow DAG](screenshots/airflow_success_dag.png)

---

## 🧩 Lessons Learned
- Managing Docker networking between services (Postgres, Airflow, dbt, Superset)  
- Debugging permission and connectivity issues in AWS & WSL2  
- Understanding DAG orchestration and dependencies in Airflow  
- Structuring dbt models for modular data transformation  
- Connecting analytical tools (Superset) to a live data warehouse  

---

## 🏁 Next Steps
- Add more complex transformations to dbt (joins, rolling averages)  
- Deploy to a cloud-hosted environment (AWS RDS + MWAA)  
- Expand visualization with interactive dashboards  

---

## 📚 Acknowledgment
This project follows the walkthrough:  
🎥 [**YouTube: End-to-End Data Engineering Project with Docker, Airflow, dbt, and Superset**](https://youtu.be/vMgFadPxOLk?si=WK15RGHJkvRZsKP7)

---

## 👤 Author
**Gilbert Walker**  
_Data Conversion Specialist | Aspiring Data Engineer_  
📍 Bethlehem, Georgia  
🔗 [GitHub: GilbertWalker-DE](https://github.com/GilbertWalker-DE)

---