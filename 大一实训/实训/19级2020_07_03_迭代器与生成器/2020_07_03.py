'''
1、Python中的特殊方法
2、__方法名/属性名__ :特殊类/属性
3、开发者重写特殊类/直接调用 达到使用特殊类的目的  __init__
4、了解这些特殊类很重要
'''

#__repr__ ：当我们调用这个函数时（print），方法的自我描述
# class item:
# 	def __init__(self,name,price):
# 		self.name = name
# 		self.price = price
#
# im = item("天",29.8)
# print(im)
# print(im.__repr__)

# class Apple:
# 	def __init__(self,color,weight):
# 		self.color = color
# 		self.weight = weight
#
# 	def __repr__(self):
# 		return "Apple[color="+self.color+"weight="+str(self.weight)+"]"
# a= Apple("红色",weight=5)
# print(a)


#__del__: 与__init__对应，任何一个Python对象在被销毁（垃圾回收GC）时，就会调用__del__。
#两个类相互调用0、1---> 1...CGC
#发生继承时，如果父类有 __del__方法，显示调用__del__
# class Item:
# 	def __init__(self,name,price):
# 		self.name = name
# 		self.price = price
# 	def __del__(self):
# 		print("del删除对象")
# im = Item('鼠标',29)
# x= im
# del im
# print("-------------------")

#__dir__：返回对象内部所有的属性、方法[]
# class Item:
# 	def __init__(self,name,price):
# 		self.name = name
# 		self.price = price
# 	def info(self):
# 		pass
# im = Item('鼠标', 29)
# print(im.__dir__())
# print("-"*20)
# print(dir(im))

#__dict__形成字典




# #反射支持
# '''
# 1、hasattr（obj（实例化类）,属性） ：检查obj里面是否包含属性
# 2、getattr（object,name[,defaulat]）:获取object里面名为name的属性的属性值
# 3、strarrt(object,name,value):将object的name的属性值进行修改
# '''
# class comment:
# 	def __init__ (self,detail,view_times):
# 		self.detail = detail
# 		self.view_times = view_times
# 	def info(self):
# 		print("一条简单的评论%s" %self.detail)
# comment = comment("今天天气不错",20)
# #判断
# print(hasattr(comment,'detail'))
# print(hasattr(comment,'info'))
# #获取值
# print(getattr(comment,'detail'))
# #设置值
# setattr(comment,'view_times',30)
# print(comment.view_times)

#__call__:hasattr()
#在实际的代码编写 过程中，支持函数调用，关键在于__call__
#XXX = (arg1,arg2)---->xxx.__call__(arg1,arg2)
# class User:
# 	def __init__(self,name,password):
# 		self.name  = name
# 		self.password = password
# 	def valued(self):
# 		pass
# u = User('tom','A1234')
# print(hasattr(u.name,'__call__'))
#
# class roo:
# 	def __init__(self,name):
# 		self.name = name
# 	# def __call__(self):
# 	# 	print("执行roo")
# r = roo("小明")
# r()



