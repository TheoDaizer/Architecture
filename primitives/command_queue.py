from collections import deque
from actions.command_interface import Command


class CommandQueue:
    def __init__(self):
        self._deque = deque()

    def put(self, value: Command):
        self._deque.append(value)

    def get(self) -> Command:
        return self._deque.popleft()

    def head(self) -> Command:
        return self._deque[0]

    def __len__(self) -> int:
        return len(self._deque)
