from typing import List
from uuid import UUID

from sqlalchemy import update, func
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from src.core.domain.repositories.order_repository import OrderRepository
from src.core.domain.entities.order import Order #
from src.core.domain.value_objects import OrderStatus #

from ..persistent_models import OrderPersistentModel

class SQLAlchemyOrderRepository(OrderRepository):
    """Implementation of the OrderRepository using SQLAlchemy.

    This repository uses an SQLAlchemy session to perform CRUD operations on orders.
    """
    #from src.core.domain.entities.order import Order
    #from src.core.domain.value_objects.order_status import OrderStatus
    def __init__(self, session: Session) -> None:
        """Initializes the SQLAlchemyOrderRepository with a given session.

        Args:
            session (Session): The SQLAlchemy session to use for database operations.
        """
        self._session = session

    def create(self, order: Order) -> Order:
        """Creates a new order in the repository.

        Args:
            order (Order): The order to be created.

        Returns:
            Order: The created order with its uuid and other persistence details populated.
        """
        #from ..persistent_models import OrderPersistentModel
        db_order = OrderPersistentModel.from_entity(order)
        self._session.add(db_order)
        self._session.commit()

        return db_order.to_entity()

    def update_status(self, order_uuid: UUID, status: OrderStatus) -> Order:
        """Updates the status of an existing order in the repository.

        Args:
            order_uuid (UUID): The uuid of the order to be updated.
            status (OrderStatus): The new status for the order.

        Returns:
            Order: The updated order.
        """
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(order_uuid)
        print(status)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        #from ..persistent_models import OrderPersistentModel
        with self._session as session:
            session.execute(
                update(OrderPersistentModel)
                .where(OrderPersistentModel.order_uuid == order_uuid)
                .values(status=status)
            )
            session.commit()
            updated_order = session.execute(
                select(OrderPersistentModel).where(OrderPersistentModel.order_uuid == order_uuid)
            ).scalar_one()
            print("#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#")
            print(updated_order)
            print("updated - order - to entity - UPDATE!!")
            print(updated_order.to_entity)
            return updated_order.to_entity()

    def list_all(self) -> List[Order]:
        """Retrieves all orders from the repository.

        Returns:
            List[Order]: A list of all orders.
        """
        
        from ..persistent_models import OrderPersistentModel
        with self._session as session:
            result = session.execute(select(OrderPersistentModel))
            return [row.to_entity() for row in result.scalars().all()]

    def get_by_uuid(self, order_uuid: UUID) -> Order | None:
        """Retrieves an order by its uuid."""
        print("$$$$$$$$$$$$$$$$$$ORDER-REPOSITORY-IMPL1$$$$$$$$$$$$$$$$$$")
        #from ..persistent_models import OrderPersistentModel
        order = (
            self._session.query(OrderPersistentModel)
            .filter(OrderPersistentModel.order_uuid == order_uuid)
            .first()
        )
        print(order)
        if order is None:
            return None
        print("$$$$$$$$$$$$$$$$$$ORDER-REPOSITORY-IMPL1- order$$$$$$$$$$$$$$$$$$")
        print(order)
        #print("$$$$$$$$$$$$$$$$$$ORDER-REPOSITORY-IMPL1 - from.entity$$$$$$$$$$$$$$$$$$")
        #print(order.from_entity())
        print("$$$$$$$$$$$$$$$$$$ORDER-REPOSITORY-IMPL1 - to.entity$$$$$$$$$$$$$$$$$$")
        print(order.to_entity())
        print("$$$$$$$$$$$$$$$$$$ORDER-REPOSITORY-IMPL- out$$$$$$$$$$$$$$$$$$")
        return order
    
    def get_last_by_status(self, status: OrderStatus) -> Order | None:
        """Retrieves a order by its status and the last id."""
        
        #from ..persistent_models import OrderPersistentModel
        max_id = (
            self._session.query(func.max(OrderPersistentModel.id))
            .filter(OrderPersistentModel.status == status)
            .scalar()
        )

        if max_id is None:
            return None

        order = (
            self._session.query(OrderPersistentModel)
            .filter(OrderPersistentModel.id == max_id)
            .first()
        )

        if order is None:
            return None

        return order.to_entity()
    
    def list_all_by_status(self, status: OrderStatus) -> List[Order]:
        """Retrieves all orders from the repository with a specific status.

        Returns:
            List[Order]: A list of all orders with a specific status.
        """
        
        #from ..persistent_models import OrderPersistentModel
        with self._session as session:
            result = session.query(OrderPersistentModel).filter(OrderPersistentModel.status == status)
            return [row.to_entity() for row in result.scalars().all()]
