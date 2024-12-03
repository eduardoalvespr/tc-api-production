from src.core.uses_cases.order import OrderResult

from ..schemas import OrderOut
from .presenter import Presenter


class OrderDetailsPresenter(Presenter[OrderOut, OrderResult]):
    """Presenter for the OrderDetailsResult use case."""

    def present(self, data: OrderResult) -> OrderOut:
        """Converts the OrderDetailsResult instance into an OrderOut instance."""
        return OrderOut(
            id=data.id,
            uuid=data.uuid,
            created_at=data.created_at,
            updated_at=data.updated_at,
            order_uuid=data.order_uuid,
            status=data.status,
        )


__all__ = ["OrderDetailsPresenter"]
