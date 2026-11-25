# API Sentinel

### Production-Ready API Monitoring, Observability & Anomaly Detection Platform

API Sentinel is a cloud-native API monitoring and observability platform designed to monitor HTTP endpoints, collect historical performance data, detect anomalies, and provide actionable alerts when monitored services become unavailable or experience abnormal behavior.

The platform combines asynchronous task processing, persistent monitoring history, statistical and machine-learning-based anomaly detection, and cloud-native observability to provide visibility into API health and performance.

---

## 1. Project Overview

Modern applications depend on multiple APIs and external services. Service disruptions, increased response times, and unexpected HTTP errors can affect application availability and reliability.

API Sentinel addresses these challenges through:

- Automated HTTP endpoint monitoring.
- Scheduled monitoring using Celery Beat.
- Asynchronous monitoring execution using Celery workers.
- Persistent monitoring history using PostgreSQL.
- Redis-based task queuing.
- Statistical and machine-learning anomaly detection.
- Alert generation and AI-assisted alert explanations.
- Prometheus metrics collection.
- Grafana Cloud dashboards and alerting.
- Kubernetes-based deployment.

**Primary objective:** Build a production-oriented monitoring system that demonstrates backend engineering, asynchronous processing, data engineering, observability, anomaly detection, and cloud infrastructure deployment.

---

## 2. Architecture

### High-Level Architecture

```mermaid
flowchart TD
    A[User / Client] --> B[FastAPI]
    B --> C[PostgreSQL]
    D[Celery Beat] --> E[Redis]
    E --> F[Celery Worker]
    F --> G[HTTPX Monitoring Engine]
    G --> H[External APIs]
    G --> C
    C --> I[Historical Monitoring Data]
    I --> J[Statistical Anomaly Detection]
    J --> K[ML Anomaly Detection]
    K --> L[Alert Engine]
    L --> M[AI Alert Explanation]
    B --> N[Prometheus Metrics]
    N --> O[Grafana Alloy]
    O --> P[Grafana Cloud]
    P --> Q[Dashboards and Alert Rules]
```

### System Components

| Component | Responsibility |
|---|---|
| FastAPI | REST API and application endpoints |
| PostgreSQL | Monitoring configuration and historical results |
| SQLAlchemy | Database ORM and persistence |
| Redis | Celery message broker |
| Celery Beat | Periodic monitoring task scheduling |
| Celery Worker | Asynchronous monitoring execution |
| HTTPX | HTTP endpoint health checks |
| Prometheus | Application metrics |
| Grafana Alloy | Metrics collection and forwarding |
| Grafana Cloud | Visualization, observability and alerting |
| Kubernetes | Container orchestration |
| Google Kubernetes Engine | Cloud deployment infrastructure |
| Cloudflare Tunnel | External access to the deployed API |
| Docker | Containerization |

---

## 3. Core Features

### 3.1 HTTP Endpoint Monitoring

Monitor external HTTP endpoints and collect:

- HTTP response status.
- Response time.
- Endpoint availability.
- Monitoring execution results.
- Historical monitoring information.

### 3.2 Automated Scheduling

Celery Beat periodically dispatches monitoring tasks.

Celery workers execute monitoring jobs asynchronously, allowing the API application to remain independent of long-running monitoring operations.

### 3.3 Historical Data Persistence

PostgreSQL stores monitoring configurations and execution results.

The historical dataset provides the foundation for performance analysis and anomaly detection.

### 3.4 Anomaly Detection

The platform incorporates multiple analytical approaches:

- Statistical anomaly detection.
- Machine-learning-based anomaly detection.
- Historical performance analysis.

These approaches help identify unusual monitoring behavior and performance deviations.

### 3.5 Alert Management

API Sentinel generates alerts based on monitoring failures and detected anomalies.

AI-assisted explanations provide additional context to help interpret alerts.

---

## 4. Technology Stack

| Category | Technologies |
|---|---|
| Backend | Python, FastAPI |
| API communication | HTTPX |
| Validation | Pydantic |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Task processing | Celery |
| Scheduler | Celery Beat |
| Message broker | Redis |
| Monitoring | Prometheus |
| Metrics collection | Grafana Alloy |
| Visualization | Grafana Cloud |
| Containers | Docker |
| Orchestration | Kubernetes |
| Cloud infrastructure | Google Cloud Platform, GKE |
| External access | Cloudflare Tunnel |

---

## 5. Database Architecture

The application uses PostgreSQL for persistent storage.

Core database tables include:

| Table | Purpose |
|---|---|
| monitors | Stores monitored endpoint configurations |
| monitoring_results | Stores historical monitoring execution results |
| alerts | Stores generated monitoring alerts |

SQLAlchemy handles database interactions, while Alembic manages database schema migrations.

---

## 6. Application Monitoring and Observability

API Sentinel exposes Prometheus-compatible application metrics through:

```text
/metrics
```

The metrics endpoint is instrumented using `prometheus-fastapi-instrumentator`.

### Metrics collected

Examples include:

- `http_requests_total`
- `http_request_duration_seconds_bucket`
- `http_request_duration_highr_seconds_bucket`
- `process_cpu_seconds_total`
- `process_resident_memory_bytes`

### Monitoring pipeline

```text
FastAPI
   |
   v
/metrics
   |
   v
Grafana Alloy
   |
   v
Grafana Cloud Prometheus
   |
   v
Grafana Dashboard
```

