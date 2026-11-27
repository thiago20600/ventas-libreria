import jwt
from fastapi import HTTPException


class Jwt:
    def __init__(self, access_token: str):
        self.claims = jwt.decode(
            access_token,
            options={
                "verify_signature": False,
                "verify_exp": False,
            },
        )

    def validate_audience(self, ms_name: str) -> None:
        aud = self.claims.get("aud", [])
        if isinstance(aud, str):
            aud = [aud]
        if ms_name not in aud:
            raise HTTPException(403, "Token no válido para este servicio")

    def get_user_id(self) -> str:
        return self.claims["sub"]

    def get_email(self) -> str | None:
        return self.claims.get("email")

    def get_username(self) -> str | None:
        return self.claims.get("preferred_username")

    def get_user_roles(self) -> list[str]:
        return self.claims.get("realm_access", {}).get("roles", [])