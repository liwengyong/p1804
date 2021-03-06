# 元类 ：创建类 type
#1.type 创建类
#type(类的名称,(类继承对象），{属性})
Test2 = type('Test2',(),{})
t = Test2
print('类的打印结果',Test2)
print('类对象的打印结果',t)
#print(t.__name__)

#2.type 属性类
# {’属性名称‘：属性值}
Foo = type('Foo',(),{'bar':True})

print('类名打印',Foo)
print('类名直接访问属性',Foo.bar)
f = Foo()
print('类名打印',f)
print('类名直接访问属性',f.bar)
print('*'*52)
#3.type 带函数类 方法
Foo = type('Foo',(),{'bar':True})
print(Foo)
def echo_bar(self):
    print(self.bar)

#让FooChild类中的echo_bar属性，指向了上面定义的函数
FooChild = type('FooChildName',(Foo,),{'echo_bar1':echo_bar})

b = FooChild()
print(b)
print(b.bar)
print(b.echo_bar1())
print(b.echo_bar1)
