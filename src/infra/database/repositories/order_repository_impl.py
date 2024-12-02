from typing import List
from uuid import UUID

from sqlalchemy import func, update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from src.core.domain.entities.order import Order  #
from src.core.domain.repositories.order_repository import OrderRepository
from src.core.domain.value_objects import OrderStatus  #

from ..persistent_models import OrderPersistentModel


class SQLAlchemyOrderRepository(OrderRepository):
    """Implementation of the OrderRepository using SQLAlchemy.

    This repository uses an SQLAlchemy session to perform CRUD operations on orders.
    """

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
        with self._session as session:
            session.execute(
                update(OrderPersistentModel)
                .where(OrderPersistentModel.order_uuid == str(order_uuid))
                .values(status=status)
            )
            session.commit()
            updated_order = session.execute(
                select(OrderPersistentModel).where(
                    OrderPersistentModel.order_uuid == str(order_uuid)
                )
            ).scalar_one()
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
        order = (
            self._session.query(OrderPersistentModel)
            .filter(OrderPersistentModel.order_uuid == str(order_uuid))
            .first()
        )
        print(order)
        if order is None:
            return None
        return order.to_entity()

    def get_last_by_status(self, status: OrderStatus) -> Order | None:
        """Retrieves a order by its status and the last id."""
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
        with self._session as session:
            result = session.query(OrderPersistentModel).filter(
                OrderPersistentModel.status == status
            )
            return [row.to_entity() for row in result.scalars().all()]
