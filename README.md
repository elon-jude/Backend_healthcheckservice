Healthcare Health Check Service

A backend health monitoring service built with **Python** and **FastAPI** for monitoring the availability of healthcare application services.

The project monitors three backend services:

- Authentication Service
- Payment Service
- Notification Service

The health check API exposes a `/health` endpoint that checks the monitored services and reports the health of the overall system.

Project Structure

```text
health_check_services/
├── app.py
└── health_checker.py

services/
├── authentication.py
├── payment.py
└── notification.py

requirements.txt
.gitignore
README.md
```

Technologies Used

- Python 3.11
- FastAPI
- Uvicorn
- HTTPX

How It Works

The health check service sends HTTP requests to the internal health endpoints of the monitored services.

Each service can report:

- Service name
- Service status
- HTTP status code
- Response details
- Error information when unavailable

The overall system is considered **healthy** when all monitored services are operational.

If one or more services are unavailable, the overall status becomes **unhealthy** and the health-check API returns HTTP `503 Service Unavailable`.

Health Endpoint

```http
GET /health
```

Example Response

```json
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

In this example, the authentication and payment services are operational, while the notification service is unavailable. Therefore, the overall system is reported as `unhealthy`.

Running the Project
1. Clone the repository

git clone https://github.com/elon-jude/Backend_healthcheckservice.git
cd Backend_healthcheckservice

2. Create a virtual environment

python -m venv .venv

3. Activate the virtual environment

.venv\Scripts\Activate.ps1

4. Install dependencies

pip install -r requirements.txt

5. Start the application

uvicorn health_check_services.app:app --reload --port 8000

The API will be available at:
http://127.0.0.1:8000

The health endpoint is:
http://127.0.0.1:8000/health

FastAPI documentation is available at:
http://127.0.0.1:8000/docs

Failure Detection

If a monitored service stops responding or returns an unsuccessful response, the health checker records the service as `down`.

For example:

```text
authentication → up
payment        → up
notification   → down
```

The health endpoint will then report:

```text
Overall status → unhealthy
HTTP status    → 503
```

This allows another monitoring system to detect that the healthcare application's backend is experiencing a service failure.

Production Monitoring
Alerts could be configured to trigger after several consecutive failures rather than immediately after one failed request.

Useful monitoring information includes:

- HTTP status codes
- Response times
- Service availability
- Error messages
- Failure counts
- Application logs
This information can help determine whether a problem is caused by a service outage, network issue, timeout, or temporary failure.

Project Purpose

This project demonstrates:
- Backend health checks
- Microservice availability monitoring
- HTTP communication between services
- Error handling
- HTTP status codes
- Service failure detection
- Basic production monitoring concepts

The project uses a healthcare application scenario to demonstrate how backend services can be monitored and how failures can be detected before they affect the wider system.

GitHub repository:
https://github.com/elon-jude/Backend_healthcheckservice
