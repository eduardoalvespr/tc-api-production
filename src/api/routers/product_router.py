from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from ..controllers import ProductController
from ..dependencies import injector
from ..schemas.product_schema import (
    ProductCreationIn,
    ProductOut,
    ProductUpdateIn,
)

router = APIRouter(tags=["Product"])


@router.post("/products", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreationIn,
    controller: ProductController = Depends(lambda: injector.get(ProductController)),  # noqa: B008
) -> ProductOut:
    return controller.create_product(product)


@router.put("/products/{product_uuid}", response_model=ProductOut)
def update_product(
    product_uuid: UUID,
    product: ProductUpdateIn,
    controller: ProductController = Depends(lambda: injector.get(ProductController)),  # noqa: B008
) -> ProductOut:
    return controller.update_product(product_uuid, product)


@router.delete("/products/{product_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_uuid: UUID,
    controller: ProductController = Depends(lambda: injector.get(ProductController)),  # noqa: B008
) -> None:
    controller.delete_product(product_uuid)


@router.get("/products/category/{category}", response_model=List[ProductOut])
def get_products_by_category(
    category: str,
    controller: ProductController = Depends(lambda: injector.get(ProductController)),  # noqa: B008
) -> List[ProductOut]:
    return controller.get_products_by_category(category)


@router.get("/products/by-uuids", response_model=List[ProductOut])  # noqa: B008
async def get_products_by_uuids(  # noqa: RUF029
    uuids: List[UUID] = Query(..., description="List of product UUIDs"),  # noqa: B008
    controller: ProductController = Depends(lambda: injector.get(ProductController)),  # noqa: B008
) -> List[ProductOut]:
    """Get a list of products by their UUIDs."""
    return controller.get_products_by_uuids(set(uuids))


@router.get("/products/by-ids", response_model=List[ProductOut])  # noqa: B008
async def get_products_by_ids(  # noqa: RUF029
    ids: List[int] = Query(..., description="List of product IDs"),  # noqa: B008
    controller: ProductController = Depends(lambda: injector.get(ProductController)),  # noqa: B008
) -> List[ProductOut]:
    """Get a list of products by their IDs."""
    return controller.get_products_by_ids(set(ids))


__all__ = ["router"]
