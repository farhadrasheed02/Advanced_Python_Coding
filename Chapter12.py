"""Try Catch Block"""
# u_input = int(input("Enter the number: -"))
# while True:
#     print("Press q to Exit")
#     a = (input("Enter the input"))
#     if a == 'q':
#         break
#     try:
#         a = int(a)
#         if a > 6:
#             print("You have entered the number greater than 6")
#     except Exception as ex:
#         print(f"Error occurred is : {ex}")
# print("Thanks for playing the game")


"""Multiple Try catch block """
# try:
#     a = int(input("Enter the number :"))
#     c = 1 / a
#     print(c)
# except ValueError as e:
#     print("Make sure you are entering integer value only")
# except ZeroDivisionError as e:
#     print("Make sure you not dividing by zero")
# except RuntimeError as e:
#     print("Check if it is not a runtime error")
# print("Thanks for using my Code...")

"""Raising Exceptions in the python using the raise key word
"""
# def increment(num):
#     try:
#         return num + 1
#     except:
#         raise ValueError("Please enter Integer only")
#
#
# a = increment(u_input)
# print(a)

""" Try except and else """

# try:
#     a = int(input("Enter the num "))
#     c = 5 / a
#     print(c)
# except Exception as e:
#     print(e)
# else:
#     print("We have done this part")  # This will get executed only after the successful execution

""" Try except and Finally """

try:
    a = int(input("Enter the num "))
    c = 5 / a
    print(c)
except Exception as e:
    print(e)
finally:
    print("We have done this part")  # This part will get execute even after the exception is raised
