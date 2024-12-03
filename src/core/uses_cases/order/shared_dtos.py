from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from ...domain.value_objects import OrderStatus


@dataclass
class OrderResult:
    """OrderDetails represents the details of an order."""

    id: int
    uuid: UUID
    created_at: datetime
    updated_at: datetime
    order_uuid: UUID
    status: OrderStatus


__all__ = ["OrderResult"]
