import random
import string
import datetime




def add(file_name: str):
    unique_id = ''.join(random.choices(string.digits, k=4))
    title = input("Введите заголовок: ")
    note_text = input("Введите текст: ")
    time = datetime.datetime.now()
    with open(file_name, "a", encoding="utf-8") as fd:
        fd.write(f"{unique_id}; {title}; {note_text}; {time}\n")


def show(file_name: str):

    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        lst = []
        for i in data:
            j = i.split("; ")
            lst.append(j)
            # print(j)
        for i in lst:
            i[0] =int(i[0])
        lst1 = sorted(lst, key=lambda id: id[0])
        for item in lst1:
            print(*item)

def main():
    file_name = 'notebook.txt'
    flag_exit = False
    while not flag_exit:
        print("1 - показать все записи")
        print("2 - добавить новую запись")
        answer = input("Введите номер команды или 'x' для выхода:  ")
        if answer == "1":
            show(file_name)
        elif answer == "2":
            add(file_name)
        elif answer == "x":
            flag_exit = True


if __name__ == '__main__':
    main()
