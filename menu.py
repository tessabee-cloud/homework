# menu
from asyncio import tasks

from main import create_project,create_task, view_tasks, change_status, delete_task, search_task
while True:
    print('/n--- TASK MANAGER---')
    print('1. create project')
    print('2. create tasks')
    print('3. view tasks')
    print('4. search task')
    print('5. change status')
    print('6. delete task')
    print('7. EXIT')

    choice = input('choose: ')

    try:
        if choice == '1':
            create_project()

        elif choice == '2':
            create_task()

        elif choice == '3':
            view_tasks()

        elif choice == '4':
            search_task()


        elif choice == '5':
            change_status()

        elif choice == '6':
         delete_task()

        elif choice == '7':
         print('exiting the application')
         break

        else:
            print('invalid choice')

    except Exception as e:
        print(f'Error: {e}')
