from api.routers import api_v1


@api_v1.get("/test", tags=["DevTools"])
def test():
    """
    Test if the server is active.

    :return: A test message.
    """
    return {"detail": "Success!"}
