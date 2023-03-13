def print_menu():
  print('Это телефонный справочник. Пожалуйства выберите дейтвие которое хотите совершить:\n'
       '1.Открыть файл\n'
       '2.Сохранить файл\n'
       '3.Показать контакты\n'
       '4.Добавить контакт\n'
       '5.Изменить контакт\n'
       '6.Найти контакт\n'
       '7.Удалить контакт\n'
       '8.Выход\n')
  data = int(input("Напишите номер действие которое хотите совершить: "))
  return data

contact = []

def open_file():
  with open('contact.txt','r',encoding='utf-8') as data:
    contact = data.readlines() 
    print('Файл открыть') 
    return contact
    

def save_file():
  with open('contact.txt','w',encoding='utf-8') as data:
    for i in contact:
      data.write(i)
  print('Изменение сохранены')

def watch_contact():
  if len(contact) == 0:
    print('вы не открыли файл')
  else:
      for i in contact:
        print(i)
      
  
def add_contact():
    if len(contact) == 0:
        print('Вы не открыли файл')
    else:
        cont = input('Введите Имя; Номер; Город контакта:')
        contact.append('\n' +cont)


def change_contact():
  cont = input('Введите номер контакта которого хотите изменить: ')
  for i in range(len(contact)):
    if cont in contact[i]:
      print(contact[i])
      new_cont = input('Введите новые данные: ')
      contact[i] = new_cont



def search_contact():
  cont = input('Введите имя контактта которого хотите найти: ')
  for name in contact:
    if cont in name:
      print(name)


def delete_contact():
    num_cont = input('Введите имя контакта: ')
    for i in range(len(contact)):
      print(i)
      if num_cont in contact[i]:
        print(contact[i])
        contact.pop(i)
    



while True:
  user_action = print_menu()
  match user_action:
    case 1:
      contact = open_file()
    case 2:
      save_file()
    case 3:
      watch_contact()
    case 4:
      add_contact()
    case 5:
      change_contact()
    case 6:
      search_contact()
    case 7:
      delete_contact()
    case 8:
      print('Выход')
      break