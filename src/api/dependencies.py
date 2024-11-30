from fastapi import Depends
from injector import Injector, Module, provider, singleton
from sqlalchemy.orm import Session

from src.core.domain.repositories import OrderRepository, ProductRepository
from src.core.uses_cases import (
    CheckinUseCase, 
    GetProductsByCategoryUseCase, 
    GetProductsByUUIdsUseCase,
    GetProductsByIdsUseCase,
    ListOrdersUseCase, 
    UpdateOrderStatusUseCase,
    ProductCreationUseCase,
    ProductDeleteUseCase,
    ProductUpdateUseCase,
    )

from src.infra.database.repositories import SQLAlchemyOrderRepository, SQLAlchemyProductRepository
from src.infra.database.config.database import get_db_session

from .controllers import OrderController, ProductController
from .presenters import (
    OrderCreatedPresenter,
    OrderDetailsPresenter,
    ProductDetailsPresenter,
    Presenter,
)
from .schemas import OrderCreationOut, OrderOut , ProductOut


class AppModule(Module):
    """AppModule is a class that provides the dependencies for the application.

    It uses the provider decorator from the injector package to specify how to provide each
     dependency.
    """
    @singleton
    @provider
    def provide_session(self) -> Session:
        """Provides an SQLAlchemy session."""
        return next(get_db_session())    
    
    @singleton
    @provider
    def provide_product_repository(
        self,
        session: Session ) -> ProductRepository:
        """Provides a ProductRepository instance."""
        return SQLAlchemyProductRepository(session)

    @singleton
    @provider
    def provide_order_repository(self, session: Session) -> OrderRepository:
        """Provides an OrderRepository instance."""
        return SQLAlchemyOrderRepository(session)

    @provider
    def provide_product_creation_use_case(self, product_repository: ProductRepository) -> ProductCreationUseCase:
        """Provides a ProductCreationUseCase instance."""
        return ProductCreationUseCase(product_repository)

    @provider
    def provide_product_update_use_case(self, product_repository: ProductRepository) -> ProductUpdateUseCase:
        """Provides a ProductUpdateUseCase instance."""
        return ProductUpdateUseCase(product_repository)

    @provider
    def provide_product_delete_use_case(self, product_repository: ProductRepository) -> ProductDeleteUseCase:
        """Provides a ProductDeleteUseCase instance."""
        return ProductDeleteUseCase(product_repository)

    @provider
    def provide_get_products_by_category_use_case(self, product_repository: ProductRepository) -> GetProductsByCategoryUseCase:
        """Provides a GetProductsByCategoryUseCase instance."""
        return GetProductsByCategoryUseCase(product_repository)
    
    @provider
    def provide_get_products_by_uuids(self, product_repository: ProductRepository) -> GetProductsByUUIdsUseCase:
        """Provides a GetProductsByCategoryUseCase instance."""
        return GetProductsByUUIdsUseCase(product_repository)
    
    @provider
    def provide_get_products_by_ids(self, product_repository: ProductRepository) -> GetProductsByIdsUseCase:
        """Provides a GetProductsByCategoryUseCase instance."""
        return GetProductsByIdsUseCase(product_repository)

    @provider
    def provide_checkin_use_case(
        self, order_repository: OrderRepository, product_repository: ProductRepository
    ) -> CheckinUseCase:
        """Provides a CheckinUseCase instance."""
        return CheckinUseCase(order_repository, product_repository)
    
    @provider
    def provide_list_orders_use_case(self, order_repository: OrderRepository) -> ListOrdersUseCase:
        """Provides a ListOrdersUseCase instance."""
        return ListOrdersUseCase(order_repository)

    @provider
    def provide_update_order_status_use_case(self, order_repository: OrderRepository) -> UpdateOrderStatusUseCase:
        """Provides an UpdateOrderStatusUseCase instance."""
        return UpdateOrderStatusUseCase(order_repository)

    @provider
    def provide_product_details_presenter(self) -> Presenter[ProductOut, ProductOut]:
        """Provides a ProductDetailsPresenter instance."""
        return ProductDetailsPresenter()
    
    @provider
    def provide_order_created_presenter(self) -> Presenter[OrderCreationOut, OrderOut]:
        """Provides an OrderCreatedPresenter instance."""
        return OrderCreatedPresenter()

    @provider
    def provide_order_details_presenter(self) -> Presenter[OrderOut, OrderOut]:
        """Provides an OrderDetailsPresenter instance."""
        return OrderDetailsPresenter()

    @provider
    def provide_product_controller(
        self,
        product_creation_use_case: ProductCreationUseCase,
        product_update_use_case: ProductUpdateUseCase,
        product_delete_use_case: ProductDeleteUseCase,
        get_products_by_category_use_case: GetProductsByCategoryUseCase,
        get_products_by_uuids_use_case: GetProductsByUUIdsUseCase,
        get_products_by_ids_use_case: GetProductsByIdsUseCase,
        product_details_presenter: Presenter[ProductOut, ProductOut],
    ) -> ProductController:
        """Provides a ProductController instance."""
        return ProductController(
            product_creation_use_case,
            product_update_use_case,
            product_delete_use_case,
            get_products_by_category_use_case,
            get_products_by_uuids_use_case,
            get_products_by_ids_use_case,
            product_details_presenter,
        )

    @provider
    def provide_order_controller(
        self,
        checkout_use_case: CheckinUseCase,
        list_orders_use_case: ListOrdersUseCase,
        update_order_status_use_case: UpdateOrderStatusUseCase,
        order_created_presenter: Presenter[OrderCreationOut, OrderOut],
        order_details_presenter: Presenter[OrderOut, OrderOut],
    ) -> OrderController:
        """Provides an OrderController instance."""
        return OrderController(
            checkout_use_case,
            list_orders_use_case,
            update_order_status_use_case,
            order_created_presenter,
            order_details_presenter,
        )

injector = Injector([AppModule()])

def injector_dependency(cls):
    def dependency(injector: Injector = Depends(lambda: injector)):
        return injector.get(cls)
    return dependency

__all__ = ["injector"]
