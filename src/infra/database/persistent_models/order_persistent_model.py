from typing import List

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import Column, Integer, String # ,Enum as SaEnum, Float, ForeignKey

from src.core.domain.entities import Order as OrderEntity
from src.core.domain.value_objects import OrderStatus

from .order_item_persistent_model import OrderItemPersistentModel
from .persistent_model import PersistentModel


class OrderPersistentModel(PersistentModel):
    """SQLAlchemy model for persisting Order entities."""

    __tablename__ = "orders"

#    id = Column(Integer, primary_key=True)
    customer: Mapped[str] = Column(String, nullable=False)
    order_items: Mapped[List["OrderItemPersistentModel"]] = relationship(
        "OrderItemPersistentModel", back_populates="order", 
        cascade="all, delete-orphan"
    )

    total_value: Mapped[float] #= Column(Float, nullable=False)
    status: Mapped[OrderStatus] #= Column(SaEnum, nullable=False)

    def to_entity(self) -> OrderEntity:
        """Converts the persistent model to an Order entity."""
        return OrderEntity(
            _id=self.id,
            _items=[item.to_entity() for item in self.order_items],
            _total_value=self.total_value,
            _status=self.status,
            customer=self.customer,
            uuid=self.uuid,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(entity: OrderEntity) -> "OrderPersistentModel":
        """Converts an Order entity to the persistent model."""
        return OrderPersistentModel(
            customer=entity.customer,
            items=[OrderItemPersistentModel.from_entity(item, entity.id) for item in entity.items],
            total_value=entity.total_value,
            status=entity.status,
            uuid=entity.uuid,
            id=entity.id,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


__all__ = ["OrderPersistentModel"]
