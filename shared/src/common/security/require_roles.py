from fastapi import Depends, HTTPException, status
from ..user_identity.user_schema import CurrentUser
from ..user_identity.user import get_current_user


def require_roles(*allowed_roles: str):
    def dependency(user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
        if not any(role in user.roles for role in allowed_roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tenés permisos para realizar esta acción",
            )

        return user

    return dependency