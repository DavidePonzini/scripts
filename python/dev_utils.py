import importlib
from types import ModuleType

def reload_module(module: ModuleType):
    importlib.reload(module)