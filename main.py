print(2*2)
name = str(input())

print(f"Hi from {name} heheheh !!")

def fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(2))