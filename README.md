# Healthcare Health Check Service

A simple backend health monitoring service built with Python and FastAPI.

The service monitors the availability of three healthcare-related backend services:

- Authentication Service
- Payment Service
- Notification Service

It exposes a /health endpoint that reports the health status of each service and the overall system.

## Project Structure

text
health_check_services/
    app.py
    health_checker.py
services/
    authentication.py
    payment.py
    notification.py
    
Technologies Used
*Python
*FastAPI
*Uvicorn
*HTTPX

How It Works
The health check service sends requests to the internal health endpoints of the monitored services.
Each service reports:
  Service name
  Status
  HTTP status code
  Response details
  Error information when unavailable
The overall system is considered healthy only when all monitored services are operational.
If one or more services are unavailable, the overall health status becomes unhealthy and the API returns HTTP 503.

Health Endpoint
GET /health

Example response:
```
{
  "status": "unhealthy",
  "services": [
    {
      "name": "authentication",
      "status": "up",
      "status_code": 200,
      "details": {
        "status": "ok",
        "checks": {
          "database": "ok",
          "token_store": "ok",
          "jwt_keys": "ok"
        }
      }
    },
    {
      "name": "payment",
      "status": "up",
      "status_code": 200,
      "details": {
        "status": "ok",
        "checks": {
          "database": "ok",
          "payment_gateway": "ok",
          "webhook_listener": "ok"
        }
      }
    },
    {
      "name": "notification",
      "status": "down",
      "error": "Connection timeout"
    }
  ]
}
```
Running the Project
Create and activate a virtual environment:
python -m venv .venv
.venv\Scripts\activate
Install the dependencies:
pip install -r requirements.txt

Start the healthcare services and health-check API using Uvicorn.
The health endpoint can then be accessed at:
http://127.0.0.1:8000/health

Production Monitoring
Alerts can be configured for repeated failures rather than a single failed request. Response times, HTTP status codes, logs, and failure counts can help identify whether an issue is caused by a service outage, network problem, or temporary failure.

Project Purpose
This project demonstrates basic backend service monitoring, health checks, HTTP communication, error handling, and service availability detection in a healthcare application environment.
