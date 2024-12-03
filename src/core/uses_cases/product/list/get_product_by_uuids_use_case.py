from typing import Iterable, Set
from uuid import UUID

from ....domain.repositories import ProductRepository
from ..shared_dtos import ProductResult


class GetProductsByUUIdsUseCase:
    """A use case for retrieving products by Ids."""

    def __init__(self, product_repository: ProductRepository) -> None:
        """Initializes the use case with a product repository.

        Args:
            product_repository (ProductRepository): The repository for accessing product data.
        """
        self._product_repository = product_repository

    def execute(self, product_uuids: Set[UUID]) -> Iterable[ProductResult]:
        """Executes the use case to retrieve products by their UUIDs.

        Args:
            product_uuids (Set[UUID]): A set of product UUIDs to retrieve.

        Returns:
            Iterable[ProductResult]: An iterable containing the resulting products.
        """
        products = self._product_repository.get_by_uuids(product_uuids)

        return [
            ProductResult(
                id=product.id,
                uuid=product.uuid,
                name=product.name,
                category=product.category,
                price=product.price,
                description=product.description,
                images=product.images,
                cooktime=product.cooktime,
                created_at=product.created_at,
                updated_at=product.updated_at,
            )
            for product in products
        ]


__all__ = ["GetProductsByUUIdsUseCase"]
