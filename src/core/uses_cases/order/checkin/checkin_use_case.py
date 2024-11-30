from typing import Iterable
from uuid import UUID

from ....domain.exceptions import (
    EmptyOrderError,
    OrderCreationFailedDueToMissingProductsError,
)


from ....domain.repositories import (
    OrderRepository,
    ProductRepository,
)

from ..shared_dtos import CustomerSummaryResult, OrderItemResult, OrderResult
from .checkin_dto import CheckinItem, CheckinOrder

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
        self._validate_items(request.items)
        
        customer = request.customer_name
        #produtos = request.items.
#        print('###############################CHEGUEI AQUI########################')
#        print(request.items) - ta chegando o objeto certinho
        product_map = self._get_products(request.items)
        
        items = self._create_order_items(request.items, product_map)

        order = Order(_customer=customer, _items=list(items))
        created_order = self._order_repository.create(order)

        
        return OrderResult(
            uuid=created_order.uuid,
            status=created_order.status,
            total_value=created_order.total_value,
            created_at=created_order.created_at,
            updated_at=created_order.updated_at,
            customer=CustomerSummaryResult(
                name=created_order.customer,
                #email=str(created_order.customer.email),
                #cpf=str(created_order.customer.cpf),
            ),
            items=[
                OrderItemResult(
                    product_name=item.product.name,
                    quantity=item.quantity,
                    unit_price=item.unit_price,
                )
                for item in created_order.items
            ],
        )
    
#    def checkin

    @staticmethod
    def _validate_items(items: Iterable[CheckinItem]) -> None:
        if not items:
            raise EmptyOrderError()

    def _get_products(self, items: Iterable[CheckinItem]) -> dict[id, Product]:
        """Gets the products for the order items.

        Args:
            items: The order items containing the product identifiers.

        Returns:
            A dictionary containing the product UUIDs as keys and the products as values.

        Raises:
            OrderCreationFailedDueToMissingProductsError: If any product is not found.
        """
        #uuids = {item.product_uuid for item in items}
        product_ids = {item.product_id for item in items}
#        print('###############################CHEGUEI AQUI########################')
#        print(product_ids) - TUDO CERTO ATÉ AQUI!!
        products = self._product_repository.get_by_uuids(product_ids)
        product_map = {product.id: product for product in products}
        missing_products = product_ids - product_map.keys()

        if missing_products:
            raise OrderCreationFailedDueToMissingProductsError(missing_products)

        return product_map

    from ....domain.entities import OrderItem
    @staticmethod
    def _create_order_items(
        items: Iterable[CheckinItem], product_map: dict[UUID, Product]
    ) -> Iterable[OrderItem]:
        from ....domain.entities import OrderItem
        return [
            OrderItem(
                product=product_map[item.product_id],
                unit_price=product_map[item.product_id].price,
                quantity=item.quantity,
            )
            for item in items
        ]


__all__ = ["CheckinUseCase"]
