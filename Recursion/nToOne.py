# 1 to n using tail recursion 
def fun(n):
  if  n==0:
    return
  fun(n-1)
  print(n)

fun(5)
  