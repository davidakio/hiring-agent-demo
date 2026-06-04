from fastapi import FastAPI
from pydantic import BaseModel

from .llm import screen_candidate

app = FastAPI(title="Hiring Agent")


class ScreenRequest(BaseModel):
    role: str
    cv_text: str


@app.post("/screen")
def screen(req: ScreenRequest) -> dict:
    return screen_candidate(req.cv_text, req.role)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
