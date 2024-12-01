from dataclasses import dataclass
from enum import Enum


@dataclass
class CheckinOrder:
    """CheckoutOrderRequest encapsulates all necessary data for performing a checkout."""

    order_uuid: str
    status: Enum


__all__ = ["CheckinOrder"] 
