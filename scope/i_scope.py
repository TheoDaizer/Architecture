from typing import NewType, Callable


Scope = NewType('Scope', dict[str, Callable])
