from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from threading import Thread
from app.main import start_recognition
from app.predictions import latest_prediction
from fastapi.responses import StreamingResponse
from fastapi.responses import Response
import app.sharedframe as shared_frame
from fastapi.staticfiles import StaticFiles

app = FastAPI()
recognition_started = False

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/start")
def start():

    global recognition_started

    if not recognition_started:

        thread = Thread(
            target=start_recognition,
            daemon=True
        )

        thread.start()
        recognition_started = True

    return {"status": "started"}

@app.post("/stop")
def stop():

    global recognition_started

    shared_frame.running = False
    recognition_started = False

    return {"status": "stopped"}
    
@app.get("/predictions")
def prediction():
    return latest_prediction
def generate_frames():

    while True:

        if shared_frame.latest_frame is None:
            continue

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            shared_frame.latest_frame +
            b'\r\n'
        )

@app.get("/video_feed")
def video_feed():
    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )


app.mount(
    "/",
    StaticFiles(
        directory="frontend/dist",
        html=True
    ),
    name="frontend"
)