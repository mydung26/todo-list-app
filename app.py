tasks = []

def add_task(task_name):
    tasks.append({'name': task_name, 'completed': False})

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
    else:
        print("Chỉ số không hợp lệ!")

def list_tasks():
    print("Danh sách công việc:")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{i}. {status} {task['name']}")

if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập")
    complete_task(0)
    list_tasks()
