from enum import Enum #StrEnum #, auto
from typing import List


class Category(Enum):
    """An Enum that represents a Product Category."""

    LANCHE = "lanche" # auto()
    ACOMPANHAMENTO = "acompanhamento" # auto()
    BEBIDA = "bebida" # auto()
    SOBREMESA = "sobremesa" # auto()

    @classmethod
    def values(cls) -> List["Category"]:
        """Return a list of Category values."""
        return [cls[member] for member in cls.__members__]


__all__ = ["Category"]
