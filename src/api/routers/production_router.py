from http import HTTPStatus
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends

from ..controllers.order_controller import OrderController
from ..dependencies import injector
from ..schemas.order_schema import (
    OrderIn,
    OrderOut,
    OrderStatusEnum,
)

router = APIRouter(tags=["production"], prefix="/production")


@router.post("/checkin", response_model=OrderOut, status_code=HTTPStatus.CREATED)
def checkin(
    order_in: OrderIn,
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> OrderOut:
    """Process a fake checkout by adding selected products to the order queue."""
    return controller.checkin(order_in)

@router.put("/{order_uuid}/status", response_model=OrderOut)
def update_order_status(
    order_uuid: UUID,
    status_update: OrderStatusEnum,
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> OrderOut:
    """Update the status of an existing order."""
    return controller.update_status(order_uuid, status_update)


@router.get("/order/{order_uuid}", response_model=List[OrderOut])
def get_order(
    order_uuid: UUID,
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> OrderOut:
    """Return an order."""
    print("$$$$$$$$$$$$$$$$$$ROUTER$$$$$$$$$$$$$$$$$$")
    return controller.get_order(order_uuid)

