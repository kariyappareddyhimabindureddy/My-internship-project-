print('----------To-Do List----------')
print()

tasks = []
completed_tasks = []

def add_task():
    print()
    name = input('Task name: ')
    description= input('Enter description about task: ')
    priority = input('Enter priority: ')
    due_date = input('Enter date: ')
   
    if len(name) == 0 or len(description) == 0 or len(priority) == 0 or len(due_date) == 0:
        print()
        print('Please full all fields')
        return
    data  = dict(name = name, description = description, priority = priority, due_date = due_date, is_task_completed = False)
    tasks.append(data)
    print()
    print('Task successfully added.')
    
def show_task():
    print()
    if len(tasks) == 0:
        if len(completed_tasks) == 0:
            print('There is no Uncompleted tasks.')
        else: 
            print('There is no tasks')
            
    print()
    for i in tasks:
        for j,k in i.items():
            print(f'{j} : {k}')
        print()
        
    for i in completed_tasks:
        for j,k in i.items():
            print(f'{j} : {k}')
        print()
        
    return
    
    
def remove_task():
    print()
    if len(tasks) == 0:
        print('There is no tasks. add task to remove.')
        return
    name = input('Enter name to find: ')
    
    x = {}
    
    for i in tasks:
        if i['name'] == name:
            x = i
        else: 
            print(f'there is no task with: {name}')
            return
    index = tasks.index(x)
    tasks.pop(index)
    print('Task successfully removed.')
    return


def update_task():
    print()
    if len(tasks) == 0:
        print('There is no tasks. add task to update.')
        return
    name = input('Enter task name to find: ')
 
        
    x = {}
    index = 0
    for i in tasks:
        if i['name'] == name:
            x = i
            index = tasks.index(i)
        else:
            print(f'There is no task with: {name}')
    
    print(x)
    print()
    
    ask = input('Enter key to update: ')
    
    if not ask in x.keys():
        print('Key is not available')
        return
    data = input(f'Write the {ask} here: ')
    
    if ask == 'is_task_completed':
        x[ask] = data
        tasks.pop(index)
        completed_tasks.append(x)
    else:
        x[ask] = data
        tasks.pop(index)
        tasks.append(x)
    
    
    
    print('Task successfully updated.')
    
    
    
    
    
while True:
    print()
    ask = input('''1.Show Tasks\n2.Add Tasks\n3.Remove Task\n4.Update Task\n''')
    
    if ask == '1':
        show_task()
    elif ask == '2':
        add_task()
    elif ask == '3':
        remove_task()
    elif ask == '4':
        update_task()
    else:
        print('Wrong choice')
        
        
    
    
