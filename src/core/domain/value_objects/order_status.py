from enum import StrEnum
from typing import Dict, Iterable


class OrderStatus(StrEnum):
    """An Enum that represents an Order Status."""

    RECEBIDO = "recebido"
    EM_PREPARACAO = "em_preparacao"
    PRONTO = "pronto"
    FINALIZADO = "finalizado"

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
