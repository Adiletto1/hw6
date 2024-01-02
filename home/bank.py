class Bank:
    def __init__(self,name,age,money,key):
        self._name=name
        self._age=age
        self.__money=money
        self.__key=key

    def print_name(self):
        print(self._name,self._age,self.__money,self.__key)

class Bank2(Bank):
    def set_name(self,name):
        self._name = name


    def get_name(self):
        return self._name, self._age, self.__money, self.__key

class Bank3(Bank2):
    @property
    def value(self):
        return self._name
    @value.setter
    def value(self, new):
        self._name = new

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,new_age):
        self._age = new_age

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,new_money):
        self.__money = new_money

    @property
    def key(self):
        return self.__key
    @key.setter
    def key(self, new_key):
        self.__key = new_key

adilet = Bank3('Adilet', 18, 20000, 1215)
adilet.value = 'Adiletto'
print(adilet.value)
adilet.age = 19
print(adilet.age)
adilet.money = 3000000
print(adilet.money)
adilet.key = 1011
print(adilet.key)


