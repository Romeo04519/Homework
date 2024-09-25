import inspect
from pprint import pprint

class Inspec:

    def __init__(self, obj):
        self.obj = obj

    def introspection_info(self):
        #atr_list = []
        dict_obj = {}
        type_ = type(self.obj).__name__
        dict_obj['type'] = type_
        # for i in dir(self.obj):
        #     if inspect.isfunction(i) or inspect.ismethod(i):
        #         continue
        #     else:
        #         atr_list.append(i)
        # dict_obj['attributes'] = atr_list
        methods_ = inspect.getmembers(self.obj, predicate=inspect.isroutine)
        atr = inspect.getmembers(self.obj, predicate=lambda x: not (inspect.isroutine(x)))
        dict_obj['attributes'] = atr
        dict_obj['methods'] = methods_
        module_ = inspect.getmodule(self.obj)
        dict_obj['module'] = module_.__name__ if module_ else None
        return dict_obj

number_info = Inspec(42)
pprint(number_info.introspection_info())