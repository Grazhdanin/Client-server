# import logging
# from logging.handlers import TimedRotatingFileHandler
from functools import wraps

#
#
# log_format = logging.Formatter(
#     '%(asctime)s %(levelname)s %(module)s %(message)s')
#
# rotation_handler = TimedRotatingFileHandler('log/server.log', 'midnight', 10, encoding='utf-8')
# rotation_handler.setFormatter(log_format)
#
# serv_log = logging.getLogger('server')
# serv_log.setLevel(logging.INFO)
# serv_log.addHandler(rotation_handler)
#
# serv_log = logging.getLogger('server')

#
#
# def logthis(fnc):
#     @wraps(fnc)
#     def wrapped(*args, **kwargs):
#         print('log init value:', args[0])
#         res = fnc(*args, **kwargs)
#         print('log result:', res)
#         return res
#
#     return wrapped
#
#
# @logthis
# def your_func(your_arg):
#     return your_arg + 10


# print('your result:', your_func(10))

# def flogging(func):
#     def log_function_called():
#         serv_log.info(f'Вызвана {func}')
#     return log_function_called

# def flogging(func):
#     @wraps(func)
#     def wrapped(*args, **kwargs):
#         print(args)
#         print(kwargs)
#         print(f'Вызвана {func}')
#
#     return wrapped
#
#
# @flogging
# def my_name(a):
#     print(a)
#
#
# my_name(6)


# import inspect
#
#
# def foo():
#     print(inspect.stack()[1][3])
#
#
# def bar():
#     foo()
#
#
# bar()