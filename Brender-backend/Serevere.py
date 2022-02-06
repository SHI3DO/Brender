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
