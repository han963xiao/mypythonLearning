# 字符串可以用双引号也可以用单引号 ctrl+/是注释的快捷键
#ctrl+shift+f 是搜索 搜索任意东西
#具体内容看廖雪峰

from collections import Iterable, Iterator
hello='hello'
world="world"
hw2015='%s %s %d'%(hello,world,2015)
print(hw2015)

# 字符串对象有很多很好用的函数
# 自动补全中v表示变量 c表示类 f表示函数可以直接传进去参数使用 p表示参数 m表示类中的方法
s='helo'
print(s.capitalize()) #字符串的首字母大写
print(s.upper()) #全大写
print(s.rjust(7)) #以7为长度右对齐
print(s.center(7)) #7个长度然后居中
print(s.replace('l','ell'))#字符替换，把l换成ell
print(' world'.strip()) #去掉首位空格
#列表list
xs=[3,1,2]
print(xs,xs[2]) #序号是从0开始标的
print(xs[-1]) #-1是最后一个位置
xs[2]='foo'
print(xs)
xs.append('bro')
print(xs)
x=xs.pop()
print(x)
#列表常用的操作切片
nums=list(range(100)) #立刻生成一个从0开始的序列
print(nums)
print(nums[0:10]) #取出里面序号从0到10的元素
print(nums[:10]) #从0开始可以省略这个0
print(nums[-2:]) #从最后开始也不用写-1
print(nums[20:22])
print(nums[:10:2]) #前10个数每2个取一次
print(nums[::2]) #所有数每2个取一个，默认全部的话就是全部

#循环
animals=['dog','cat','mouse'] #必须用：来开启代码块
for animal in animals:
    print(animal)

#enumerate()是python的内置函数,不仅可以返回值而且可以返回索引..
#多用在循环中既取序号又取值
list=['这','是','一个','测试']   #index,item这个中间是逗号，不是仅仅有空格
for index,item in enumerate(list):
    print(index,item)
#可以设置他们的索引值从哪一个数开始的,在后面添加数字
for index, item in enumerate(list,2):
    print(index, item)

#List comprehension
#这个相当相当相当有用，在很长的list生成过程中，效率完胜for循环

nums =[0,1,2,3,4]
squares=[]
for x in nums:
    squares.append(x**2) #x**2是它的二次方
print(squares)

#list comprehension在生成长的list中效率非常的高
nums=[0,1,2,3,4]
squares=[x**2 for x in nums] #这里就是读取然后直接写入的,list里可以直接写语句，能够读懂的
print(squares)

nums=[0,1,2,3,4]
squares=[x**2 for x in nums if x%2==0] #里面可以加条件的
print(squares)

#dic
d={'cat':'cute','dog':'fury'}
print(d['cat']) #根据key取出value
print('cat'in d)#判断是不是存在这个key
d['fish']='wet' #添加元素
print(d)
print(d.get('monkey','N/A')) #有key返回vaue，没有key返回n/a
del d['fish'] #删除某个key以及对应的value
for key,value in d.items():     #怎么遍历dic
    print('key:'+key+',value'+value)

#tuple,一旦初始化就不能修改 他外面是小括号
t=(1,) #只有一个元素的tuple必须要加，否则系统认为是一个数
print(t)
t2=('class','bob','home') #这就是tuple，外面是（）
print(t2)

#函数 py里面f开头的都是函数 例如max还有abs、还有最常用的print
print(max(2,3,5,6,3))   #这是两个函数
print(int('3'))
print(str(3))   #这里面都是强转
print(bool(-1)) #只要不是0和''都是true的

#函数返回多个值，实际就是一个tuple
def sign(x): #括号里面是函数需要传的值,开启代码块的：一定不能忘啊！,定义函数
    if x>0:
        return 'positive'
    if x<0:
        return 'negative'
    else:
        return 'zero'
for x in [-1,0,1]:
    print(sign(x))

#有关参数去看廖雪峰的blog
#可以在参数中定义默认参数，可以用也可以不用，可以传也可以不穿
#默认参数的写法，age=6,city='beijing' 还有更奇葩的L=[]
#要记住默认参数要指向不变对象，例如这里，因为默认参数是一个指针，指向的是一个变量，如果指向的那个值变了，默认参数也会改变的
#默认参数其实就是一个指针,如果值针指向的值变了，默认参数也会变
#你单独执行函数其实就是对默认参数操作的 例如add_end()
# def add_end(L=[]):
#     L.append('END')
#     return L

# def add_end(L=None): #这样写才是对的，默认参数指向不变对象
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#可变参数：传入参数不定的时候就可以采用这个写法 def calc(*numbers) 参数前带一个*号
#一般是把参数当成一个list，这样可以传进去一个不同大小的list，但是这样太麻烦
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#传参数的时候就是传calc([1, 2, 3]) 传一个数组

# def calc(*numbers): #可变参数的写法
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#当你的函数定义成了可变参数，你的参数却组成了一个list，例如你的参数数组是x[] 你调用可变参数的函数 可以这样 calc(*x) 在list或者其他类型前面加一个*号

#还有关键词参数
#可变参数是可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
#关键词参数必须是一个dict
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, **extra) extra是关键词参数，传进去的一个dic

#命名关键词参数 参数组合很复杂，去看blog
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。 不要引入太多参数，这样理解性太差了

#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。



def enroll(name,gender,age=6,city='beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age=',age)  #定义的默认参数不用也是可以的，下面这两行没有也是行的
    print('city:',city)

#传进去参数需要按顺序的
enroll('mengxiao','S')
enroll('mengxiao','S',22,'QINGZHOU')




#isinstance这是一个函数,不用自己手动引入的，引入之后可以自动联想
#判断是不是可以迭代的对象，前面是对象，后面是类型这里判断是不是iterable
#Iterable类型的对象，都是可以用for循环来遍历的
print(isinstance([],Iterable))
#这个就是判断是不是Iterator对象,前面这个对象，这个函数都是可以判断的!前面是对象后面是类型
#Iterator对象,可以用next()函数来不断调用
print(isinstance([],Iterator))
#可以把Iterable类型变成Iterator对象，用iter()函数，然后可以使用next()函数
print(isinstance(iter([]),Iterator))

#高阶函数sorted，可以对list进行排序，从小到大 这个函数里面可以联想到一个P，这个是选项的意思是不是按照绝对值排序等
#默认从小到大排序
#当然可以不带选项，就是默认的啊！
print(sorted([38,6,2,-1,-4,5],key=abs))
#这个函数可以对字符串进行排序，也就是对ASCII码
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)) #这个选项是忽略大小写的，有很多选项，ket还有revers还有boolean

#变量也可以指向函数的，所有的函数名其实都是指针，名字都是可以变的
f=abs   #代指的时候只能带名字不能带括号，abs()
print(f(-10))







