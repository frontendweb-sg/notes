class Descriptor:
    def __init__(self, value: int) -> None:
        self.value = value

    def __get__(self, instance, owner):
        print("Getting value", instance, owner)
        return self.value


class Use:
    attr = Descriptor(10)


attr = Descriptor(10)
print(attr.value)
