from uuid import UUID

from ....domain.exceptions.order_not_found_error import OrderNotFoundError
from ....domain.repositories.order_repository import OrderRepository
from ..shared_dtos import OrderResult


class GetOrderByUUIDUseCase:
    """ListOrdersUseCase encapsulates the business logic for retrieving orders."""

    def __init__(self, repository: OrderRepository) -> None:
        """Initializes a new instance of the ListOrdersUseCase class.

        Args:
            repository (OrderRepository): The repository instance for order persistence operations.
        """
        self.repository = repository

    def get_order(self, order_uuid: UUID) -> OrderResult:
        """Retrieves all orders.

        Returns:
            An iterable of all orders.
        """
        order = self.repository.get_by_uuid(order_uuid)

        if not order:
            raise OrderNotFoundError(order_uuid)

        return OrderResult(
            id=order.id,
            uuid=order.uuid,
            status=order.status,
            created_at=order.created_at,
            updated_at=order.updated_at,
            order_uuid=order_uuid,
        )


__all__ = ["GetOrderByUUIDUseCase"]
