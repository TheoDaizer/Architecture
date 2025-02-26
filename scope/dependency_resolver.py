from typing import Any

from .i_scope import Scope
from .errors import RootScopeHasNoParentError

from ioc.errors import ResolveDependencyError


class DependencyResolver:
    def __init__(self, scope: Scope):
        self.scope = scope

    def resolve(self, dependency: str, **kwargs) -> Any:
        scope_to_look_up = self.scope
        while (resolve_strategy := scope_to_look_up.get(dependency)) is None:
            try:
                scope_to_look_up = scope_to_look_up['IoC.Scope.Current.Parent'](**kwargs)
            except RootScopeHasNoParentError:
                raise ResolveDependencyError(f'Unknown dependency "{dependency}"')

        return resolve_strategy(**kwargs)
