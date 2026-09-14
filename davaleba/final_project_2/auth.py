
from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

SECRET_KEY = "change-this-to-a-long-random-secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    password: str,
    hashed_password: str
) -> bool:
    return password_hash.verify(
        password,
        hashed_password
    )


def create_access_token(
    username: str,
    user_id: int
):
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": username,
        "user_id": user_id,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
# from datetime import datetime, timedelta, timezone
#
# import jwt
# from pwdlib import PasswordHash
#
# secret_key = 'zetian-the-empress'
# algorithm = 'HS256'
# access_token_expire_minutes = 30
#
# password_hash = PasswordHash.recommended()
#
# users_db={}
#
#
# def hash_password(password: str) ->str:
#     return password_hash.hash(password)
#
# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return password_hash.verify(plain_password, hashed_password)
#
# def create_access_token(username: str,user_id: str) -> str:
#     expire = datetime.now(timezone.utc) + timedelta(minutes=access_token_expire_minutes)
#
#     payload = {
#         'sub': username,
#         "user_id": user_id,
#         'exp': expire,
#     }
#
#     return jwt.encode(payload, secret_key, algorithm=algorithm)