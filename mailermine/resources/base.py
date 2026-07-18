"""Shared base class for all resource wrappers."""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

from mailermine.exceptions import ApiError, map_generated_error

T = TypeVar("T")


class BaseResource:
    """Base class that maps generated failures into public SDK exceptions."""

    def __init__(self, *, timeout: float) -> None:
        self._timeout = timeout

    def execute(self, operation: Callable[[], T]) -> T:
        """Run a generated API call and translate failures.

        Parameters
        ----------
        operation:
            Zero-argument callable that performs the generated request.

        Returns
        -------
        T
            The operation result.

        Raises
        ------
        ApiError
            Public SDK error corresponding to the failure.
        """
        try:
            return operation()
        except ApiError:
            raise
        except Exception as error:
            mapped = map_generated_error(error)
            raise mapped from None
