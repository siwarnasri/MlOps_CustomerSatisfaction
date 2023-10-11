"""Step output class."""

from typing import Any, Iterator, NamedTuple, Tuple, Type


class Output(object):
    """A named tuple with a default name that cannot be overridden."""

    def __init__(self, **kwargs: Type[Any]):
        """Initializes the output.

        Args:
            **kwargs: The output values.
        """
        self.outputs = NamedTuple("ZenOutput", **kwargs)  # type: ignore[misc]

    def items(self) -> Iterator[Tuple[str, Type[Any]]]:
        """Yields a tuple of type (output_name, output_type).

        Yields:
            A tuple of type (output_name, output_type).
        """
        yield from self.outputs.__annotations__.items()
