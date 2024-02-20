
def greet(fx):
    def vfx():
        print("Welcome")
        fx()
        print("Good morning")
    return vfx
   

@greet
def hello():
    print("Hello")

hello()