from __future__ import annotations

from typing import Dict, List, Optional

from models import Task, TaskCreate, TaskUpdate


class TaskStore:
    """Minimal in-memory persistence so the API feels realistic."""

    def __init__(self) -> None:
        self._items: Dict[int, Task] = {}
        self._next_id: int = 1

    def list(self) -> List[Task]:
        return list(self._items.values())

    def get(self, item_id: int) -> Optional[Task]:
        return self._items.get(item_id)

    def create(self, payload: TaskCreate) -> Task:
        task = Task(id=self._next_id, **payload.model_dump())
        self._items[task.id] = task
        self._next_id += 1
        return task

    def update(self, item_id: int, payload: TaskUpdate) -> Optional[Task]:
        current = self._items.get(item_id)
        if current is None:
            return None

        updated_data = payload.model_dump(exclude_unset=True)
        updated_task = current.model_copy(update=updated_data)
        self._items[item_id] = updated_task
        return updated_task

    def delete(self, item_id: int) -> Optional[Task]:
        return self._items.pop(item_id, None)

    def seed_demo_data(self) -> None:
        self.create(TaskCreate(title="Set up FastAPI server", completed=True))
        self.create(
            TaskCreate(title="Connect React app to API", description="Use fetch/axios")
        )
