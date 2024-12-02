
from uuid import UUID
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field 

from src.core.uses_cases.order import  CheckinOrder 
from src.core.domain.value_objects import OrderStatus




class OrderStatusEnum(str, Enum):
    """Schema for updating the status of an order."""
    RECEBIDO = "recebido"
    EM_PREPARACAO = "em_preparacao"
    PRONTO = "pronto"
    FINALIZADO = "finalizado"

class OrderStatusIn(BaseModel):
    status: OrderStatusEnum

class OrderIn(BaseModel):
    """Schema for creating a new order."""
    model_config = ConfigDict(str_strip_whitespace=True)
    order_uuid: UUID = Field(description="The Order UUID.")
    status: OrderStatus = Field(description="The Order status")
    

    def to_checkin_request(self) -> CheckinOrder:
        """Converts the OrderIn instance to a CheckoutRequest instance."""
        return CheckinOrder(
            order_uuid=self.order_uuid,
            status=self.status,
        )


class OrderCreationOut(BaseModel):
    """Schema for returning the result of creating an order."""
    order_uuid: UUID = Field(description="The order UUID")
    status: OrderStatus = Field(description="The Order status")
    id: int = Field(description="The id indicates the position number in the queue")

class OrderOut(BaseModel):
    """Schema for returning an order."""
    order_uuid: UUID = Field(description="The order UUID")
    status: OrderStatus = Field(description="The Order status")
    id: int = Field(description="The id indicates the position number in the queue")
    model_config = ConfigDict(str_strip_whitespace=True) #, arbitrary_types_allowed=True

__all__ = [
    "OrderCreationOut",
    "OrderIn",
    "OrderOut",
    "OrderStatusEnum",
    "OrderStatusIn"
]
