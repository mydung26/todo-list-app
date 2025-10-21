tasks = []

def add_task(task_name):
    tasks.append(task_name)

def list_tasks():
    print("Danh sách công việc:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập")
    list_tasks()
