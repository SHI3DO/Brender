import starlette.status
from fastapi.exceptions import HTTPException

from api.routers import api_v1


@api_v1.get("/blender", tags=["File Hosting"])
def blender(type: str = "windows"):
    """
    Returns a download link of the blender.

    :param type: User's operating system.
    :return: A download link of the blender.
    """
    if type == "windows":
        return {
            "url": "http://asphodel.kro.kr:1351/Hosting/blender-3.0.1-windows-x64.zip"
        }
    elif type == "linux":
        return {
            "url": "http://asphodel.kro.kr:1351/Hosting/blender-3.0.1-linux-x64.tar.xz"
        }
    else:
        raise HTTPException(
            status_code=starlette.status.HTTP_404_NOT_FOUND, detail="Not Found"
        )
