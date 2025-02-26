import pytest
from threading import Thread

from ..initializer import Initializer
from ioc.errors import ResolveDependencyError
from ioc.ioc_container import IoC


class TestInitializer:
    def setup_method(self, method):
        Initializer.execute()
        scope = IoC.resolve('IoC.Scope.Create')
        IoC.resolve('IoC.Scope.Current.Set', scope=scope).execute()

    def teardown_method(self, method):
        IoC.resolve('IoC.Scope.Current.Clear').execute()

    def test_ioc_resolve_registered_dependency_in_current_scope(self):
        IoC.resolve(
            dependency='IoC.Register',
            dependency_to_register='TestDependency',
            dependency_resolve_strategy=lambda: 1
        ).execute()
        assert IoC.resolve('TestDependency') == 1

    def test_ioc_throw_error_on_unregistered_dependency_in_current_scope(self):
        with pytest.raises(ResolveDependencyError):
            IoC.resolve('UnregisterDependency')

    def test_ioc_use_dependency_from_parent_scope_if_not_defined_in_current_scope(self):
        IoC.resolve(
            dependency='IoC.Register',
            dependency_to_register='TestDependency',
            dependency_resolve_strategy=lambda: 2
        ).execute()

        scope = IoC.resolve('IoC.Scope.Create')
        IoC.resolve('IoC.Scope.Current.Set', scope=scope).execute()

        assert IoC.resolve('TestDependency') == 2

    def test_ioc_set_parent_scope_manually_for_new_scope(self):
        scope_1 = IoC.resolve('IoC.Scope.Create')
        scope_2 = IoC.resolve('IoC.Scope.Create', parent_scope=scope_1)

        IoC.resolve('IoC.Scope.Current.Set', scope=scope_1).execute()
        IoC.resolve(
            dependency='IoC.Register',
            dependency_to_register='TestDependency',
            dependency_resolve_strategy=lambda: 3
        ).execute()

        IoC.resolve('IoC.Scope.Current.Set', scope=scope_2).execute()
        assert IoC.resolve('TestDependency') == 3

    def test_global_root_scope_with_threads(self):
        IoC.resolve('IoC.Scope.Current.Clear').execute()
        IoC.resolve(
            dependency='IoC.Register',
            dependency_to_register='ScopeName',
            dependency_resolve_strategy=lambda **kwargs: 'global'
        ).execute()

        def runner():
            IoC.resolve(
                dependency='IoC.Register',
                dependency_to_register='ScopeName',
                dependency_resolve_strategy=lambda: 'thread'
            ).execute()


        thread = Thread(name='thread', target=runner)
        thread.start()
        thread.join()

        assert IoC.resolve('ScopeName') == 'thread'


    def test_local_current_scope_with_threads(self):
        IoC.resolve(
            dependency='IoC.Register',
            dependency_to_register='ScopeName',
            dependency_resolve_strategy=lambda: 'global'
        ).execute()

        def runner():
            IoC.resolve(
                dependency='IoC.Register',
                dependency_to_register='ScopeName',
                dependency_resolve_strategy=lambda: 'thread'
            ).execute()


        thread = Thread(name='thread', target=runner)
        thread.start()
        thread.join()

        assert IoC.resolve('ScopeName') == 'global'
