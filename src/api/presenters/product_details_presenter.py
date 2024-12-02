from src.core.uses_cases.product import ProductResult

from ..schemas import ProductOut
from .presenter import Presenter


class ProductDetailsPresenter(Presenter[ProductOut, ProductResult]):
    """Presenter for the product details."""

    def present(self, data: ProductResult) -> ProductOut:
        """Converts the CustomerResult instance into a CustomerDetailsOut instance."""
        return ProductOut(
            id=data.id,
            uuid=data.uuid,
            created_at=data.created_at,
            updated_at=data.updated_at,
            name=data.name,
            category=data.category,
            price=data.price,
            description=data.description,
            images=data.images,
            cooktime=data.cooktime,
        )


__all__ = ["ProductDetailsPresenter"]
