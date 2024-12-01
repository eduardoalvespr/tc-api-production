#from sqlalchemy import Column, Float, ForeignKey, Integer
#from sqlalchemy.orm import relationship

#from src.core.domain.entities.order_item import OrderItem

#from ..repositories.dtos import OrderItemDTO
#from .persistent_model import PersistentModel


#class OrderItemPersistentModel(PersistentModel):
#    """SQLAlchemy model for persisting OrderItem entities."""

#    __tablename__ = "order_items"

#    id = Column(Integer, primary_key=True)
#    order_id = Column(ForeignKey("orders.id"), nullable=False)
#    product_uuid = Column(ForeignKey("products.uuid"), nullable=False)
    
#    order = relationship("OrderPersistentModel", back_populates="order_items")
#    product = relationship("ProductPersistentModel", lazy="joined")
#    quantity = Column(Integer, nullable=False)
#    unit_price = Column(Float, nullable=False)
#    cookTime = Column(Integer, nullable=True)
    

#    def to_entity(self) -> OrderItem:
#        """Converts the persistent model to an OrderItem entity."""
#        return OrderItem(
#            id=self.id,
#            uuid=self.uuid,
#            product=self.product,
#            quantity=self.quantity,
#            unit_price=self.unit_price,
#            created_at=self.created_at,
#            updated_at=self.updated_at,
#        )

#    @staticmethod
#    def from_entity(entity: OrderItem, order_id: int) -> "OrderItemPersistentModel":
#        """Converts an OrderItem entity to the persistent model."""
#        return OrderItemPersistentModel(
#            id=entity.id,
#            order_id=order_id,
#            uuid=entity.uuid,
#            created_at=entity.created_at,
#            updated_at=entity.updated_at,
#            product_id=entity.id,
#            product_uuid=entity.uuid,
#            quantity=entity.quantity,
#            unit_price=entity.unit_price,
#            cookTime=entity.cookTime,
#        )


#__all__ = ["OrderItemPersistentModel"]
