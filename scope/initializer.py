from typing import Optional
from threading import local

from .i_scope import Scope
from .dependency_resolver import DependencyResolver
from .errors import RootScopeHasNoParentError
from .register_dependency_command import RegisterDependencyCommand
from ioc.ioc_container import IoC
from ioc.i_resolve_dependency_strategy import ResolveDependencyStrategy


class LocalStorage(local):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data: Optional[Scope] = None


class Initializer:

    current_scope = LocalStorage()
    root_scope: Scope = {}
    _already_initialized = False

    @classmethod
    def execute(cls):
        if cls._already_initialized:
            return

        cls.root_scope['IoC.Scope.Current'] = \
            lambda **kwargs: cls.current_scope.data if cls.current_scope.data is not None else cls.root_scope

        cls.root_scope['IoC.Scope.Current.Set'] = lambda **kwargs: SetCurrentScopeCommand(**kwargs)

        cls.root_scope['IoC.Scope.Current.Parent'] = lambda **kwargs: raiser(RootScopeHasNoParentError())

        cls.root_scope['IoC.Scope.Current.Clear'] = lambda **kwargs: ClearScopeCommand()

        cls.root_scope['IoC.Scope.Create.Empty'] = lambda **kwargs: dict()

        cls.root_scope['IoC.Scope.Create'] = lambda **kwargs: create_scope(**kwargs)

        cls.root_scope['IoC.Register'] = lambda **kwargs: RegisterDependencyCommand(**kwargs)

        IoC.resolve(
            dependency='Set IoC Resolve Dependency Strategy',
            strategy_updater=default_resolve_dependency_strategy_updater
        ).execute()

        cls._already_initialized = True


def raiser(error: Exception):
    raise error


def create_scope(parent_scope: Optional[Scope] = None):
    if parent_scope is None:
        parent_scope = IoC.resolve('IoC.Scope.Current')
    new_scope = IoC.resolve('IoC.Scope.Create.Empty')
    new_scope['IoC.Scope.Current.Parent'] = lambda **kwargs: parent_scope
    return new_scope


def default_resolve_dependency_strategy_updater(old_strategy: ResolveDependencyStrategy) -> ResolveDependencyStrategy:
    def resolve_dependency_strategy(dependency: str, **kwargs):
        scope = Initializer.current_scope.data if Initializer.current_scope.data else Initializer.root_scope
        return DependencyResolver(scope).resolve(dependency, **kwargs)
    return resolve_dependency_strategy


class SetCurrentScopeCommand:
    def __init__(self, scope: Scope):
        self.scope = scope

    def execute(self):
        Initializer.current_scope.data = self.scope


class ClearScopeCommand:
    def execute(self):
        Initializer.current_scope.data = None
