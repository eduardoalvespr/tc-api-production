from dataclasses import dataclass
from typing import Iterable
from uuid import UUID


@dataclass
class CheckinItem:
    """CheckoutItem represents the data for an item in a checkout."""

    product_uuid: UUID
    product_id: int
    product_name: str
    quantity: int
    cookTime: int


@dataclass
class CheckinOrder:
    """CheckoutOrderRequest encapsulates all necessary data for performing a checkout."""

    customer_name: str
    items: Iterable[CheckinItem]


__all__ = ["CheckinItem", "CheckinOrder"]
