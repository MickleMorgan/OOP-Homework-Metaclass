import json


class MetaClass(type):
    filename = "class_data.json"

    def __new__(mcs, name, bases, attrs):
        fields = [field for field in attrs if not callable(attrs[field])]
        data = {
            'name': name,
            'fields': fields
        }
        with open(mcs.filename, 'a') as f:
            f.write(json.dumps(data) + '\n')
        return super().__new__(mcs, name, bases, attrs)


class TestClass(metaclass=MetaClass):
    field1 = 1
    field2 = "test"