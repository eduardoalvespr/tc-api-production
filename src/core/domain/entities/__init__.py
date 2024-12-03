"""Contains the main entities of the domain model.

Entities are unique objects identified not by their attributes, but by their continuity and
distinct identity.
They form the core of the domain model, encapsulating both behavior and data.
"""

from .order import Order
from .product import Product

__all__ = ["Order", "Product"]