Grafana Alloy scrapes application metrics every 30 seconds and forwards them to Grafana Cloud.

### Grafana Dashboard

The API Sentinel production observability dashboard includes:

1. Total API Requests
2. Request Rate by Endpoint
3. HTTP Response Status Distribution
4. API Request Latency (p50, p95, p99)
5. API Error Rate
6. API Availability
7. API Process CPU Usage
8. API Process Memory Usage
9. HTTP Request Volume by Endpoint

### Grafana Alerting

Three alert rules are configured.

| Alert | Condition | Evaluation |
|---|---|---|
| API Unavailable | Scrape value below 0.5 | 2-minute pending period |
| High HTTP 5xx Error Rate | Error rate above 5% | 5-minute pending period |
| High API Latency | p95 latency above 1 second | 5-minute pending period |

Email notifications are configured through a Grafana Cloud contact point.

The email contact point has been tested successfully.

---

## 7. Containerization

Docker is used to package application components into containers.

The platform includes separate application processes for:

- FastAPI application.
- Celery Beat scheduler.
- Celery worker.

PostgreSQL and Redis provide persistent storage and message-broker functionality.

Docker Compose is used for local multi-container development.

---

## 8. Kubernetes Deployment

API Sentinel is deployed on Google Kubernetes Engine.

### Deployment components

| Workload | Purpose |
|---|---|
| api-sentinel-api | FastAPI application |
| celery-beat | Scheduled task dispatch |
| celery-worker | Asynchronous task execution |
| postgres | Persistent database |
| redis | Message broker |
| api-sentinel-tunnel | External application access |

### Kubernetes capabilities demonstrated

- Deployments and StatefulSets.
- ClusterIP services.
- ConfigMaps and Secrets.
- PersistentVolumeClaims.
- Container image management.
- Pod health and readiness verification.
- Application rollout and deployment management.
- Namespace isolation.

### Cluster information

| Configuration | Value |
|---|---|
| Cloud provider | Google Cloud |
| Kubernetes service | Google Kubernetes Engine |
| Cluster | api-sentinel-gke |
| Region | asia-south1 |
| Namespace | api-sentinel |

### Useful Kubernetes commands

Check application pods:

```bash
kubectl get pods -n api-sentinel
```

Check services:

```bash
kubectl get services -n api-sentinel
```

Check deployments:

```bash
kubectl get deployments -n api-sentinel
```

View API logs:

```bash
kubectl logs deployment/api-sentinel-api -n api-sentinel
```

Check deployment rollout:

```bash
kubectl rollout status deployment/api-sentinel-api -n api-sentinel
```

---

## 9. Local Development Setup

### Prerequisites

- Python
- Docker
- Docker Compose
- PostgreSQL-compatible database configuration
- Redis
- Git

### Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

```bash
cd api-sentinel
```

### Configure environment variables

Create a `.env` file containing the environment variables required by the application.

Example configuration:

```env
POSTGRES_PASSWORD=<YOUR_DATABASE_PASSWORD>
GEMINI_API_KEY=<YOUR_GEMINI_API_KEY>
```

Add any additional variables required by the application configuration.

Never commit `.env` files, API keys, database credentials, or cloud access tokens.

### Start the application

```bash
docker compose up --build -d
```

Check running containers:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs -f
```

Stop the application:

```bash
docker compose down
```

---

## 10. API Health Verification

The application exposes a health endpoint:

```text
/health
```

Example local verification:

```bash
curl http://localhost:8000/health
```

The metrics endpoint can be accessed through:

```text
/metrics
```

API documentation is available through the FastAPI Swagger interface:

```text
/docs
```

Production documentation access may be protected by Cloudflare Access.

---

## 11. Security Considerations

The deployment uses environment-based configuration and Kubernetes Secrets for sensitive credentials.

Security considerations include:

- Avoid committing credentials to Git.
- Store API keys outside source code.
- Use Kubernetes Secrets for deployment credentials.
- Protect production documentation endpoints.
- Restrict access to monitoring infrastructure.
- Use authenticated cloud services for metrics ingestion.
- Rotate credentials if they are exposed.

---

## 12. Project Outcomes

API Sentinel demonstrates the implementation and integration of:

- REST API development.
- Asynchronous task processing.
- Database architecture and persistence.
- Scheduled background execution.
- HTTP service monitoring.
- Historical data processing.
- Statistical and machine-learning anomaly detection.
- Alert management.
- Prometheus instrumentation.
- Grafana Cloud observability.
- Docker containerization.
- Kubernetes orchestration.
- Google Cloud deployment.

The project brings together backend development, data engineering, machine learning, DevOps, and production observability in one integrated system.

---

## 13. Future Improvements

Potential future extensions include:

- Multi-tenant monitoring.
- Advanced anomaly detection.
- More configurable alert policies.
- Additional notification integrations.
- Distributed monitoring agents.
- Advanced service-level objective reporting.

These are future possibilities and are not required for the current project release.

---

## 14. Project Status

**Project:** API Sentinel

**Category:** Backend Engineering | MLOps | DevOps | Observability

**Deployment:** Google Kubernetes Engine

**Monitoring:** Grafana Cloud and Prometheus-compatible metrics

**Status:** Core implementation and deployment completed; final documentation and verification in progress.

---

## Author

Developed as a production-oriented engineering portfolio project.

**Focus areas:** Python Backend Development, API Engineering, Data Analytics, Machine Learning, DevOps and Cloud Infrastructure.
