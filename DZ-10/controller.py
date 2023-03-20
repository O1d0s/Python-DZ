import db_manager
from view import *
from db_manager import PhoneBook



def start():
  pb = PhoneBook('contact.txt')
  while True:
    user_action = print_menu()
    match user_action:
      case 1:
        pb.open_file()
      case 2:
        pb.save_file()
      case 3:
        cb = pb.get()
        show_contacts(cb)
      case 4:
        new = new_contact_input()
        pb.add(new)
      case 5:
        ind = input_id(pb.get())
        pb.change_contact(*ind)
      case 6:
        find_con = find_contact()
        show_contacts(pb.find(find_con))
      case 7:
        pb = pb.get()
        show_contacts(pb)
        ind = input_id()
        pb.delete_contact(ind)
      case 8:
        print('Вы вышли из программы!')
        break