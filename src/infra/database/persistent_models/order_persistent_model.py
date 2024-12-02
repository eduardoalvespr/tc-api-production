from typing import List

from sqlalchemy.orm import Mapped 

from src.core.domain.entities import Order as OrderEntity
from src.core.domain.value_objects import OrderStatus

from .persistent_model import PersistentModel


class OrderPersistentModel(PersistentModel):
    """SQLAlchemy model for persisting Order entities."""

    __tablename__ = "orders"

    order_uuid: Mapped[str]
    status: Mapped[OrderStatus]

    def to_entity(self) -> OrderEntity:
        """Converts the persistent model to an Order entity."""
        return OrderEntity(
            order_uuid=self.order_uuid,
            _status=self.status,
            _id=self.id,
            uuid=self.uuid,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(entity: OrderEntity) -> "OrderPersistentModel":
        """Converts an Order entity to the persistent model."""
        return OrderPersistentModel(
            order_uuid=entity.order_uuid,
            status=entity.status,
            id=entity.id,
            uuid=entity.uuid,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


__all__ = ["OrderPersistentModel"]
