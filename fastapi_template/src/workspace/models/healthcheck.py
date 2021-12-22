from pydantic import BaseModel
from typing import Optional


class HealthBase(BaseModel):
    description: str


class HealthCheck(HealthBase):
    class Config:
        orm_mode = True
