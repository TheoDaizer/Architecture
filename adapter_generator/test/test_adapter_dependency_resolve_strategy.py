from typing import Protocol
from test_cases.test_case_initialize_scope import InitializeScopeTestCase
from ioc.ioc_container import IoC
from ..adapter_dependency_resolve_strategy import adapter_dependency_resolve_strategy



class TestInitializer(InitializeScopeTestCase):

    def test_adapter_dependency_resolve_strategy(self):
        class TestInterface(Protocol):
            def get_a(self) -> int:
                ...

            def get_b(self) -> int:
                ...

            def set_b(self, new_value: int):
                ...

        mock_data = {'a': 5, 'b': 6}

        IoC.resolve(
            dependency='IoC.Register',
            dependency_to_register='Adapter',
            dependency_resolve_strategy=adapter_dependency_resolve_strategy,
        ).execute()

        adapter: TestInterface = IoC.resolve(dependency='Adapter', interface=TestInterface, data_object=mock_data)

        assert adapter.get_a() == 5
        assert adapter.get_b() == 6
        adapter.set_b(4)
        assert adapter.get_b() == 4
