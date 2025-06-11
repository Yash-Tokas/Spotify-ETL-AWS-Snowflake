# 🎵 Spotify Analytics ETL Pipeline with AWS, Snowflake & Power BI

A fully automated, serverless ETL pipeline that extracts data from Spotify API, transforms it, and loads it into Snowflake for advanced analytics and visualization in Power BI. Built using AWS Lambda, S3, Snowpipe, and CloudWatch.

![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange?logo=amazon-aws&logoColor=white)
![Amazon S3](https://img.shields.io/badge/Amazon-S3-green?logo=amazon-aws&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-Data%20Warehouse-blue?logo=snowflake&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Visualization-yellow?logo=powerbi&logoColor=white)
![Spotify API](https://img.shields.io/badge/Spotify-API-brightgreen?logo=spotify&logoColor=white)
![Python](https://img.shields.io/badge/Python-Data%20Extraction-blue?logo=python&logoColor=white)

**Project Description:**  
Serverless ETL pipeline for Spotify analytics leveraging AWS Lambda, Amazon S3, Snowpipe, and Snowflake, with Power BI dashboards for near real-time data insights.

## Overview

This project implements a **serverless ETL pipeline** to extract data from the Spotify API, transform it, and load it into Snowflake for advanced analytics and visualization using Power BI.

The goal is to enable **near real-time insights** on Spotify streaming data by leveraging modern cloud-native services with automated orchestration and scaling.

## Architecture Workflow

### Extract (Spotify API → AWS Lambda → S3)

- Extracts data from Spotify API using Python and the Spotipy package.
- AWS Lambda (Extraction Function) is triggered by Amazon CloudWatch on a **daily schedule**.
- Extracted raw data is stored in **Amazon S3** as JSON files.

### Transform (AWS Lambda → S3)

- An **S3 Object PUT event** triggers a second AWS Lambda (Transformation Function).
- The Lambda performs necessary data cleaning, normalization, and transformation.
- Transformed data is written back to S3 in a **separate folder** ready for loading.

### Load & Analyze (Snowpipe → Snowflake → Power BI)

- **Snowpipe** continuously ingests transformed data from S3 into **Snowflake**.
- Data is modeled within Snowflake using **SQL-based transformations**.
- **Power BI** connects live to Snowflake to visualize Spotify analytics dashboards.

## Technologies Used

- **Spotify API** → Data source for streaming and metadata.
- **Python** → Used in AWS Lambda for Extraction and Transformation.
- **AWS Lambda** → Serverless compute to automate ETL logic.
- **Amazon CloudWatch** → Scheduling Lambda extraction functions.
- **Amazon S3** → Storage of raw and transformed data.
- **S3 Trigger** → Event-driven transformation process.
- **Snowpipe** → Continuous, automated data loading into Snowflake.
- **Snowflake** → Cloud Data Warehouse for scalable analytics.
- **Power BI** → Visualization layer for creating dashboards and reports.

## Automation

- AWS CloudWatch triggers periodic **Spotify data extraction**.
- S3 Object PUT event triggers **automatic data transformation**.
- Snowpipe **auto-ingests transformed data** to Snowflake without manual intervention.
- **Power BI dashboards** are connected to live Snowflake views for always up-to-date insights.

## Setup & Deployment

1. **Obtain Spotify API credentials** (Client ID & Secret) and configure Spotipy in Lambda.
2. **Deploy AWS Lambda Functions**:
    - Extraction Lambda → Fetches Spotify data, writes raw JSON to S3.
    - Transformation Lambda → Cleans/transforms data, writes to a separate S3 folder.
3. **Configure Amazon CloudWatch** to trigger Extraction Lambda daily/weekly.
4. **Enable S3 PUT Trigger** to invoke the Transformation Lambda.
5. **Configure Snowpipe** to monitor the transformed data S3 path and auto-load data into Snowflake.
6. **Connect Power BI** to Snowflake using Snowflake Connector → Build interactive dashboards.

## Usage

- **Extract** Spotify data → Stored in S3 (Raw).
- **Transform** data using Lambda → Stored in S3 (Transformed).
- **Load** transformed data into Snowflake via Snowpipe.
- **Visualize** Spotify analytics in Power BI dashboards.

Example Use Cases:
- Daily/weekly Spotify stream trends.
- Artist/track popularity over time.
- Playlist analytics.
- Audience insights by geography.

## Final Note

This architecture provides a **modern, fully automated, serverless, and scalable ETL pipeline** for near real-time Spotify data analytics using AWS and Snowflake.

It demonstrates key data engineering concepts:
- Serverless orchestration
- Event-driven pipelines
- Continuous data ingestion
- Cloud-native data warehousing
- Business analytics and visualization.

---

## 📈 Project Summary (for LinkedIn / Portfolio / GitHub pinned repo)

**Designed and implemented an automated Spotify Analytics ETL pipeline leveraging AWS Lambda, S3, Snowpipe, and Snowflake. The solution extracts data from Spotify API, transforms it in real-time, and loads it into Snowflake for advanced visualization in Power BI. The architecture is fully serverless and scalable, enabling near real-time Spotify data insights. Great example of modern data engineering practices using cloud-native tools.**
