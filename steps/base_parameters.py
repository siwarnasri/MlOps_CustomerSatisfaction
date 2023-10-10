"""Step parameters."""

from pydantic import BaseModel


class BaseParameters(BaseModel):
    """Base class to pass parameters into a step."""
