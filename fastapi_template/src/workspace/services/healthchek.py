from ..models.healthcheck import HealthCheck
from fastapi import HTTPException
from fastapi import status


class HealthcheckService:
    def __init__(self):
        pass

    async def check(self, s=None):
        if s:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
            )
        else:
            return {"description": "OK"}
