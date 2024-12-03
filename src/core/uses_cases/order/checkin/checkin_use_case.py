from ....domain.repositories import (
    OrderRepository,
    ProductRepository,
)
from ..shared_dtos import OrderResult
from .checkin_dto import CheckinOrder


class CheckinUseCase:
    """CheckoutUseCase encapsulates the business logic for creating orders."""

    from ....domain.entities import Product

    def __init__(
        self,
        order_repository: OrderRepository,
        product_repository: ProductRepository,
    ) -> None:
        """Initializes a new instance of the CheckoutUseCase class.

        Args:
            order_repository: The repository instance for order persistence operations.
            customer_repository: The repository instance for customer persistence operations.
            product_repository: The repository instance for product persistence operations.
            payment_use_case: The use case for processing payments.
        """
        self._order_repository = order_repository
        self._product_repository = product_repository

    def checkin(self, request: CheckinOrder) -> OrderResult:
        """Creates a new order in the system.

        Args:
            request: The checkout request data.

        Returns:
            CheckoutResponse: The response containing the order number.

        Raises:
            EmptyOrderError: If the order has no items.
            OrderCreationFailedDueToMissingProductsError: If any product is not found.
            CustomerNotFoundError: If the customer is not found.
        """
        from ....domain.entities import Order

        order = Order(order_uuid=request.order_uuid, _status=request.status)
        created_order = self._order_repository.create(order)

        return OrderResult(
            id=created_order.id,
            uuid=created_order.uuid,
            status=created_order.status,
            created_at=created_order.created_at,
            updated_at=created_order.updated_at,
            order_uuid=created_order.order_uuid,
        )


__all__ = ["CheckinUseCase"]
