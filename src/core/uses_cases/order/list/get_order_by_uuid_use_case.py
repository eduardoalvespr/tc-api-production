#from typing import Iterable
from uuid import UUID

from ....domain.repositories.order_repository import OrderRepository
from ..shared_dtos import  OrderResult


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
    
        print("$$$$$$$$$$$$$$$$$$CHECKIN-USE-CASE1s$$$$$$$$$$$$$$$$$$")
        print(order_uuid)
        print("Order_UUID - use-case")
        order = self.repository.get_by_uuid(order_uuid)
        return OrderResult(
            uuid=order.uuid,
            status=order.status,
            id=order.id,
            created_at=order.created_at,
            updated_at=order.updated_at,
            order_uuid=order.order_uuid,
            ) 


__all__ = ["GetOrderByUUIDUseCase"]
