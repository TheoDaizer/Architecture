from scope.initializer import Initializer
from ioc.ioc_container import IoC


class InitializeScopeTestCase:
    def setup_method(self, method):
        Initializer.execute()
        scope = IoC.resolve('IoC.Scope.Create')
        IoC.resolve('IoC.Scope.Current.Set', scope=scope).execute()

    def teardown_method(self, method):
        IoC.resolve('IoC.Scope.Current.Clear').execute()
