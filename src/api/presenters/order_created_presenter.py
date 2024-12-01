from src.core.uses_cases.order import OrderResult

from ..schemas import OrderCreationOut
from .presenter import Presenter


class OrderCreatedPresenter(Presenter[OrderCreationOut, OrderResult]):
    """Presenter for the OrderCreated use case."""

    def present(self, data: OrderResult) -> OrderCreationOut:
        """Converts the OrderResult instance into an OrderCreationOut instance."""
        return OrderCreationOut(
            order_uuid=data.uuid,
            status=data.status,
            id=data.id,
            )


__all__ = ["OrderCreatedPresenter"]
