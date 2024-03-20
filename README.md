# tree_menu
Тестовое задание - Древовидное меню, выполнено на Windows 10


<br>

- [Установка и запуск](#установка-и-запуск)


<br>


## Установка и запуск:



1. git clone https://github.com/TasteBeam/tree_menu.git <br> cd tree_menu



2. python -m venv venv && source venv/bin/activate (linux) <br>
   python -m venv venv && venv\Scripts\activate (windows)

3. pip install -r requirements.txt


4. python app/manage.py makemigrations <br>
   python app/manage.py migrate <br>
   python app/manage.py load_data <br>
   python app/manage.py create_superuser <br>
   python app/manage.py runserver

Запустится локальный сервер. `http://127.0.0.1:8000/`

5. Остановить приложение можно комбинацией клавиш Ctrl-C.

Доступ к админ панели(Создан при установке) <br>
  -username = adm <br>
  -password = adm
      
 

Адрес меню: <br>
  - http://127.0.0.1:8000/menu/ <br>
  - http://localhost/menu/ 

Адрес админ панели и данные для входа: <br> <br>
  -username = adm <br>
  -password = adm<br>
  - http://127.0.0.1:8000/admin/<br>
  - http://localhost/admin/<br>
