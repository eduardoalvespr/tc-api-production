from enum import Enum
from typing import List


class Category(Enum):
    """An Enum that represents a Product Category."""

    LANCHE = "lanche"
    ACOMPANHAMENTO = "acompanhamento"
    BEBIDA = "bebida"
    SOBREMESA = "sobremesa"

    @classmethod
    def values(cls) -> List["Category"]:
        """Return a list of Category values."""
        return [cls[member] for member in cls.__members__]


__all__ = ["Category"]
