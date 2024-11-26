from enum import StrEnum, auto
from typing import Dict, Iterable


class OrderStatus(StrEnum):
    """An Enum that represents an Order Status."""

    RECEBIDO = auto()
    EM_PREPARACAO = auto()
    PRONTO = auto()
    FINALIZADO = auto()

    @classmethod
    def values(cls) -> Iterable["OrderStatus"]:
        """Return a list of OrderStatus values."""
        return [cls[member] for member in cls.__members__]

    def get_allowed_transitions(self) -> Iterable["OrderStatus"]:
        """Returns the allowed transitions for the given status."""
        _transitions: Dict["OrderStatus", Iterable["OrderStatus"]] = {
            OrderStatus.RECEBIDO: [OrderStatus.EM_PREPARACAO],
            OrderStatus.EM_PREPARACAO: [OrderStatus.PRONTO],
            OrderStatus.PRONTO: [OrderStatus.FINALIZADO],
        }

        return _transitions.get(self, [])


__all__ = ["OrderStatus"]
