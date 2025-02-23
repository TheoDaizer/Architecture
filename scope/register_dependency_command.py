from threading import Lock
from typing import Callable
from ioc.ioc_container import IoC



class RegisterDependencyCommand:
    _lock = Lock()

    def __init__(self, dependency_to_register: str, dependency_resolve_strategy: Callable):
        self.dependency_to_register = dependency_to_register
        self.resolve_strategy = dependency_resolve_strategy

    def execute(self):
        with self._lock:
            current_scope = IoC.resolve('IoC.Scope.Current')
            current_scope[self.dependency_to_register] = self.resolve_strategy
