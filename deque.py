# from collections import deque

# def search(name):
#     search_queue = deque()
#     search_queue += graph["name"]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if not person in searched:
#             if person_is_seller(person):
#                 print(f'{person} is a mango seller!')
#                 return True
#             else:
#             search_queue += graph[person]
#             searched.append(person)
#     return False

# search("you")

# from collections import deque

# graph = {
#     "you": ["Alice", "Bob", "Claire"],
#     "Bob": ["Anuj", "Peggy"],
#     "Alice": ["Peggy"],
#     "Claire": ["Tom", "Jonny"],
#     "Anuj": [],
#     "Peggy": [],
#     "Tom": [],
#     "Jonny": []
# }


# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if not person in searched:
#             if person_is_seller(person):
#                 print(f'{person} is a mango seller!')
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False

# search("you")

from collections import deque

graph = {
    "you": ["Alice", "Bob", "Claire"],
    "Bob": ["Anuj", "Peggy"],
    "Alice": ["Peggy"],
    "Claire": ["Tom", "Jonny"],
    "Anuj": [],
    "Peggy": [],
    "Tom": [],
    "Jonny": []
}


def person_is_seller(person):
    # Здесь вы можете добавить свою логику для определения, является ли человек продавцом манго
    return person.endswith("mango_seller")


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
