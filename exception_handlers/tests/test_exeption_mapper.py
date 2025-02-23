from unittest.mock import Mock
from exception_handlers.exception_mapper import ExceptionMapper


def test_exception_mapper():
    mock_error = Exception()
    mock_command = Mock()
    mock_handler = Mock()

    exception_mapper = ExceptionMapper()
    exception_mapper.register_handler(type(mock_command), type(mock_error), mock_handler)

    handler = exception_mapper.get_handler(mock_command, mock_error)

    assert handler is mock_handler

def test_exception_mapper_unknown_command():
    mock_error = Exception()
    mock_init_command = Mock()
    mock_command = Mock()
    mock_handler = Mock()

    exception_mapper = ExceptionMapper()
    exception_mapper.register_handler(type(mock_init_command), type(mock_error), mock_handler)

    handler = exception_mapper.get_handler(mock_command, mock_error)

    assert handler is None

def test_exception_mapper_unknown_error():
    mock_init_error = Exception()
    mock_error = ValueError()
    mock_command = Mock()
    mock_handler = Mock()

    exception_mapper = ExceptionMapper()
    exception_mapper.register_handler(type(mock_command), type(mock_init_error), mock_handler)

    handler = exception_mapper.get_handler(mock_command, mock_error)

    assert handler is None
