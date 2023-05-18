#1

import time

def rrr(func):
    def timer(*args, **kwargs):
        s=int(input("Введіть кількість викликів функції: "))
        f1=int(input("Введіть проміжок часу між викликами: "))
        for i in range(s):
            time.sleep(f1)
            func(*args, **kwargs)
    return timer
@rrr
def start():
    print("d")
start()

#2
def rrr(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs) + 100
        print(a)
    return wrapper

@rrr
def dobutok(s):
    res=1
    for args in s:
        res *= args
    return res
lst = [1, 2, 3, 4, 5]
dobutok(lst)


#3

def loging(func):
    def ddd(*args, **kwargs):
        returning=func(*args, **kwargs)
        print(f"Функція {func.__name__} приймає аргументи args :{args}"
              f" та kwargs :{kwargs}, і повертає {returning}")
    return ddd

@loging
def celsiy(c):
    farangeyt=1.8*c+32
    return farangeyt
celsiy(30)
celsiy(40)
celsiy(50)

#4
def numberrs(func):
    def wrapper(n):
        start_time=time.time()
        for i in range(2, n-1):
            if (n % i) == 0:
                print('число не є простим')
                break
            else:
                print('число просте')
                break
        end_time = time.time()
        time_taken = end_time - start_time
        print("Час виконання:", time_taken)
    return wrapper
@numberrs
def number(n):
    return n
number(43)

