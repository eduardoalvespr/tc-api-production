from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, status, Query

#from src.core.domain.value_objects import Category

from ..controllers import ProductController
from ..dependencies import injector
from ..schemas.product_schema import ProductCreationIn, ProductOut, ProductUpdateIn, ProductCategoryIn

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

@router.get("/products", response_model=List[ProductOut])
async def get_products_by_uuids(
    uuids: List[UUID] = Query(..., description="List of product UUIDs"),
    controller: ProductController = Depends(lambda: injector.get(ProductController))
):
    """
    Get a list of products by their UUIDs.
    """  
    print('###############################CHEGUEI AQUI####PRODUCT ROUTER######')
    print(uuids)
    return controller.get_products_by_uuids(set(uuids))


__all__ = ["router"]
