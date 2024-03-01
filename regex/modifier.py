
class Sample:

    _name = "chintan"

    def __init__(self) -> None:
        pass

class Demo(Sample):

    def show(self):
        print(self._name)

s = Sample()
# print(s.name)

d = Demo()
d.show()