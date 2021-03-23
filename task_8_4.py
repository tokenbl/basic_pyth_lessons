def val_checker(lambda_func):
   def _val_checker(func):
      def wrapper(number):
         if lambda_func(number):
            return func(number)
         else:
            raise ValueError(number)
      return wrapper
   return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(3))
