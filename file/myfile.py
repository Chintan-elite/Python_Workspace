# f = open("myfile.txt",'rb')
# # f.write("hello py")
# text = f.read()
# print(text)


# f = open("kinju.jpg",'rb')
# text = f.read()
# print(text)

# with open("myfile.txt",'w') as f:
    # print(type(f))
    # f.seek(5)
    # f.write("Hello python")
    # f.truncate(5)
    # text = f.read()
    # print(text)


# f = open("myfile.txt","r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"{m1} {m2} {m3}")


# with open("myfile.txt") as f :
#     f.seek(11) 
#     print(f.tell())
#     text = f.read()
#     print(text)


import os
os.rmdir("NEWF")
# os.chdir(r'D:/')
# if not os.path.exists("NEWF"):
#     os.makedirs("NEWF")
# else:
#     print("Exist")
