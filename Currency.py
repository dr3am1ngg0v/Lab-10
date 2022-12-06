import logging

logging.basicConfig(level = logging.INFO, filename = "log.log", format = "%(asctime)s - %(levelname)s - %(message)s")

notes = [1, 2, 4, 8, 16, 32, 64]    # Список с достоинством банкнот
number_of_notes = [0, 0, 0, 0, 0, 0, 0]     # Список количества банкнот


while True:     # Цикл обработки ввода
    try:
        sum = int(input("Введите сумму натуральным числом больше 0: "))
        assert sum > 0
        logging.info(f'User has entered a sum: {sum}')
        break
    except AssertionError:
        logging.error(f'ERROR: Incorrect enter.')
        print("Некорректный ввод.\nПовторите попытку: ")
    except ValueError:
        logging.error(f'ERROR: Incorrect enter.')
        print("Некорректный ввод.\nПовторите попытку:")

    # Объявление вспомогательной переменной
step = 6
     
while sum > 0:  # Цикл подсчета
    pos = notes[step]
    number_of_notes[step] = sum // int(pos)
    if notes[step] != 0:
        sum = sum % int(pos)
    step -= 1

logging.info('Calculation has been made.')

for i in range(len(number_of_notes)):   # Вывод ответа
    if number_of_notes[i] != 0:
        print(f'Количество купюр стоимостью {notes[i]}: {number_of_notes[i]}')
        logging.info(f'Number of banknotes in face value {notes[i]}: {number_of_notes[i]}')
    else:
        pass

logging.info('Program finished')