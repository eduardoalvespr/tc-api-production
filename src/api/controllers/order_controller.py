from typing import Iterable
from uuid import UUID


from src.core.uses_cases.order import (
    CheckinUseCase,
    ListOrdersUseCase,
    UpdateOrderStatusUseCase,
    OrderResult
)

from ..presenters import Presenter
from ..schemas.order_schema import (
    OrderCreationOut,
    OrderIn,
    OrderOut,
    OrderStatusEnum,
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
        update_order_status_use_case: UpdateOrderStatusUseCase,
        order_created_presenter: Presenter[OrderCreationOut, OrderResult],
        order_details_presenter: Presenter[OrderOut, OrderResult],#REVISAR NECESSIDADE
    ) -> None:
        self._checkin_use_case = checkin_use_case
        self._list_orders_use_case = list_orders_use_case
        self._update_order_status_use_case = update_order_status_use_case
        self._order_created_presenter = order_created_presenter
        self._order_details_presenter = order_details_presenter#REVISAR NECESSIDADE

    def checkin(self, order_in: OrderIn) -> OrderOut:
        """Registers a new order in the system from the provided order data"""
        order = self._checkin_use_case.checkin(order_in.to_checkin_request())
        
        return self._order_created_presenter.present(order)

    def list_orders(self) -> Iterable[OrderOut]:
        """Get a list of orders in the system"""
        print("$$$$$$$$$$$$$$$$$$CONTROLLER1$$$$$$$$$$$$$$$$$$")
        orders = self._list_orders_use_case.list_orders()
        print("$$$$$$$$$$$$$$$$$$CONTROLLER2$$$$$$$$$$$$$$$$$$")
        return self._order_details_presenter.present_many(orders)

    def update_status(self, order_uuid: UUID, status_update: OrderStatusEnum) -> OrderOut:
        """Update the status of an order in the system from the provided order ID and status"""
        order = self._update_order_status_use_case.update_status(order_uuid, status_update)
        return self._order_details_presenter.present(order)
    
    def addToQueue(self, order_uuid: UUID) -> OrderIn:
        """Register a new order to the queue from order_uuid provided"""
        order = self._checkin_use_case.checkin(order_uuid)
        return self._order_details_presenter.present(order)


__all__ = ["OrderController"]
