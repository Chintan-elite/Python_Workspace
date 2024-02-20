# var = 10;

# if(var<20):
#     print("okay")
# print("done")

a = 10;
b = 20;
c = 30;

# if(a>b):
#     if(a>c):
#         print("A is greater")
#     else:
#         print("C is greater")
# else:
#     if(b>c):
#         print("A is greater")
#     else:
#         print("C is greater")

if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is gresater")