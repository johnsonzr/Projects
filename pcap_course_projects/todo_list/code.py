import random 
import string 

lower = string.ascii_lowercase
digits = string.digits 

class Todo_list:
    def __init__(self, file_path):
        self.file = file_path
        self.menu()
    def menu(self):
        while True:
            try:
                self.option = int(input('''== TODO LIST ==
[1] show tasks
[2] add task
[3] complete task
[4] exit
Your choice: '''))
                break
            except:
                    print('Please enter a valid option')
        if self.option == 1:
            self.show_tasks()

        elif self.option == 2:
            self.add_task()

        elif self.option == 3:
            self.complete_task()

        else:
            self.exit()
        

    def show_tasks(self):
        stream = open(self.file, 'r')
        lines = stream.readlines()
        for line in lines:
            print(line.strip().replace(';', ' | '))

        input('Press Enter to return to menu...')
        self.menu()
        stream.close()

    def add_task(self):
        stream = open(self.file, 'a')
        print('[ADD TASK]')
        new_task = input('Enter new task name: ')
        deadline = input('Enter deadline: ')
        new_id = random.choices(list(lower + digits), k = 14)
        stream.write(f"{''.join(new_id[0:6])}-{''.join(new_id[6:10])}-{''.join(new_id[10:14])};{new_task};{deadline}\n")
        stream.flush()
        stream.close()
        self.menu()

    def complete_task(self):
        stream = open(self.file, 'r')
        lines = stream.readlines()
        stream.close()
        for line in lines:
            print(line.strip().replace(';', ' | '))
        print('[COMPLETE TASK]')
        del_id = input('Enter ID of task to complete: ')
        updated_lines = [line for line in lines if not line.startswith(del_id)]
        stream = open(self.file, 'w')

        print(updated_lines)
        stream.writelines(updated_lines)
        stream.close()
        self.menu()

    def exit(self):
        print('Bye!')

list = Todo_list('pcap_course_projects/todo_list_project/list.txt')
