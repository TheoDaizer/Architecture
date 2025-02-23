import pytest
from unittest.mock import Mock

from ..ioc_container import IoC, default_ioc_strategy
from ..errors import ResolveDependencyError


@pytest.fixture(scope="function")
def test_set_ioc_resolve_dependency_strategy():
    mock_strategy = Mock()
    mock_strategy_updater = Mock(return_value=mock_strategy)
    IoC.resolve('Set IoC Resolve Dependency Strategy', strategy_updater=mock_strategy_updater).execute()

    mock_strategy_updater.assert_called_once_with(default_ioc_strategy)
    assert IoC.strategy is mock_strategy


def test_unknown_dependency():
    with pytest.raises(ResolveDependencyError):
        IoC.resolve('UnknownDependency')
