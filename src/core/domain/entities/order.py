from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID

from ...domain.value_objects import OrderStatus
from ..base import AggregateRoot, AssertionConcern
from ..exceptions import InvalidStatusTransitionError


@dataclass(kw_only=True)
class Order(AggregateRoot):
    """Represents an order in the system."""

    _id: int | None = field(default=None)  #
    uuid: Optional[UUID] | None = field(default=None)  #
    created_at: Optional[datetime] | None = field(default=None)  #
    updated_at: Optional[datetime] | None = field(default=None)  #
    order_uuid: str
    _status: OrderStatus

    def __post_init__(self) -> None:
        self.validate()

    @property
    def status(self) -> OrderStatus:
        """Return self status attribute.

        This method return the status of the object

        Raises:
            DomainError: If any of the order's attributes are invalid.
        """
        return self._status

    @status.setter
    def status(self, new_status: OrderStatus) -> None:
        """Updates the status of the order.

        Args:
            new_status: The new status of the order.

        Raises:
            InvalidStatusTransitionError: If the new status is invalid.
        """
        if new_status not in self.status.get_allowed_transitions():
            raise InvalidStatusTransitionError(self.status, new_status)
        self._status = new_status

    def validate(self) -> None:
        """Validates the order's attributes.

        This method checks if the user_uuid, products, and status are valid.
        If any of these conditions are not met,
         a DomainError will be raised with a relevant message.

        Raises:
            DomainError: If any of the order's attributes are invalid.
        """
        AssertionConcern.assert_argument_not_null(self.order_uuid, "order_uuid is required")


__all__ = ["Order"]
