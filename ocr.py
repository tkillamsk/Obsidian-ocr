import os
from apple_ocr.ocr import OCR
from PIL import Image
from datetime import datetime

############
# Путь до ваулта Obsidian
vault = f''
# Файл, куда кладется распознанный текст.
file_name = 'unsorted.md'
# Какой символ выделяет задачу
task_sign = '#'

def read_tasks(pic):
    image = Image.open(pic)
    ocr_instance = OCR(image=image)
    result = ''
    for i in ocr_instance.recognize()['Content']:
        result +=i

    final = result.replace(task_sign, '\n- [ ] ')
    final = result.replace('!', '\n')
    return final


def write_tasks_to_file(filename, tasks, file=f'{vault}/{file_name}'):
        with open(file, 'a') as the_file:
            string = f'![[{filename}]]\n{datetime.now().strftime("%d/%m/%Y %H:%M")}\n {tasks}\n'
            the_file.write(string)
            print('Success!')

def do_delete(file_list):
    if len(file_list)==0:
        pass
    else:
        answer = input("Удалить файлы? Y/y для удаления")
        if answer == "Y" or answer == "y":
            for file in file_list:
                print(f'Deleting: {file}')
                os.remove(f'{vault}/{file}')
            else:
                pass



##################

file_list = [
    file for file in os.listdir(vault) if (file.endswith('.png') or
                                           file.endswith('.jpeg') or
                                           file.endswith('.jpg')
                                           )
             ]

for file in file_list:
    print(file.split('/')[-1])
    tasks = read_tasks(f'{vault}/{file}')
    write_tasks_to_file(file, tasks)
do_delete(file_list)
