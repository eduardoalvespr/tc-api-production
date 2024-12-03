from typing import Iterable

from ....domain.repositories.order_repository import OrderRepository
from ..shared_dtos import OrderResult


class ListOrdersUseCase:
    """ListOrdersUseCase encapsulates the business logic for retrieving orders."""

    def __init__(self, repository: OrderRepository) -> None:
        """Initializes a new instance of the ListOrdersUseCase class.

        Args:
            repository (OrderRepository): The repository instance for order persistence operations.
        """
        self.repository = repository

    def list_orders(self) -> Iterable[OrderResult]:
        """Retrieves all orders.

        Returns:
            An iterable of all orders.
        """
        orders = self.repository.list_all()
        return [
            OrderResult(
                uuid=order.uuid,
                status=order.status,
                id=order.id,
                created_at=order.created_at,
                updated_at=order.updated_at,
                order_uuid=order.order_uuid,
            )
            for order in orders
        ]


__all__ = ["ListOrdersUseCase"]
