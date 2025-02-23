from typing import Any, Callable, NewType

ResolveDependencyStrategy = NewType('ResolveDependencyStrategy', Callable[[str, dict[str, Any]], Any])
