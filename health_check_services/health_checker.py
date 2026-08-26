import asyncio

import requests


SERVICES = {
    "authentication": "http://127.0.0.1:8001/internal/health",
    "payment": "http://127.0.0.1:8002/internal/health",
    "notification": "http://127.0.0.1:8003/internal/health",
}


def _check_service(name: str, url: str) -> dict:
    try:
        response = requests.get(url, timeout=2)
        data = response.json()
        is_healthy = response.status_code == 200 and data.get("status") == "ok"

        return {
            "name": name,
            "status": "up" if is_healthy else "down",
            "status_code": response.status_code,
            "details": data,
        }
    except requests.RequestException as exc:
        return {
            "name": name,
            "status": "down",
            "error": str(exc),
        }


async def check_all_services() -> list[dict]:
    checks = [
        asyncio.to_thread(_check_service, name, url)
        for name, url in SERVICES.items()
    ]
    return await asyncio.gather(*checks)


def calculate_overall_status(services: list[dict]) -> str:
    return "healthy" if all(
        service.get("status") == "up"
        for service in services
    ) else "unhealthy"
