# AI-Powered Log Anomaly Detection

## Overview
Detect anomalies in distributed system logs using a Transformer model and GPT-4 for automatic incident summaries.

## Features
- Real-time log ingestion with Kafka
- Fast anomaly search with OpenSearch (placeholder)
- AI-powered log anomaly detection
- GPT-4 generated root cause analysis

## Structure
- `data/` : Sample logs
- `kafka_pipeline/` : Kafka producer & consumer
- `model/` : Transformer training
- `gpt_integration/` : GPT-4 summary scripts

## Usage
1. Start Kafka and create topic `logs`
2. Run `producer.py` to send logs
3. Run `consumer.py` to receive logs
4. Train model with `train_transformer.py`
5. Generate summaries with `generate_summary.py`
