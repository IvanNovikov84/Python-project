                                #Завдання 38. ООП. Клас телефон.
                                #Доброго раночку!
class Phone:
    def __init__(self, number, model, weight):
        self.number=number
        self.model=model
        self.weight=weight

    def receiveCall (self, name):
        print('Телефонує:', name)


    def Three (self, number, model, weight):
        print("Номер телефону:",number, "Модель:", model, "Вага:",  weight)

    @classmethod
    def Two (cls, number, model):
        print("Номер телефону:",number, "Модель:", model)

    def NoneP (self):
        pass

    def getNumber (self):
        return self.number

    def sendMassege (self):
        print('Повідомлення надіслане на номер:', self.number)





Bodya=Phone(+380987845998, 'Nokia', 120)
Bodya.getNumber()
Bodya.receiveCall('Бодя')
Bodya.Two(+380987845698, 'Nokia')


Vanya=Phone(+380982345687, 'Sumsung', 130)
Vanya.getNumber()
Vanya.receiveCall('Ваня')
Vanya.Two(+380982345687, 'Sumsung')


Ira=Phone(+380977845998, 'iPhone', 110)
Ira.getNumber()
Ira.receiveCall('Іра')
Ira.Two(+380977845998, 'iPhone')

while True:
 print('________________')
 print('1. Надіслати СМС Боді\n2. Надіслати СМС Вані\n3. Надіслати СМС Ірі\n4. Заблокувати телефон')
 Sms= input('Виберіть дію:\n')
 match  Sms:
     case '1':
         a=input('Введіть текст повідомлення:\n')
         Bodya.sendMassege()
     case '2':
         a = input('Введіть текст повідомлення:\n')
         Vanya.sendMassege()
     case '3':
         a = input('Введіть текст повідомлення:\n')
         Ira.sendMassege()
     case '4':
         exit()
     case _:
         print('Ви ввели щось не так')
