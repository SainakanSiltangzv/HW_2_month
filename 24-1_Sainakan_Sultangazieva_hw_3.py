# ДЗ*:
# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # 2. Добавить сеттеры и геттеры к существующим атрибутам.
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    # 3. Добавить в класс Computer метод make_computations, в котором бы выполнялись
    # арифметические вычисления с атрибутами объекта cpu и memory.
    def make_computations(self):
        if isinstance(self.__cpu, int) and isinstance(self.__memory, int):
            return self.__cpu + self.__memory
        else:
            raise TypeError

    # 9. В каждом классе переопр. магический метод __str__ которые бы возвращали полную информацию об объекте.
    def __str__(self):
        return f'CPU:{self.__cpu}, memory:{self.__memory}'

    # 10. Перезаписать все магические методы сравнения в классе Computer, для того чтоб
    # можно было сравнивать между собой объекты, по атрибуту memory. == !=  <  >  <= >=
    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


# 4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
class Phone:
    __sim_cards_list = ['beeline', 'O!', 'Megacom']

    # 5. Добавить сеттеры и геттеры к существующему атрибуту.
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list  # self даже атрибутам класса

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    # 6. Добавить в класс Phone метод call с входящим параметром sim_card_number и
    # call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от
    # переданного номера сим-карты (например: если при вызове метода передать число 1 и
    # номер телефона, распечатывается текст “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).
    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - Beeline')

    # 9. В каждом классе переопр. магический метод __str__ которые бы возвращали полную информацию об объекте.
    def __str__(self):
        return f'sim_cards_list:{self.__sim_cards_list}'


# 7. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
class SmartPhone(Computer, Phone):
    def __init__(self,cpu, memory):
        Computer.__init__(self,cpu, memory)
        Phone.__init__(self)

    # 8. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который
    # бы распечатывал симуляцию приложения маршрута до локации.
    def use_gps(self, location):
        print(f'построен маршрут от текущей локации до {location}')

        # 9. В каждом классе переопр. магический метод __str__ которые бы возвращали полную информацию об объекте.
        '''не будет, т.к. унаследует от родительского класса'''


# 11. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
lenovo = Computer(200, 8)
phone = Phone()
Samsung_Galaxy_M32 = SmartPhone(150, 6)
Samsung_Galaxy_A32 = SmartPhone(140, 8)
Samsung_Galaxy_S21 = SmartPhone(180,12)


# 12. Распечатать информацию о созданных объектах
print(lenovo)
print(phone)
print(Samsung_Galaxy_M32)
print(Samsung_Galaxy_A32)
print(Samsung_Galaxy_S21)

# 13. Опробовать все возможные методы каждого объекта (например: use_gps, а также магические методы и тд.)
# == !=  <  >  <= >=
print(f'проверяет на равенство: {Samsung_Galaxy_M32 == Samsung_Galaxy_A32}')
print(f'проверяет на неравенство: {lenovo != Samsung_Galaxy_S21}')
print(f'проверяет меньше ли Samsung_Galaxy_S21 чем Samsung_Galaxy_A32:  {Samsung_Galaxy_S21 < Samsung_Galaxy_A32}')
print(f'проверяет больше ли lenovo чем Samsung_Galaxy_M32 : {lenovo > Samsung_Galaxy_M32}')
print(f'проверяет на больше либо равно:{Samsung_Galaxy_S21 <= Samsung_Galaxy_A32}')
print(f'проверяет на меньше либо равно: {lenovo >= Samsung_Galaxy_S21}')
print(SmartPhone.use_gps(Samsung_Galaxy_S21,'Tokmok'))