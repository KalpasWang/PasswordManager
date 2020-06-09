from ast import literal_eval
from pathlib import Path
from os import system

def show_menu():
  system('clear')
  menu = '''
密碼管理大師
=================
1. 新增帳密
2. 顯示帳密
3. 修改密碼
4. 刪除帳密

輸入q結束程式
=================
'''
  print(menu)
  

def read_password():
  my_file = Path("./password.txt")
  if not my_file.exists():
    f = open('password.txt', 'w+')
    f.close()

  with open('password.txt', 'r', encoding='utf-8-sig') as f:
    data = f.read()
    if data != '':
      return literal_eval(data)
    return dict()
    


def add_password(passwords_dict):
  while True:
    name = input('輸入帳號(按ENTER鍵返回)；')
    if name == '':
      break
    if name in passwords_dict:
      print('帳號已存在，請換另一個帳號名稱')
      continue
    password = input('輸入密碼；')
    passwords_dict[name] = password
    with open('password.txt', 'w', encoding='utf-8-sig') as f:
      f.write(str(passwords_dict))
      print(f'{name}已儲存')
    input('')
    break
    

  

def show_password(passwords_dict):
  s = '''
帳號\t\t密碼
===========================
'''
  for key in passwords_dict:
    s += f'{key}\t\t{passwords_dict[key]}'
  s+= '\n'
  print(s)
  input()

def edit_password(passwords_dict):
  while True:
    name = input('輸入帳號(按ENTER鍵返回)：')
    if name == '':
      break
    if name not in passwords_dict:
      print('帳號不存在')
      continue
    while True:
      password = input('輸入原密碼：')
      if password == passwords_dict[name]:
        break
      print('密碼錯誤')

    new_password = input('輸入新密碼：')
    passwords_dict[name] = new_password

    with open('password.txt', 'w', encoding='utf-8-sig') as f:
      f.write(str(passwords_dict))
      print(f'{name} 密碼已儲存')
    input('')
    break
  
  

def del_password(passwords_dict):
  while True:
    name = input('輸入帳號(按ENTER鍵返回)：')
    if name == '':
      break
    if name not in passwords_dict:
      print('帳號不存在')
      continue
    
    choice = input(f'確定要刪除{name}的帳密嗎？(y/n) ').lower()
    if choice == 'y':
      del passwords_dict[name]
      with open('password.txt', 'w', encoding='utf-8-sig') as f:
        f.write(str(passwords_dict))
        print(f'{name} 已刪除')

    input('')
    break
  
 
  

