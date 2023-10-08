"""A ZenML pipeline consists of tasks that execute in order and yield artifacts.

The artifacts are automatically stored within the artifact store and metadata 
is tracked by ZenML. Each individual task within a pipeline is known as a
step. The standard pipelines within ZenML are designed to have easy interfaces
to add pre-decided steps, with the order also pre-decided. Other sorts of
pipelines can be created as well from scratch, building on the `BasePipeline` class.

Pipelines can be written as simple functions. They are created by using decorators appropriate to the specific use case you have. The moment it is `run`, a pipeline is compiled and passed directly to the orchestrator.
"""


from zenml.config import DockerSettings
from zenml.config.schedule import Schedule
from zenml.pipelines.base_pipeline import BasePipeline
from zenml.pipelines.pipeline_decorator import pipeline

__all__ = ["BasePipeline", "DockerSettings", "pipeline", "Schedule"]
