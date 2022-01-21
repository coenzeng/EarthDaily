def fib(n: int, memo = {}):
  if n < 2:
    return n
  if n in memo:
    return memo[n]
  else:
    memo[n] = fib(n - 1) + fib(n - 2)
  return memo[n]
