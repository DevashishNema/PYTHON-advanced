# def outer_fun(fun):
#     def inner_fun():
#         return fun()
#     return inner_fun
# @outer_fun
# def main():
#     print("This is from main fun")
# main()    


# def outer_fun(fun):
#     def inner_fun(x,y):
#         x=x+10
#         y=y+10
        
#         fun(x,y)
       
#         print("main function call")
#     return inner_fun
    
# def main_fun(x,y):
#     return x+y
    
# var1=outer_fun(main_fun)

# var2=var1(x,y)
# print(var2)


def outer_fun(fun):
    def inner_fun():
        return fun()
    return inner_fun
def main():
    print("This is from main fun")
var1=outer_fun(main)
var2=var1()