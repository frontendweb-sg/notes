class User:
    def __init__(self, name: str) -> None:
        self._name = name

    name = property(lambda self: self._name)
    other = name

    @classmethod
    def set_name(self, value: str):
        if len(value) <= 0:
            raise ValueError("value must be greater then 0")
        if self._name in self.__dict__:
            self._name = value
    # name = other.setter(set_name)


u1 = User('pl')

print(u1.name)

print(u1.set_name("HP"))
print(u1.name, u1.__dict__, User.__dict__, User._name)
