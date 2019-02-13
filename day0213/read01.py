class Person(object):
    # 类属性
    name = "pp"

    def __init__(self,_age):
        # 实例属性
        self.age =_age

      # 通过构造函数得到类的实例
# s1 = Person()
# s2 = Person()
# print(s1.name , s2.name)
# print(s1.age , s2.age)

s1 = Person(10)
s2 = Person(20)
s1.age = 52
print(s1.age , s2.age)