
import os
import secrets

from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader


api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False,
)


def verify_api_key(api_key: str = Security(api_key_header)):
    expected_api_key = os.getenv("API_SENTINEL_API_KEY")

    if not expected_api_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API authentication is not configured",
        )

    if not api_key or not secrets.compare_digest(
        api_key, expected_api_key
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )

    return True
