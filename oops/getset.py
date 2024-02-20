class Demo:

    def __init__(self,value):
        self.value=value

    def show(self):
        print(f"value is : {self.value}")

    @property
    def ten_value1(self):
        return 10*self.value
    
    @ten_value1.setter
    def ten_value(self, newval):
        self.value=newval

d = Demo(10)
d.show()

d.ten_value=50
print(d.ten_value)
