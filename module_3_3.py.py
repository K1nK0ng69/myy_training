def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = [4, True, "Row"]
values_dict = {'a':57, 'b':False, 'c':"Cry"}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 69.32]
print_params(*values_list_2, 42)