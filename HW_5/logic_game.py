from random import randint
from main import many
slot = randint(1,30)
bank = many
def game():
    global bank
    print('Здравствуйте , вас приветствуует игра казино)')
    try:
        while True:
            print(f'Ваш нынешний баланс: {bank}')
            action = input('Сделайте свой выбор\n1 Играть \n2 Выйти\n')
            if action == '1':
                choose_slot = int(input('Выберите слот: '))
                stavka = int(input('Сколько хотите поставить: '))
                if choose_slot == slot and stavka <= bank:
                    bank += (stavka * stavka)
                    print('Вы угодали!')
                elif slot != choose_slot and stavka <= bank:
                    if bank > 0 and stavka <= bank:
                        bank -= stavka
                        print('Вы не угодали!')
                elif bank == 0:
                    print('Вы проиграли все свои денги')
                    continue
                elif stavka > bank:
                    print('У вас не хватает средств!')
            elif action == '2':
                if bank < 1000:
                    print('Вы в проиграше')
                    print('Игра окончена')
                    print(f'Ваша баланс {bank}')
                    break
                elif bank > 1000:
                    print('ВЫ в выйграше')
                    print('Игра окончена')
                    print(f'Ваш баланс {bank}')
                    break
                else:
                    break
            else:
                print('Нет такой настройки!!!')
    except TypeError:
        print('Error')
    except ValueError:
        print('Error, Пишите только ЧИСЛА!')
    except Exception:
        print('Error')