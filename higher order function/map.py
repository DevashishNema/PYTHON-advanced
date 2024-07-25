# WAP to find square of any collection by MAP

# my_list = [1,2,3,4,5]

# def square(n):
#     return n**2
# new_list = list(map(square,[1,2,3,4,5]))
# print(new_list)

# ---------------------------------------------------------

# WAP to find add of any 2 collection on the basis of indexing by MAP

my_list1 = [1,2,3,4,5]
my_list2 = [5,4,3,2,1]

def add(x,y):
    return x+y
new_list = list(map(add,my_list1,my_list2))
print(new_list)