def schedule_tasks(task_hierarchy):
    i = 1
    task_hierarchy = sorted(task_hierarchy, key=lambda x: x['priority'])
    for item in task_hierarchy:
        if item['priority'] == i:
            if item['subtasks']:
                print(f'Task: {item['name']} - id: {item['id']} - priority: {item['priority']}')
                schedule_tasks(item['subtasks'])
            else:
                print(f'Task: {item['name']} - id: {item['id']} - priority: {item['priority']}')
        i+=1


task_hierarchy = [
    {'id':1, 'name': 'A', 'subtasks': [{'id':3, 'name': 'A-1', 'subtasks':[], 'priority': 2}, {'id':4, 'name': 'A-2', 'subtasks':[], 'priority': 1}, {'id':7, 'name': 'A-3', 'subtasks':[], 'priority': 3}], 'priority': 2},
    {'id':2, 'name': 'B', 'subtasks': [], 'priority': 1}, # no subtask - empty str or empty list works too
    {'id':5, 'name': 'C', 'subtasks': [{'id':6, 'name': 'C-1', 'subtasks':[{'id':8, 'name': 'C-1a', 'subtasks':[], 'priority': 1}], 'priority': 1}, {'id':6, 'name': 'C-2', 'subtasks':[], 'priority': 2}], 'priority': 3},
]
schedule_tasks(task_hierarchy)

# Time complexity
# Time complexity is O(nlog(n)) for the sorted function (Timsort) within the function and O(n) for the linear for loop. 
# Each time the function is called recursively the time complexity O(nlog(n)) + O(n) adds to itself, making this 
# time complexity n*(O(n*log(n)) + O(n)) where the first n is the number of times the function is called 
# (first time function is called recursively makes n = 2, second time n = 3, etc..)

# Space complexity
# Space compelxity of this function is O(n) as the sorted list rewrites the original list but grows in memory linearly
# as the size of the size of the list grows. Each time the function is called the space complexity adds making this space complexity
# n*O(n)