



# def stadard_arg(arg):
#     print(arg)
# def pos_only_arg(arg, /)
#     print(arg)
# def kwd_only_arg(*, arg):
#     print(arg)
# def combined_example(pos_only, /, standard, *, kwd_onle):
#     print(pos_only, standard, kwd_only)
#
#
# def foo(name, **kwds):
#     return 'name' in kwds
#
# def foo(name, /, **kwds):
#     return 'name' in kwds


# x = int(input("Please enter an integer: "))
#
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')
#
#
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w., len(w))


# list(range(5, 10))
# list(range(0, 10, 3))
# list(range(-10, -100, -30))
#
# a = ['mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])
#
# range(10)
#
# sum(range(4))
#
#
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         print(n, 'is a prime number')
#
#
# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found an odd number", num)
#
#
# while True:
#     pass
#
#
# class MyEmptyClass:
#     pass
#
# def initlog(*args):
#     pass
#
#
# def http_error(status):
#     match status:
#         case 400:
#             return "bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"
#
#
#
# case 401 | 403 | 404:
# return "Nor allowed"
#
# match point:
#     case(o, o):
#         print("Origin")
#     case(o, y):
#         print(f'Y={y}')
#     case(x, o):
#         print(f'X={x}')
#     case(x, y):
#         print(f'x={x}, y={y}')
#     case _:
#         raise ValueError('Not a point')
#
#
#
# class Point:
#     x: int
#     Y: int
#
#
# def Where_is(Point):
#     match Point:
#         case Point(x=0, y=0):
#             print("Origin")
#         case Point(x=0, y=y):
#             print(f'Y={y}')
#         case Point(x=x, y=0):
#             print(f'x={x}')
#         case Point():
#             print("Somewhere else")
#         case _:
#             print("Not a point")
#
#
#
# match points:
#     case []:
#         print("No points")
#     case [Point(0, 0)]:
#         print("The origin")
#     case [Point(x, y)]:
#         print(f'Single point {x}, {y}')
#     case [Point(0, y1), Point(0, y2)]:
#         print(f'Two on the Y axis at {y1}, {y2}')
#     case _:
#         print("Something else")
#
#
#
# match point:
#     case Point(x, y) if x == y:
#         print(f'y=x at {x}')
#     case Point (x, y):
#         print(f'Not on the diagonal')
#
#
# from enum import Enum
# class color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'
#
# color = Color(input("Enter your choice of 'red', 'blue', or 'green': "))
#
# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")


# n = int(input('ajflsd'))
# for i in range(n):
#     print(i*i)


# x = int(input("please enter an integer:"))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')
#
#
#
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
#
#
# users = {'Hans': 'active', 'elenore': 'inactive', 'fffff': 'active'}
#
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
#
# active_users = {}
# for user, status in users.items():
#     if status == 'active': active_users[user] = status
#
#
#

# a, b = 0,1
# while a < 1000:
#     print(a, end=',')
#     a, b = b, a+b


# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a+b