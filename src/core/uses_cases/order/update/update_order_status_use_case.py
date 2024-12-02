from uuid import UUID

from ....domain.exceptions import OrderNotFoundError
from ....domain.repositories.order_repository import OrderRepository
from ....domain.value_objects.order_status import OrderStatus
from ..shared_dtos import  OrderResult #OrderItemResult,


class UpdateOrderStatusUseCase:
    """UpdateOrderStatusUseCase encapsulates the business logic for updating order status."""

    def __init__(self, repository: OrderRepository) -> None:
        """Initializes a new instance of the UpdateOrderStatusUseCase class.

        Args:
            repository (OrderRepository): The repository instance for order persistence operations.
        """
        self.repository = repository

    def update_status(self, order_uuid: UUID, status: OrderStatus) -> OrderResult:
        """Updates the status of an existing order.

        Args:
            order_uuid: The uuid of the order to be updated.
            status: The new status for the order.

        Returns:
            Order: The updated order.
        """
        print("###################################################")
        print(order_uuid)
        print(status)
        order = self.repository.get_by_uuid(order_uuid)
        print(order)
        print("##################################################")

        if not order:
            raise OrderNotFoundError(order_uuid)

        order.status = status
        order = self.repository.update_status(order_uuid, status)
        return OrderResult(
                id=order.id,
                uuid=order.uuid,
                status=order.status,
                created_at=order.created_at,
                updated_at=order.updated_at,
                order_uuid=order_uuid,
            )


__all__ = ["UpdateOrderStatusUseCase"]
