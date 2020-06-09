from utils import show_menu, read_password, add_password, show_password, edit_password, del_password

passwords_dict = read_password()

while True:
  show_menu()
  cmd = input('輸入你的指令：')

  if cmd == '1':
    add_password(passwords_dict)
  elif cmd == '2':
    show_password(passwords_dict)
  elif cmd == '3':
    edit_password(passwords_dict)
  elif cmd == '4':
    del_password(passwords_dict)
  elif cmd == 'q':
    break


