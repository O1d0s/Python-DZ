

class PhoneBook:
  def __init__(self, path):
    self.path = path
    self.contact_book = []

  def open_file(self):
    with open(self.path, 'r', encoding='utf-8') as file:
      data= file.readlines() 
      for contact in data:
        new = contact.strip().split(';')
        new_contact = {}
        new_contact['name'] = new[0]
        new_contact['phone'] = new[1]
        new_contact['comment'] = new[2] 
        self.contact_book.append(new_contact)
    print(f'\nФайл {self.path} успешно открыт\n')
      
  def get(self):
    return self.contact_book

  def add(self, new_contact: dict):
    self.contact_book.append(new_contact)
    print(f'\n Контакт {new_contact.get("name")} успешно добавлен!\n')

  def save_file(self):
    data = []
    for contact in self.contact_book:
      data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open(self.path, 'w', encoding='utf-8') as file:
      file.write(data)
      print(f'\nФайл {self.path} успешно сохранен\n')

  def find(self,find_option: str):
    all_find = []
    for contact in self.contact_book:
      for element in contact.values():
        if find_option in element:
          print("Результат поиска:")
          all_find.append(contact)
    return all_find

  def change_contact(self, ind: int, contact: dict):
    self.contact_book[ind] = contact
    print(f'\n Контакт {contact.get("name")} был успешно изменен!\n')

  def delete_contact(self, ind: int):
    for i in self.contact_book:
      self.contact_book.pop(ind-1)

