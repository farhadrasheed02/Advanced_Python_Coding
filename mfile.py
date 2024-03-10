# import Chapter12 as m_function

# m_function.greet("Rashid")


""" Global Variable """

a = 44  # Global  Variable

# def fun1():
#     global a
#     print(f"Global variable value : - {a}")
#     a = 20  # Local Variable when global variable is not used
#     print(f"Local Variable value is : {a}")
#
#
# fun1()
# print(f"The value of a defined outside function is : - {a}")

"""Enumerate Function """
# lst = ['farhad',20.2,False,22]
#
# # for i in lst:
# #     print(i)
# for item,index in enumerate(lst):
#     print(item, index)

""" List Comprehension """

a1 = [2, 4, 6, 9, 10, 21, 25, 29, 30]

# for item in a1:
#     if item%2==0:
#         b.append(item)
# print(b)
b = [i for i in a1 if i % 2 == 0] # unique way of creating a list from existing List
print(b)
t= [1,2,3,4,5,4,6,8]
s= {i for i in t}
print(s)