'''
序列：所谓序列，指的是一块可存放多个值的连续内存空间，这些值按一定顺序排列，可通过每个值所在位置的编号(称为索引)访问它们
包含：字符、列表、元组
特质：所有序列都支持迭代
   	 序列表示索引为非负整数的有序对象集合
   	 字符和元组属于不可变序列，列表可变
'''
# def check_key(key):
# 	'''
# 	1、该函数将会负责检查序列的索引，该索引必须是整数，否则会引发TypeError异常
# 	2、要求程序索引必须为非负整数，否则引发IndexError异常
# 	:return:
# 	'''
# 	if not isinstance(key,int):raise TypeError('索引值必须是整数！')
# 	if key<0:raise IndexError('索引必须是非负整数')
# 	if key>=26**3:raise IndexError("索引值不能超过%d" %26**3)
# class Stringsq:
# 	def __init__(self):
# 		#用于存储被修改的数据
# 		self.__changed={}
# 		self._deleted = []
# 	def __len__(self):
# 		return 26**3 #17576
# 	def __getitem__(self,key):
# 		'''
# 		根据索引获取序列中元素
# 		'''
# 		check_key(key)
# 		#如果在self.__changed中找到修改后的数据
# 		if key in self.__changed:
# 			return self.__changed[key]
# 		#如果key在self.__deleted中,说明该元素已经被删除
# 		if key in self._deleted:
# 			return None
# 		#否则根据计算规则返回序列元素 //:整除
# 		three = key//(26*26)
# 		Two = (key-three*26*26)//26
# 		one = key%26
# 		return chr(65+three)+chr(65+Two)+chr(65+one)
#
# 	def __setitem__(self, key, value):
# 		'''
# 		根据索引修改序列中元素
# 		'''
# 		check_key(key)
# 		#将修改的元素以K-V对的形式保存在____changed中
# 		self.__changed[key] = value
# 	def __delitem__(self, key):
# 		'''
# 		根据索引删除序列中元素
# 		'''
# 		check_key(key)
# 		#如果_deleted列表中没有包含被删除的key,则添加被删除的key
# 		if key not in self._deleted:self._deleted.append(key)
# 		#如果___changed中包含被删除的key,则删除它
# 		if key in self.__changed:del  self.__changed[key]
#
# #创建序列
# sq = Stringsq()
# #获取序列的长度，实际上就是返回__len__()方法的返回值
# print(len(sq))
# print(sq[26*26])
# #打印修改之前的sq[1]
# print(sq[1])
# #修改sq[1]元素
# sq[1] = "tom"
# #打印
# print(sq[1])
# #删除sq[1]
# del sq[1]
# print(sq[1])
#
# #再次对sq[1]进行赋值
# sq[1] = 'Kitty'
# print(sq[1])

# 迭代器 = 遍历  	__iter__,__next__(返回迭代器的下一个元素)
'''
应用场景：
	1、如果数列（序列、列表、元组）的数据规模巨大
	2、数列有规律，但是依靠列表推导式描述不出来
	3、__reversed__(), 反 转
'''
#斐波那契数列
# class Fibs:
# 	def __init__(self,len):
# 		self.first = 0
# 		self.sec = 1
# 		self.__len = len
# 	#定义迭代器所需的__next__方法
# 	def __next__(self):
# 		if self.__len ==0:
# 			raise StopIteration
# 		#完成数列计算
# 		self.first,self.sec = self.sec,self.first+self.sec
# 		#数列长度-1
# 		self.__len-=1
# 		print(self.__len)
# 		return self.first
# 	#定义__iter__方法。该方法返回迭代器
# 	def __iter__(self):
# 		return  self
# # 创建
# fibs = Fibs(10)
# # #输出迭代器的下一个元素
# print('第一个元素为：',next(fibs))
# #使用for-in循环遍历迭代器
# for el in fibs:
# 	print(el  ,end='')


# 生成器 生成器就是一个迭代器 '冻结'
'''
1、yield创建
2、for循环
'''
# def test(val,step):
# 	print("函数开始执行")
# 	cur = 0
# 	#遍历，从0开始
# 	for i in range(val):
# 		cur += i*step
# 		yield cur
# t = test(10,2)
# # print("=============")
# print(next(t))
# print(next(t))
# for ele in t:
# 		print(ele,end=' ')
# print(list(t))#生成列表
# print(tuple(t)) #生成元组

#Demo2
# def square_gan(val):
# 	i = 0
# 	out_val = None
# 	while True:
# 		#使用yield 语句生成值，使用out_val接受send()方法发送的参数
# 		out_val = (yield out_val ** 2) if out_val is not None else (yield i ** 2)
# 		#如果程序使用send()方法获取下一个值，out_val会获取send()方法的参数值
# 		if out_val is not None:print("====%d" % out_val)
# 		i += 1
# sg = square_gan(5)
# print(sg.send(None))
# print(next(sg))
# # print("-------------------------")
# print(sg.send(9))
# print(next(sg))
# sg.close()