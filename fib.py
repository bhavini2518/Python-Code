# a=1
# b=1
# for i in range(10):
#     c=a+b
#     print(c)
#     a,b=b,c


def fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-1)
    
    for i in range(40):
        print(fib(i))