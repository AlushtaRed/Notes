import random
import string
import datetime


def add(file_name: str):
    unique_id = ''.join(random.choices(string.digits, k=4))
    title = input("Введите заголовок: ")
    note_text = input("Введите текст: ")
    time = datetime.datetime.now()
    with open(file_name, "a", encoding="utf-8") as fd:
        fd.write(f"{unique_id}, {title}, {note_text}, {time}\n")


def show(file_name: str):

    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        lst = []
        for i in data:
            j = i.split(", ")
            lst.append(j)
        for i in lst:
            i[0] = int(i[0])
        lst1 = sorted(lst, key=lambda id: id[0])
        for item in lst1:
            print(*item)
    return lst1

def find (file_name: str):

        show(file_name)
        
        attr = input("Введите заголовок для поиска: ")
        with open(file_name, "r", encoding="utf-8") as f:
            data = f.readlines()
            data = list(filter(lambda x: x.split(", ")[1] == attr, data))
            x = list(zip(range(1,len(data)+1), data))
            for item in x:
                print(*item)
        #     if (data == []):
        #         print("Заметки с таким заголовком не найдено")
        #     else:
        #         print(data)
           
        return data[0]

def cover(file_name: str):
    old_data = find(file_name)
    old_id = old_data[0]
    print(old_data)
    print("Введите новые данные")
    new_title = input("Введите новый заголовок: ")
    new_note_text = input("Введите новый текст заметки: ")
    time = datetime.datetime.now()
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
       
        i = data.index(old_data)
       
        data[i] = f"{old_id}, {new_title}, {new_note_text}, {time}\n"
    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(data)
    show(file_name)

def main():
    file_name = 'notebook.txt'
    flag_exit = False
    while not flag_exit:
        print("1 - показать все записи")
        print("2 - добавить новую запись")
        print("3 - искать по заголовку")
        print("4 - корректировать заметку")
        answer = input("Введите номер команды или 'x' для выхода:  ")
        if answer == "1":
            show(file_name)
        elif answer == "2":
            add(file_name)
        elif answer =="3":
            find(file_name)
        elif answer =="4":
            cover(file_name)
        elif answer == "x":
            flag_exit = True


if __name__ == '__main__':
    main()
