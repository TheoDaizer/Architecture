from typing import Type
from .adapter_from_interface_generator import AdapterGenerator

def adapter_dependency_resolve_strategy(interface: Type, data_object: dict):
    adapter_cls = AdapterGenerator(interface).generate()
    return adapter_cls(data_object)
