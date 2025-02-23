from typing import Protocol
from .i_resolve_dependency_strategy import ResolveDependencyStrategy


class ResolveDependencyStrategyUpdater(Protocol):
    def __call__(self, old_strategy: ResolveDependencyStrategy) -> ResolveDependencyStrategy:
        ...
