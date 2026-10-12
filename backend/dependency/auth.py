from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from redis import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from redis_client import get_redis
from security import decode_access_token
from services.user_service import UserService


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_session),
    redis: Redis = Depends(get_redis),
):
    # 1. Проверяем JWT
    try:
        payload = decode_access_token(token)
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    # 2. Достаём user_id из payload
    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )

    # 3. JWT sub должен содержать числовой ID пользователя
    try:
        user_id_num = int(user_id)
    except (TypeError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user_id in token",
        )

    # 4. Получаем пользователя
    service = UserService(session, redis)
    user = await service.get_user_by_id(user_id_num)

    return user