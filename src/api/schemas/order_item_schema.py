#from uuid import UUID

#from pydantic import BaseModel, Field


#class _BaseOrderItem(BaseModel):
#    quantity: int = Field(description="The quantity of the product", gt=0)


#class OrderItemIn(_BaseOrderItem):
#    """Schema for creating a new order product."""

#    product_id: UUID = Field(description="The product id")
    


#class OrderItemOut(_BaseOrderItem):
#    """Schema for returning an order product."""

#    product_name: str
#    product_id: int
#    quantity: int
#    unit_price: float
#    cookTime: int
#    product_uuid: UUID


#__all__ = [
#    "OrderItemIn",
#    "OrderItemOut",
#]
