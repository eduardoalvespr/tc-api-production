from http import HTTPStatus
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends

from ..controllers.order_controller import OrderController
from ..dependencies import injector
from ..schemas.order_schema import (
    OrderCreationOut,
    OrderIn,
    OrderOut,
    OrderStatusEnum,
)

router = APIRouter(tags=["production"], prefix="/production")


@router.post("/checkin", response_model=OrderCreationOut, status_code=HTTPStatus.CREATED)
def checkin(
    order_in: OrderIn,
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> OrderCreationOut:
    """Process a fake checkout by adding selected products to the order queue."""
    return controller.checkin(order_in)

#@router.post("/{order_uuid}", response_model=OrderCreationOut, status_code=HTTPStatus.CREATED)
#def addToQueue(
#    order_uuid: UUID,
#    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
#) -> OrderCreationOut:
#    """Process a fake checkout by adding selected products to the order queue."""
#    return controller.addToQueue(order_uuid)

@router.put("/{order_uuid}/status", response_model=OrderOut)
def update_order_status(
    order_uuid: UUID,
    status_update: OrderStatusEnum,
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> OrderOut:
    """Update the status of an existing order."""
    return controller.update_status(order_uuid, status_update)


@router.get("/", response_model=List[OrderOut])
def list_orders(
    controller: OrderController = Depends(lambda: injector.get(OrderController)),  # noqa: B008
) -> List[OrderOut]:
    """List all orders."""
    return controller.list_orders()


#@router.get("/production/{oder_uuid}")        get_by_uuid
#@router.get("/production/last?status=status") get_last_by_status
#@rouger.get("/production/{status}")           list_all_by_status
