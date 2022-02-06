import hashlib
import re
from datetime import datetime

# import jwt
import starlette.status
from fastapi import Request
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

from api.mongo import database
from api.routers import api_v1

UserDB = database["Users"]


class User(BaseModel):
    username: str
    password: str


def hash_password(password):
    """
    Hashes a password. Three rounds of SHA512 are used.

    :param password: The password to hash.
    :return: The hashed password.
    """
    once = hashlib.sha512(password.encode("utf-8")).hexdigest()
    twice = hashlib.sha512(once.encode("utf-8")).hexdigest()

    return hashlib.sha512(twice.encode("utf-8")).hexdigest()


def raise_forbidden(detail):
    """
    Returns a forbidden exception with the given detail.

    :param detail: The detail of the exception.
    """
    return HTTPException(status_code=starlette.status.HTTP_403_FORBIDDEN, detail=detail)


@api_v1.post("/register", tags=["User"])
def register(user: User, request: Request):
    """
    Register a new user.

    :param user: User object
    """

    FORBIDDEN_USERNAME = ["root", "admin"]

    # Validate username
    if user.username in FORBIDDEN_USERNAME:
        raise raise_forbidden("Forbidden Username")

    elif not re.match(r"^[a-zA-Z0-9_]{5,32}$", user.username):
        raise raise_forbidden("Not allowed Characters Included / Too Short / Too Long")

    # Evaluate User
    if UserDB.find_one({"username": user.username}):
        raise raise_forbidden("Username Already Exists")
    else:
        if UserDB.find_one({"ip": request.client.host}):
            raise raise_forbidden("Client Already Registered")
        else:
            UserDB.insert_one(
                {
                    "username": user.username,
                    "password": hash_password(user.password),
                    "ip": request.client.host,
                    "creation": datetime.now(),
                }
            )
            return {"detail": "User Registered"}


@api_v1.post("/login", tags=["User"])
def login(user: User, request: Request):
    """
    Login a user and return a token.

    :param user: User object
    """

    if UserDB.find_one({"username": user.username}):
        if UserDB.find_one({"username": user.username}).get(
            "password"
        ) == hash_password(user.password):
            UserDB.find_one_and_update(
                {"username": user.username},
                {
                    "$set": {
                        "last_login": datetime.now(),
                        "last_ip": request.client.host,
                    }
                },
            )

            payload_data = {
                "username": user.username,
                "ip": request.client.host,
            }

            return {"detail": "Logged In"}

        else:
            raise raise_forbidden("Incorrect Password")
    else:
        raise raise_forbidden("User Not Found")
