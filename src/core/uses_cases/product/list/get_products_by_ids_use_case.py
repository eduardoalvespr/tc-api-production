from typing import Iterable, Set

from ....domain.repositories import ProductRepository
from ..shared_dtos import ProductResult


class GetProductsByIdsUseCase:
    """A use case for retrieving products by Ids."""

    def __init__(self, product_repository: ProductRepository) -> None:
        """Initializes the use case with a product repository.

        Args:
            product_repository (ProductRepository): The repository for accessing product data.
        """
        self._product_repository = product_repository

    def execute(self, ids: Set[int]) -> Iterable[ProductResult]:
        """Initializes the use case with a product repository.

        Args:
            product_repository (ProductRepository): The repository for accessing product data.
        """
        products = self._product_repository.get_by_ids(ids)
        return [
            ProductResult(
                id=product.id,
                uuid=product.uuid,
                created_at=product.created_at,
                updated_at=product.updated_at,
                name=product.name,
                category=product.category,
                price=product.price,
                description=product.description,
                images=product.images,
                cookTime=product.cookTime,  
            )
            for product in products
        ]
        

__all__ = ["GetProductsByIdsUseCase"]
