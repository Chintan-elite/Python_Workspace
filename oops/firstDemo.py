
class Pen:
    price=10
    color="Red"

    def info(self):
        print(f"price : {self.price} , color : {self.color}")
    
    def __str__(self):
        return "Hello"



a = Pen()
# a.price=50;
# a.info()
print(a)