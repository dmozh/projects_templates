from typing import (List, Optional)

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from fastapi import Request

from ..services.healthchek import HealthcheckService
from ..models.healthcheck import HealthCheck

from ..logger import log

router = APIRouter(
    # prefix="/"
)


@router.get('/healthcheck', response_model=HealthCheck)
async def get(
        service: HealthcheckService = Depends(),
):
    print('12345')
    return await service.check()