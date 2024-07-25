# max from reduce 

# # import functools
# from functools import reduce
# def max(x,y):
#     if x>y:
#         return x
#     else :
#         return y

# print(reduce(max,[10,30,60,40,50,20])) 
# # print(functools.reduce(max,[10,30,50,40,60,20]))   

# min from reduce

# import functools
from functools import reduce
def min(x,y):
    if x<y:
        return x
    else :
        return y

print(reduce(min,[10,30,60,40,50,20])) 
# print(functools.reduce(max,[10,30,50,40,60,20]))  