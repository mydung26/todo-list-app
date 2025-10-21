tasks = []

def add_task(task_name):
    tasks.append({'name': task_name, 'completed': False})

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        deleted = tasks.pop(task_index)
        print(f"Đã xóa: {deleted['name']}")
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
    delete_task(1)
    list_tasks()
