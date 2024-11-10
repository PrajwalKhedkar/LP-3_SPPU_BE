'''Write a program non-recursive and recursive program to calculate Fibonacci numbers and
analyze their time and space complexity.
'''
import time

def fib_rec(num):
    if(num==1 or num==2):
        return 1
    else:
        return(fib_rec(num-1)+fib_rec(num-2))

def fib_itr(num):
    if(num==1 or num==2):
       return 1
    a=1
    b=1
    while(num>2):
        c=a+b
        a=b
        b=c
        num-=1
    return c

inp=8

time1=time.perf_counter()
time5=time.time()
op1=fib_rec(inp)
time2=time.perf_counter()
time6=time.time()

time3=time.perf_counter()
op2=fib_itr(inp)
time4=time.perf_counter()
print('Recursive:',op1)
print('Iterative:',op2)
print((time2-time1)* 10**9,'\n',(time4-time3)* 10**9,'\n')
print(time5,'\n',time6)