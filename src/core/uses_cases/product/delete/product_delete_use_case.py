from uuid import UUID

from ....domain.exceptions import ProductNotFoundError
from ....domain.repositories import ProductRepository


class ProductDeleteUseCase:
    """A use case for deleting a product within the system."""

    def __init__(self, product_repository: ProductRepository) -> None:
        """Initializes the use case with a specific product repository.

        Parameters:
            product_repository: An instance of ProductRepository used for product data interactions.
        """
        self._product_repository = product_repository

    def execute(self, product_uuid: UUID) -> None:
        """Executes the product deletion use case.

        Parameters:
            product_uuid (UUID): The UUID of the product to delete.
        """
        print("$$$$$$$$$$$DELETE-USE-CASE1$$$$$$$$$$$")
        if not self._product_repository.get_by_uuid(product_uuid):
            raise ProductNotFoundError(search_param=str(product_uuid))
        print("$$$$$$$$$$$DELETE-USE-CASE2$$$$$$$$$$$")
        self._product_repository.delete(product_uuid)


__all__ = ["ProductDeleteUseCase"]
