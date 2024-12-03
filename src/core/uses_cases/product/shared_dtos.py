from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from ...domain.value_objects import Category


@dataclass
class ProductResult:
    """Data structure for holding product data."""

    id: int
    uuid: UUID
    created_at: datetime
    updated_at: datetime
    name: str
    category: Category
    price: float
    description: str
    images: list[str]
    cooktime: int


__all__ = ["ProductResult"]
