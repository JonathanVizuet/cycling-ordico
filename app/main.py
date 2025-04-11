from fastapi import FastAPI, HTTPException, Request
from app.state import cyclist_state

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API de Ordico Cycling esta funcionando"}

@app.post("/events")
async def register_event_request(event: Request):
    data = await event.json()
    cyclist_id = data["cyclist_id"]
    cyclist_state[cyclist_id] = {
        "event": data["event"],
        "location": data.get("location"),
        "time": data["time"]
    }
    return {"message": "Event registered"}

@app.get("/cyclists/{cyclist_id}/status")
def get_list_status(cyclist_id: str):
    if cyclist_id not in cyclist_state:
        raise HTTPException(status_code=404, detail="Not Found")

    return cyclist_state[cyclist_id]