def print_params(a = 1, b = ' Module', c = True):
    print(a,b,c)

values_list=[2,'b',False]
values_dict={'a':1, 'b':'Module', 'c':True}
values_list_2=[2,'a']


print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)