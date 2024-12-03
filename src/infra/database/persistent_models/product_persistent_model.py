from typing import List

from sqlalchemy import ARRAY, Column, Float, Integer, String
from sqlalchemy import Enum as SaEnum
from sqlalchemy.orm import Mapped

from src.core.domain.entities import Product as ProductEntity
from src.core.domain.value_objects import Category

from .persistent_model import PersistentModel


class ProductPersistentModel(PersistentModel):
    """Represents a product in the system."""

    __tablename__ = "products"

    name: Mapped[str] = Column(String(100), nullable=False, unique=True)
    category: Mapped[Category] = Column(SaEnum(Category), nullable=False)
    price: Mapped[float] = Column(Float, nullable=False)
    description: Mapped[str] = Column(String(255), nullable=False)
    images: Mapped[List[str]] = Column(ARRAY(String), nullable=False)
    cooktime: Mapped[int] = Column(Integer, nullable=True)

    def to_entity(self) -> ProductEntity:
        """Converts the persistent model to a domain entity."""
        return ProductEntity(
            _id=self.id,
            uuid=self.uuid,
            created_at=self.created_at,
            updated_at=self.updated_at,
            name=self.name,
            category=self.category,
            price=self.price,
            description=self.description,
            images=self.images,
            cooktime=self.cooktime,
        )


__all__ = ["ProductPersistentModel"]
