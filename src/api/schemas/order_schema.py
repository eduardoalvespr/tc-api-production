
from datetime import datetime
from typing import List
from uuid import UUID
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field

from src.core.uses_cases.order import CheckinItem, CheckinOrder

from .order_item_schema import OrderItemOut



class OrderIn(BaseModel):
    """Schema for creating a new order."""

    customer_name: str = Field(description="The customer name")
    items: List[OrderItemOut] = Field(description="List of products in the order")

    model_config = ConfigDict(str_strip_whitespace=True)

    def to_checkin_request(self) -> CheckinOrder:
        """Converts the OrderIn instance to a CheckoutRequest instance."""
        return CheckinOrder(
            customer_name=self.customer_name,
            items=[
                CheckinItem(
                    product_id=item.product_id, 
                    product_name=item.product_name, 
                    product_uuid=item.product_uuid,
                    quantity=item.quantity, 
                    cookTime=item.cookTime
                    )
                for item in self.items
            ],
        )


class OrderCreationOut(BaseModel):
    """Schema for returning the result of creating an order."""

    number: UUID = Field(description="The order number")
    id: int = Field(description="The id indicates the position number in the queue")


class OrderOut(BaseModel):
    """Schema for returning an order."""

    number: UUID = Field(description="The order external uuid")
    id: int = Field(description="The position number in the queue")
    customer: UUID = Field(description="The customer uuid")
    items: List[OrderItemOut] = Field(description="List of items in the order")
    status: Enum = Field(description="The order status")
    created_at: datetime = Field(description="The order creation date")
    updated_at: datetime = Field(description="The order last update date")
    total_value: float = Field(description="The total value of the order")

    model_config = ConfigDict(str_strip_whitespace=True, arbitrary_types_allowed=True)


class OrderStatusEnum(str, Enum):
    """Schema for updating the status of an order."""
    RECEBIDO = "recebido"
    EM_PREPARACAO = "em_preparacao"
    PRONTO = "pronto"
    FINALIZADO = "finalizado"

#class OrderStatusEnum(BaseModel):
#    """Represents the incoming data for a order status update"""
#    order_status: Literal["recebido","em_preparacao","pronto","finalizado"]

__all__ = [
    "OrderCreationOut",
    "OrderIn",
    "OrderOut",
    "OrderStatusEnum",
    #"OrderStatusEnum",
]




