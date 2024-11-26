from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from ...domain.value_objects import Category


@dataclass
class ProductResult:
    """Data structure for holding product data."""

    name: str
    category: Category
    price: float
    description: str
    images: list[str]
    cookTime: int
    uuid: UUID
    id: int
    created_at: datetime
    updated_at: datetime


__all__ = ["ProductResult"]
