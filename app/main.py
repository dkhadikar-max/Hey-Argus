from fastapi import FastAPI

app = FastAPI(
    title="Hey Argus",
    version="0.1.0",
    description="Secure personal agentic AI operating assistant.",
)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "hey-argus"}
