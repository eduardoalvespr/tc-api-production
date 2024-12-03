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
        """Executes the use case to retrieve products by their IDs.

        Args:
        ids (Set[int]): A set of product IDs to retrieve.

        Returns:
        Iterable[ProductResult]: An iterable containing the resulting products.
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
                cooktime=product.cooktime,
            )
            for product in products
        ]


__all__ = ["GetProductsByIdsUseCase"]
