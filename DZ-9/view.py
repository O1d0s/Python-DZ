
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

def show_contacts(pb: list[dict]):
  if pb == []:
    print('Телефонная книга пуста или вы не открыли файл')
  else:
    for i,contact in enumerate(pb,1):
        name = contact.get('name')
        phone = contact.get('phone')
        comment = contact.get('comment')
        print(f'{i}. {name:<20} {phone:<20} {comment:<20}')

def new_contact_input():
  name = input("Введите имя и фамилию: ")
  phone = input("Введите телефонный номер: ")
  comment = input("Введите коментарий: ")
  new_contact = {}
  new_contact['name'] = name
  new_contact['phone'] = phone
  new_contact['comment'] = comment
  return new_contact


def find_contact():
  find = input('Введите имя или номер: ')
  return find

def input_id():
  ind = int(input('Введите индекс: '))
  return ind



  