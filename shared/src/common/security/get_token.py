from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from common.security.jwt import Jwt

security = HTTPBearer()


def get_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Jwt:
    return Jwt(access_token=credentials.credentials)