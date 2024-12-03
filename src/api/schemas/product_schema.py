from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from src.core.domain.entities.product import Product
from src.core.domain.value_objects import Category
from src.core.uses_cases.product import ProductCreation, ProductUpdate


class _BaseProduct(BaseModel):
    name: str = Field(description="The product name", min_length=1, max_length=100)
    category: Category = Field(description="The product category")
    price: float = Field(description="The product price", gt=0)
    description: str = Field(description="The product description", max_length=255, min_length=10)
    images: List[str] = Field(
        description="List of image URLs for the product", min_length=1, max_length=50
    )
    cooktime: int = Field(description="Time to get ready", gt=0)


class ProductCreationIn(_BaseProduct):
    """Schema for creating a new product."""

    model_config = ConfigDict(str_strip_whitespace=True)

    def to_product_creation_dto(self) -> ProductCreation:
        """Converts the schema to a ProductCreation instance."""
        return ProductCreation(
            name=self.name,
            category=self.category,
            price=self.price,
            description=self.description,
            images=self.images,
            cooktime=self.cooktime,
        )


class ProductUpdateIn(_BaseProduct):
    """Schema for updating an existing product."""

    model_config = ConfigDict(str_strip_whitespace=True)

    def to_product_update_dto(self) -> ProductUpdate:
        """Converts the schema to a ProductCreation instance."""
        return ProductUpdate(
            name=self.name,
            category=self.category,
            price=self.price,
            description=self.description,
            images=self.images,
            cooktime=self.cooktime,
        )


class ProductOut(ProductCreationIn):
    """Schema for returning a product."""

    id: int = Field(description="The product ID")
    uuid: UUID = Field(description="The product external uuid")
    created_at: datetime = Field(description="The product creation date")
    updated_at: datetime = Field(description="The product last update date")

    @staticmethod
    def from_entity(entity: Product) -> "ProductOut":
        """Creates a ProductOut instance from a Product entity."""
        if isinstance(entity.uuid, UUID):
            try:
                entity.uuid = UUID(str(entity.uuid))
            except ValueError:
                raise ValueError(f"The UUID provided '{entity.uuid}' is not valid")  # noqa: TRY003, TRY004, B904
        elif not isinstance(entity.uuid, UUID):
            raise ValueError(f"The UUID provided '{entity.uuid}' is not valid")  # noqa: TRY003, TRY004, B904

        return ProductOut(
            id=entity._id,
            uuid=entity.uuid,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            name=entity.name,
            category=entity.category,
            price=entity.price,
            description=entity.description,
            images=entity.images,
            cooktime=entity.cooktime,
        )


class ProductCategoryEnum(str, Enum):
    """Represents the incoming data for a Product Category."""
    LANCHE = "lanche"
    ACOMPANHAMENTO = "acompanhamento"
    BEBIDA = "bebida"
    SOBREMESA = "sobremesa"


class ProductCategoryIn(BaseModel):
    """Represents the incoming data for a Product Category."""

    category: ProductCategoryEnum


__all__ = [
    "ProductCategoryEnum",
    "ProductCategoryIn",
    "ProductCreationIn",
    "ProductOut",
    "ProductUpdateIn",
]
