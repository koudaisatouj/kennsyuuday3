from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    completed: bool = False


class TaskCreate(TaskBase):
    """Payload used when a client creates a brand-new task."""


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    completed: Optional[bool] = None


class Task(TaskBase):
    id: int
