
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
  while True:
    data = int(input("Напишите номер действие которое хотите совершить: "))
    if data.isdigit() and 0 < int(data) < 9:
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
  while True:
    if new_contact['name'] != '' and new_contact['name'] != '' and new_contact['name'] != '':
      return new_contact
    elif new_contact['name'] == '':
      name = input("Введите имя и фамилию: ")
    elif new_contact['phone'] == '':
      phone = input("Введите телефонный номер: ")
    elif new_contact['comment'] == '':
      comment = input("Введите комментарий: ")
    


def find_contact():
  find = input('Введите имя или номер: ')
  return find

def input_id(book:list)->tuple:
  show_contacts(book)
  choise = int(input("Выберите контакт, который хотите изменить: "))
  name = input('Введите имя или Enter оставить без изменений: ')
  phone = input('Введите номер телеофна или Enter оставить без изменений: ')
  comment = input('Введите комментарии или Enter оставить без изменений: ')
  return choise-1, {'name': name if name else book[choise-1].get('name'),
                    'phone': phone if phone else book[choise-1].get('phone'),
                    'comment': comment if comment else book[choise-1].get('comment')}



  