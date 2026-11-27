from fastapi import Depends

from ..security.get_token import get_jwt
from common.security.jwt import Jwt
from .user_schema import CurrentUser


def get_current_user(jwt: Jwt = Depends(get_jwt)) -> CurrentUser:
    return CurrentUser(
        id=jwt.get_user_id(),
        email=jwt.get_email(),
        username=jwt.get_username(),
        roles=jwt.get_user_roles(),
    )