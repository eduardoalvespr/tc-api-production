from dataclasses import dataclass
from typing import List
#from uuid import UUID

from ....domain.value_objects import Category


@dataclass
class ProductUpdate:
    """Data structure for holding product creation data."""

    name: str
    category: Category
    price: float
    description: str
    images: List[str]
    cookTime: int


__all__ = ["ProductUpdate"]
