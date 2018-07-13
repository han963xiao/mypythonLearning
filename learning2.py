#filter可以接受函数还有一个序列，意思是吧函数应用于每个元素，根据函数的
#所以函数必须要返回,true或者false
from functools import reduce
from operator import add
import  functools


def is_odd(n):
    return n % 2 ==0
list1=[1,2,3,4,5,6,7,8,9]
#list(),这里就是强转的
print(list(filter(is_odd,list1)))

#高阶函数就是把这个函数对于各种list中的各个元素，map()
def square(x): #这个函数是对于任何数来应用的
    return x*x
r=map(square,[1,2,3,4,5,6])#你看这个map的解释也能知道,要先传进去一个函数，可以传进去可以iteratable的对象
print(list(r))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))) #list啊还有str这些函数都是强转类型的函数

#reduce也是高阶函数，但是跟map完全不一样，他使迭代的用法，必须接受两个参数,里面的函数也是对两个数计算的
#每次把前两个数的结果和第三个数再进行运算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4) 类似这样
r1=reduce(add,[1,3,7,9])
print(r1)

#例如把序列变成对应的十进制数，例如把[1,3,5,7,9]变成13579，利用reduce就非常方便
#reduce在迭代方面非常方便
def toTen(x,y):
    return x*10+y
print(reduce(toTen,[1,3,5,7,9]))

#map和reduce的综合应用
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#上面先用map把字符转成数字，他是一个list，然后把数字list变成十进制的数
#用了lambda表达式，也就是匿名函数

#匿名函数
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#冒号前面的x表示函数参数
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果，有些功能很小的地方匿名函数很有用

#decrator的用法学习
def log(text):
    def decorator(func):
        #下面这个包好像不会自动引入
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s,%s:'%(text,func.__name__)) #参数格式化，外面的%一定不能忘啊！！！
            return func(*args,**kw) #这里调用原函数
        return wrapper
    return  decorator
@log('execute')
def now():
    print('2015-3-25')
now()

#int函数提供额外的base参数,默认值位10，可以指定从字符串做n进制的转化
#最后都是华为10进制的，这里的base是指字符串他是几进制的
print(int('12345',base=6))