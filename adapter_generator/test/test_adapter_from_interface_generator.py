from typing import Protocol
from unittest.mock import Mock
import pytest

from test_cases.test_case_initialize_scope import InitializeScopeTestCase
from ..adapter_from_interface_generator import AdapterGenerator
from ..set_strategy_decorator import set_strategy



class TestAdapterGenerator(InitializeScopeTestCase):

    def test_adapter_from_interface_generator(self):
        class TestInterface(Protocol):
            def get_a(self):
                ...

            def get_b(self):
                ...

            def set_b(self, new_value):
                ...

        mock_data = {}
        mock_get_a = Mock()
        mock_get_b = Mock()
        mock_set_b = Mock()

        mock_data['a'] = mock_get_a
        mock_data['b'] = mock_get_b

        adapter_cls = AdapterGenerator(TestInterface).generate()
        adapter_obj: TestInterface = adapter_cls(mock_data)

        assert adapter_obj.get_a() is mock_get_a
        assert adapter_obj.get_b() is mock_get_b
        adapter_obj.set_b(mock_set_b)
        assert adapter_obj.get_b() is mock_set_b
        assert mock_data['b'] is mock_set_b

    def test_user_defined_strategies(self):
        class TestInterface(Protocol):
            def get_a(self) -> int:
                ...

            @set_strategy(strategy=lambda adapter: -7)
            def get_b(self) -> int:
                ...

            @set_strategy(strategy=lambda adapter, new_value: adapter.data_object.__setitem__('b', new_value * 2))
            def set_b(self, new_value: int) -> int:
                ...

            @set_strategy(strategy=lambda adapter: adapter.get_a() + adapter.get_b())
            def my_funk(self) -> int:
                ...

        mock_data = {'a': 11, 'b': -11}

        adapter_cls = AdapterGenerator(TestInterface).generate()
        adapter_obj: TestInterface = adapter_cls(mock_data)

        assert adapter_obj.get_b() == -7
        adapter_obj.set_b(45)
        assert mock_data['b'] == 90
        assert adapter_obj.my_funk() == 4

    def test_unique_method_without_strategy_raises_error(self):
        class TestInterface(Protocol):
            def my_unique_funk(self) -> int:
                ...

        adapter_cls = AdapterGenerator(TestInterface)
        with pytest.raises(AttributeError):
            adapter_cls.generate()
