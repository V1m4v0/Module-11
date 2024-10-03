def introspection_info(obj):
    import inspect

    info = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not attr.startswith('__')],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')],
        'module': obj.__module__,
    }

    return info


# Пример использования
class MyClass:
    def my_method(self):
        pass


my_object = MyClass()
number_info = introspection_info(my_object)
print(number_info)