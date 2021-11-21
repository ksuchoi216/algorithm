# Define sum_to_one() below...
def sum_to_one(n):
  if n is 1:
    return n
  else:
    print("Recursing with input: {0}".format(n))
    return n + sum_to_one(n-1)

def factorial(n):
  if n <= 1:
    return 1
  else:
    print("this is num {0}".format(n))
    return n * factorial(n-1)

def flatten(my_list):
  result = []
  for el in my_list:
    if isinstance(el, list):
      print("list found!")
      flat_list = flatten(el)
      result += flat_list
    else:
      result.append(el)
  return result

def fibonacci(n):
  # base cases
  if n == 1:
    return n
  if n == 0:
    return n
  
  # recursive step
  print("Recursive call with {0} as input".format(n))
  return fibonacci(n - 1) + fibonacci(n - 2)


