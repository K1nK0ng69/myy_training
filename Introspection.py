def introspection_info(obj):
    obj_type = type(obj)
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    module = getattr(obj, "__module__", "<built-in>")
    doc_string = getattr(obj, "__doc__", "Нет доступной документации")
    result = {
        "Тип": obj_type.__name__,
        "Аттрибуты": attributes,
        "Методы": methods,
        "Модуль": module,
        "Another_one": doc_string.strip() if doc_string else "Нет доступной документации"
    }
    return result

if __name__ == "__main__":
    number_info = introspection_info(42)
    print("Инфа о числе:")
    print(number_info)
    string_info = introspection_info("Hello, world!")
    print("\nИнфа о строке:")
    print(string_info)

    class MyClass:
        def __init__(self, value):
            self.value = value

        def my_method(self):
            return f"Value: {self.value}"

    my_object = MyClass(10)
    object_info = introspection_info(my_object)
    print("\nИнфа о пользовательском классе:")
    print(object_info)
