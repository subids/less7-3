import os


# Создадим функцию для работы с заданными файлами
def create_file_list(folder):
    file_list = os.listdir(folder) # Получаем список имен файлов в папке
    print(file_list)
    merget_file_list = []  # Создаем список для хранения содержимого файлов
    for file in file_list:
        with open(folder + "/" + file, encoding='utf-8') as temp_file:  # Поочередно считываем файлы
            merget_file_list.append([file, 0, []])
            for line in temp_file:
                merget_file_list[-1][2].append(line.strip())  # Добавляем в список содержимое файла построчно
                merget_file_list[-1][1] += 1
                # Посчитаем кольчество строк
    # Отсортированный по значению числа строк список
    return sorted(merget_file_list, key=lambda x: x[1], reverse=False)


# Функцию для записи
def create_merget_file(folder, filename):
    with open(filename + '.txt', 'w+') as merget_file:  # Итоговый файл с именем "filename".txt
        merget_file.write(f'Даны файлы:\n')
        for file in create_file_list(folder):
            merget_file.write(f'Назввание файла: {file[0]}\n')  # Итоговый файл имена начальных файлов
            merget_file.write(f'Количество строк: {file[1]}\n')  # Итоговый файл число строк файлов
            for string in file[2]:
                merget_file.write(string + '\n')  # Итоговый файл содержимое начальных файлов с переносом строки
            merget_file.write('\n')
    return print('Файл создан')


create_merget_file('txt', 'merget_file')