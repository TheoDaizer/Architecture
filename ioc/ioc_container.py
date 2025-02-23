from typing import Any

from .i_resolve_dependency_strategy import ResolveDependencyStrategy
from .i_resolve_dependency_strategy_updater import ResolveDependencyStrategyUpdater
from .errors import ResolveDependencyError


def default_ioc_strategy(dependency: str, **kwargs) -> Any:
    if dependency == 'Set IoC Resolve Dependency Strategy':
        strategy_updater: ResolveDependencyStrategyUpdater = kwargs['strategy_updater']
        return UpdateResolveDependencyStrategyCommand(strategy_updater)
    else:
        raise ResolveDependencyError(f'Unknown dependency "{dependency}"')


class IoC:

    strategy: ResolveDependencyStrategy = default_ioc_strategy

    @staticmethod
    def resolve(dependency: str, **kwargs) -> Any:
        return IoC.strategy(dependency, **kwargs)


class UpdateResolveDependencyStrategyCommand:
    def __init__(self, updater: ResolveDependencyStrategyUpdater):
        self.updater = updater

    def execute(self):
        IoC.strategy = self.updater(IoC.strategy)
