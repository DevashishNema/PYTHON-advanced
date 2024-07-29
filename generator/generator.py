# def gen():
#     i=1
#     my_list=[]
#     while i<=10:
        
#         my_list.append(i)
        
#         i=i+1
#     return my_list
# var1 = gen()
# print(var1)


# def gen():
#     i=1
#     my_list=[]
#     while i<=10:
        
#         my_list.append(i)
        
#         i=i+1
#     yield my_list
# var1 = gen()
# print(var1)   

# def gen():
#     i=1
#     my_list=[]
#     while i<=10:
        
#         my_list.append(i)
        
#         i=i+1
#     yield my_list
# var1 = gen()
# print(next(var1)) 

# def gen():
#     i=1
#     my_list=[]
#     while i<=10:
        
#         my_list.append(i)
        
#         i=i+1
#     yield my_list
# var1 = gen()
# for i in var1:
#     print(i)    




# def gen_no(x,y):
#     while x<=y:
#         yield x
#         x=x+1
# var1 = gen_no(1,10)
# print(next(var1)) 

def gen_no(x,y):
    while x<=y:
        yield x
        x=x+1
var1 = gen_no(1,10)
print(next(var1+1)) 
print(next(var1+2))    
for i in var1:
    i=i+5
    print(i)   