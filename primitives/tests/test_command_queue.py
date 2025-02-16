import pytest
from unittest.mock import Mock
from primitives.command_queue import CommandQueue


def test_empty_command_queue():
    queue = CommandQueue()

    with pytest.raises(IndexError):
        queue.get()


def test_command_queue():
    mock_command_1 = Mock()
    mock_command_2 = Mock()

    queue = CommandQueue()

    queue.put(mock_command_1)
    queue.put(mock_command_2)

    assert len(queue) == 2

    assert queue.get() is mock_command_1
    assert queue.get() is mock_command_2
    with pytest.raises(IndexError):
        queue.get()

    assert len(queue) == 0


def test_command_queue_head():
    mock_command = Mock()

    queue = CommandQueue()
    queue.put(mock_command)

    assert queue.head() is mock_command
    assert queue.get() is mock_command

    with pytest.raises(IndexError):
        queue.head()
