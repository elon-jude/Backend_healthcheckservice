from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI(title="Notification Service")


# Simulated notification dependencies
_state = {
    "sms_provider": "ok",
    "email_provider": "ok",
}


class ToggleRequest(BaseModel):
    component: str
    status: str


@app.get("/")
def root():
    return {
        "service": "notification",
        "message": "Notification service is running"
    }


@app.get("/internal/health")
def health(response: Response):

    checks = dict(_state)

    overall_ok = all(
        status == "ok"
        for status in checks.values()
    )

    if not overall_ok:
        response.status_code = 503

    return {
        "status": "ok" if overall_ok else "down",
        "checks": checks
    }


@app.post("/internal/toggle")
def toggle(request: ToggleRequest):

    if request.component not in _state:
        return Response(status_code=400)

    _state[request.component] = request.status

    return {
        "component": request.component,
        "status": request.status
    }