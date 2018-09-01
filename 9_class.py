# 父类
class Car(object):
    # 类对象和实例对象
    # 类属性和实例属性
    # 类方法和实例方法
    # 私有属性和公有属性
    # 私有方法和公有方法
    # 类对象可以调用类属性和类方法，但不能使用实例属性和实例方法
    # 实例对象可以获取类属性和实例属性，但不能对类属性进行操作
    # 实例对象可以调用类方法和实例方法
    carNum = 0 # 类属性
    def __init__(self, newName, newColor, distance=0):
        self.__name = newName #私有属性
        self.__color = newColor
        self.__distance = distance
        self.length = 5 #公有属性

    def __str__(self):
        string1 = '这辆车的名字是' + self.__name
        string2 = '这辆车的颜色是' + self.__color
        string3 = '这辆车的行驶里程是' + str(self.__distance)
        return string1 + '\n' + string2 + '\n' + string3

    # 私有方法
    def __move1(self):
        self.__distance += 10
        print('这辆车的总里程' + str(self.__distance) + '公里')

    # 间接调用私有方法
    def move2(self):
        self.__move1()

    # 间接调用私有属性
    def move3(self):
        self.__distance += 100
        print('这辆车的总里程' + str(self.__distance) + '公里')

    # 类方法
    @classmethod
    def move4(cls):
        print('这是一个类方法')

    def __del__(self):
        print('这辆车到期了')

# 子类；只能间接使用私有属性和私有方法
class Audi(Car):
    def appearance(self):
        print('这辆车的长度是' + str(self.length))
        # print('这辆车的名字是' + self.__name)

# 类对象调用类属性
print(Car.carNum)

# 实例对象1
Benz = Car('Benz', '月光石灰', 0)
print('此对象的内存地址是' + str(id(Benz)))
print(Benz)
Benz.move2()
Benz.move3()

print('---------分割线---------')

# 实例对象2
A4l = Audi('A4l', '黑色', 0)
print('此对象的内存地址是' + str(id(A4l)))
print(A4l)
A4l.appearance()
A4l.move2()