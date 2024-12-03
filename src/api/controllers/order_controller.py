from typing import Iterable
from uuid import UUID

from src.core.uses_cases.order import (
    CheckinUseCase,
    GetOrderByUUIDUseCase,
    ListOrdersUseCase,
    OrderResult,
    UpdateOrderStatusUseCase,
)

from ..presenters import Presenter
from ..schemas.order_schema import (
    OrderCreationOut,
    OrderIn,
    OrderOut,
    OrderStatusIn,
)


class OrderController:
    """This class manages order-related actions using different use cases.

    The class acts as the intersection between the API and the business logic,
    handling HTTP requests related to order data.
    """

    def __init__(
        self,
        checkin_use_case: CheckinUseCase,
        list_orders_use_case: ListOrdersUseCase,
        get_order_by_uuid_use_case: GetOrderByUUIDUseCase,
        update_order_status_use_case: UpdateOrderStatusUseCase,
        order_created_presenter: Presenter[OrderCreationOut, OrderResult],
        order_details_presenter: Presenter[OrderOut, OrderResult],
    ) -> None:
        self._checkin_use_case = checkin_use_case
        self._list_orders_use_case = list_orders_use_case
        self._get_order_by_uuid_use_case = get_order_by_uuid_use_case
        self._update_order_status_use_case = update_order_status_use_case
        self._order_created_presenter = order_created_presenter
        self._order_details_presenter = order_details_presenter

    def checkin(self, order_in: OrderIn) -> OrderOut:
        """Registers a new order in the system from the provided order data."""
        order = self._checkin_use_case.checkin(order_in.to_checkin_request())

        return self._order_created_presenter.present(order)

    def get_order(self, order_uuid: UUID) -> OrderOut:
        """Get a Order by UUID."""
        order = self._get_order_by_uuid_use_case.get_order(order_uuid)
        return self._order_created_presenter.present(order)

    def list_orders(self) -> Iterable[OrderOut]:
        """Get a list of orders in the system."""
        orders = self._list_orders_use_case.list_orders()
        return self._order_details_presenter.present_many(orders)

    def update_status(self, order_uuid: UUID, status_update: OrderStatusIn) -> OrderOut:
        """Update the status of an order in the system from the provided order ID and status."""
        order = self._update_order_status_use_case.update_status(order_uuid, status_update)
        return self._order_details_presenter.present(order)


__all__ = ["OrderController"]
