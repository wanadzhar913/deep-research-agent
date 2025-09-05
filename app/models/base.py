"""Base models and common imports for all models."""
from zoneinfo import ZoneInfo
from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    """Base model with common fields."""

    created_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Asia/Kuala_Lumpur")))
