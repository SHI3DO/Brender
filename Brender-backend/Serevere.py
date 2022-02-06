from fastapi import FastAPI


from modules.Utils import Utilities
from api.routers import api_v1

app = FastAPI(title="Brender Server", description="No Desc", version="Alpha")
app.include_router(api_v1)


@app.get("/", tags=["Root"])
async def root():
    return {"detail": "Brender API root"}


Serevere = Utilities()
Serevere.load()
Serevere.cors(app)

# For Dev

if __name__ == "__main__":
    import uvicorn
    import socket
    import os

    main_file = os.path.basename(__file__).removesuffix(".py")

    if socket.gethostname() == "DESKTOP-NI0SO2S":
        uvicorn.run(f"{main_file}:app", host="192.168.0.2", port=8585, reload=True)
    else:
        uvicorn.run(f"{main_file}:app", host="192.168.0.11", port=8586, reload=False)
