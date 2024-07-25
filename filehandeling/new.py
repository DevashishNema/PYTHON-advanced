# f = open("first.txt",'x')

# f = open("first1.txt",'w')

# f = open("first2.txt",'a')

# f = open("first2.txt",'r')
# print(f.read())



# f = open("n2.txt",'x')
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)
# print(f.writable())


# f = open("n4.txt",'x')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)



# f = open("n4.txt",'w')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)



# f = open("n4.txt",'r')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)



# f = open("n4.txt",'a')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)


# f = open("n5.txt",'x+')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)





# f = open("n5.txt",'w+')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)




# f = open("n5.txt",'r+')
# print(f.name)
# print(f.mode)
# print(f.encoding)

# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)



# f = open("n5.txt",'a+')
# print(f.name)
# print(f.mode)
# print(f.encoding)

# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)



# f = open("n5.py",'a+')
# f.write("n%2==0")
# data = ('''
#     s=10
#     if (s%2==0):
#         print("even")'''
# )


# f = open("n1.txt",'a')
# data = ('hello\n','hey\n','welcome\n')
# f.writelines(data)
# print(f.readable())

# f1 = open('n1.txt','r')
# data = f1.read()
# print(data)
# f1.close()

# f = open("n1.txt",'r')

# f.read()
# f.read(5)
# f.readline()
# f.readlines()
# f.seek(0)

# print(f.read())
# print(f.read(5))
# print(f.readline())
# print(f.readlines)



f = open("n1.txt",'rb')
# f.write("Hello, This is DEVASHISH NEMA, I am from Bhopal (M.P).")
print(f.tell())
print(f.read(6))
print(f.tell())
# print(f.read(5))
print(f.seek(5,1))
print(f.tell())
print(f.read(10))
print(f.tell())
f.seek(-6,2)
f.read()
print(f.seek(-6,2))
print(f.read())


