# 1
import json
import pickle


class SerializationInterface:
    def __init__(self, value=None):
        self.value = value

    def serial_data(self, command, name_file, format_write):
        with open(name_file, format_write) as f:
            command.dump(self.value, f)


class JsonFormat(SerializationInterface):
    def __init__(self, value):
        super().__init__(value)

    def serial_data(self, *args, **kwargs):
        return super().serial_data(json, 'format.json', 'w')


class PickleFormat(SerializationInterface):
    def __init__(self, value):
        super().__init__(value)

    def serial_data(self, *args, **kwargs):
        return super().serial_data(pickle, 'format.pickle', 'wb')


# 2

class Meta(type):
    class_number = 0

    def __new__(mcs, *args, **kwargs):
        instance = super().__new__(mcs, *args, **kwargs)
        instance.class_number = mcs.class_number
        mcs.class_number = mcs.class_number + 1
        return instance


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
