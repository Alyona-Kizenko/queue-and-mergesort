from queue import Queue

def process_tasks(task_list):
    queue = Queue()
    current_time = 0
    result = []

    for duration in task_list:
        queue.enqueue(duration)

    while not queue.is_empty():
        duration = queue.dequeue()
        current_time += duration
        result.append((duration, current_time))
    
    return result

tasks = [3, 2, 5, 1]
completion_times = process_tasks(tasks)
for task, time in completion_times:
    print(f"{task}: завершена в {time}")