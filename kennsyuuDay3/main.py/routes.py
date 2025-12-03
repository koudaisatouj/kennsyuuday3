from __future__ import annotations

from typing import List

from fastapi import APIRouter, HTTPException, status

from models import Task, TaskCreate, TaskUpdate
from store import TaskStore


def create_task_router(store: TaskStore) -> APIRouter:
    router = APIRouter(prefix="/tasks", tags=["Tasks"])

    @router.get("", response_model=List[Task])
    def list_tasks() -> List[Task]:
        return store.list()

    @router.get("/{task_id}", response_model=Task)
    def get_task(task_id: int) -> Task:
        task = store.get(task_id)
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
            )
        return task

    @router.post("", response_model=Task, status_code=status.HTTP_201_CREATED)
    def create_task(payload: TaskCreate) -> Task:
        return store.create(payload)

    @router.put("/{task_id}", response_model=Task)
    def update_task(task_id: int, payload: TaskUpdate) -> Task:
        updated = store.update(task_id, payload)
        if updated is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
            )
        return updated

    @router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_task(task_id: int) -> None:
        deleted = store.delete(task_id)
        if deleted is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
            )

    return router
