from fastapi import FastAPI
from fastapi.responses import JSONResponse

from health_check_services.health_checker import check_all_services


app = FastAPI(
    title="Healthcare Platform Health Check Service",
    description="Monitors the health of critical healthcare platform services."
)


@app.get("/")
async def root():
    return {
        "service": "health-check-service",
        "status": "running"
    }


@app.get("/health")
async def health():
    services = await check_all_services()

    all_healthy = all(
        service["status"] == "up"
        for service in services
    )

    overall_status = "healthy" if all_healthy else "unhealthy"

    return JSONResponse(
        status_code=200 if all_healthy else 503,
        content={
            "status": overall_status,
            "services": services
        }
    )