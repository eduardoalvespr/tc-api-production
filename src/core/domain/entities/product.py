from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID

from ..base import AggregateRoot, AssertionConcern
from ..value_objects import Category



@dataclass(kw_only=True)
#class Product(AggregateRoot):
class Product():
    """Represents a product in the system.

    Attributes:
    name: The product's name.
    category: The product's category.
    price: The product's price.
    description: The product's description.
    images: The product's images.
    """
    _id: Optional[int] | None = field(default=None)#
    uuid: Optional[UUID] | None = field(default=None)#
    created_at: Optional[datetime] | None = field(default=None)#
    updated_at: Optional[datetime] | None = field(default=None)#
    name: str
    category: Category
    price: float
    description: str
    images: list[str]
    cookTime: int

    def validate(self) -> None:
        """Validates the product's attributes.

        This method checks if the product's name,
        category, price, and description are not null or empty.
        If any of these conditions are not met, a DomainError will be raised with a relevant
         message.

        Raises:
            DomainError: If any of the product's attributes are null or empty.
        """
        AssertionConcern.assert_argument_not_null(self.name, "Name is required")
        AssertionConcern.assert_argument_not_empty(self.name, "Name is required")
        AssertionConcern.assert_argument_not_null(self.category, "Category is required")
        AssertionConcern.assert_argument_not_null(self.price, "Price is required")
        AssertionConcern.assert_argument_not_null(self.description, "Description is required")
        AssertionConcern.assert_argument_not_empty(self.description, "Description is required")
        AssertionConcern.assert_argument_not_null(self.images, "Images are required")
        AssertionConcern.assert_argument_not_empty(self.images, "Images are required")
        AssertionConcern.assert_argument_greater_than_zero(
            self.price, "Price must be greater than zero"
        )

    @property
    def id(self) -> int | None:
        """The aggregate root's ID."""
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value


__all__ = ["Product"]
