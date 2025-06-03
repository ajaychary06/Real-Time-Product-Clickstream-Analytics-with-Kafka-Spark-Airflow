# 📊Real-Time-Product-Clickstream-Analytics-with-Kafka-Spark-Airflow

A complete end-to-end pipeline that captures, processes, and visualizes real-time product clickstream data using Apache Kafka, Spark Structured Streaming, Apache Airflow, and Flask. This project simulates real-world scenarios of handling streaming data for real-time decision-making and product insight generation.

## 🚀 Project Overview
This project simulates a real-time product analytics pipeline that captures user clickstream events (user ID, product name, timestamp) and performs real-time aggregation and visualization. From ingestion to dashboarding, it covers the full data engineering and analytics lifecycle.

Key Features:
- Real-time event ingestion using Kafka

- Streaming aggregation with Spark Structured Streaming

- Orchestration via Apache Airflow

- Dual data storage in Parquet and CSV formats

- Interactive dashboard using Flask + Plotly

- Dashboard auto-refresh and Bootstrap UI

- Optional visualization using Tableau or Power BI

- Deployed and documented for GitHub portfolio

## 🛠️ Tech Stack & Tools
| Layer             | Tools/Technologies                             |
| ----------------- | ---------------------------------------------- |
| Ingestion         | Apache Kafka                                   |
| Stream Processing | Apache Spark Structured Streaming              |
| Orchestration     | Apache Airflow (DAG-based pipeline management) |
| Storage           | Parquet & CSV                                  |
| Visualization     | Flask + Plotly + Bootstrap (dashboard)         |
| Optional BI       | Tableau / Power BI (CSV drag-and-drop import)  |
| Automation        | Python, Bash, crontab (optional)               |
| Deployment        | WSL (Ubuntu) + Windows                         |
| Version Control   | Git & GitHub                                   |

##📂 Project Structure

real-time-product-pipeline/
├── kafka_producer.py                  # Simulates real-time click events
├── spark_streaming_consumer.py       # Spark app to aggregate click counts
├── product_streaming_dag.py          # Airflow DAG to automate pipeline
├── app.py                            # Flask dashboard app
├── templates/
│   └── index.html                    # Dashboard UI with Plotly charts
├── Screenshots/                      # Dashboard, Airflow, Parquet UI
├── README.md                         # You're reading this


## 📈 Workflow

### 1. Kafka Producer
Simulates user clickstream data (user_id, product, timestamp) and sends it to the Kafka topic product_clicks.

### 2. Spark Structured Streaming
Consumes Kafka stream in real-time, parses and cleans it, aggregates product click counts over 10-second windows, and writes results in both Parquet and CSV formats (one batch per window).

### 3. Airflow DAG
Runs a DAG named kafka_spark_streaming_pipeline which triggers the Spark job on demand or on a schedule.

### 4. Dashboard (Flask + Plotly)
- Reads aggregated parquet files.
- Displays:
  - Bar chart: Most clicked products
  - Line chart: Product clicks over time
- Uses <meta> or JS-based auto-refresh for real-time UX.
- Enhanced with Bootstrap for styling.

### 5. Optional: Tableau / Power BI

- Load the CSVs via drag-and-drop.

- Analyze trends and export visuals.

## 📊 Sample Visualizations

<p align="center"> <img src="Screenshots/Flask%20With%20BS%20Dashboard1.jpeg" width="70%"> </p>

## ✅ How to Run
Works with Kafka, Spark, and Airflow all locally (tested on Windows + Ubuntu WSL)

### Step-by-Step:
1. Start Kafka (Windows)

2. Run Kafka Producer
'''
python3 kafka_producer.py

'''
3. Run Spark Consumer
'''
spark-submit spark_streaming_consumer.py
'''
4. Start Airflow Scheduler (Ubuntu)
'''
source ~/airflow_env/bin/activate
airflow scheduler
'''
5. Start Flask Dashboard
'''
python3 app.py

'''

## 📷 Screenshots

- Kafka data injection

- Spark logs with aggregation

- Airflow DAG UI

- Parquet & CSV file output

- Flask dashboard views
  
- Optional Tableau charts

## 🧠 Learnings

- Handling real-time data ingestion, processing, and visualization

- Orchestrating pipelines with Airflow

- Dual storage strategies (CSV for BI tools, Parquet for performance)

- Auto-refresh dashboards

- Combining WSL (Ubuntu) and Windows for hybrid workflows

## 🔗 GitHub Repo

https://github.com/ajaychary06/Real-Time-Product-Clickstream-Analytics-with-Kafka-Spark-Airflow.git











