from collections import deque


# --- алгоритм з Частини 1 (НЕ змінювати) ---
def shortest_path(graph: dict, start, goal):
    if start == goal:
        return [start]
    visited = {start}
    queue = deque([start])
    parent = {start: None}
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                if neighbor == goal:
                    return reconstruct(parent, goal)
                queue.append(neighbor)
    return None


def reconstruct(parent: dict, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


# --- ВАШЕ ЗАВДАННЯ: змоделюйте граф прямих сполучень ---
routes = {
    "Площа Ринок": ["Оперний театр", "Високий Замок"],
    "Оперний театр": ["Площа Ринок", "Личаківський цвинтар",00 "Проспект Свободи"],
    "Високий Замок": ["Площа Ринок", "Собор святого Юра"],
    "Проспект Свободи": ["Оперний театр", "Собор святого Юра"],
    "Личаківський цвинтар": ["Оперний театр"],
    "Собор святого Юра": ["Високий Замок", "Проспект Свободи"],
    "Стрийський парк": []
}

# --- перевірка маршруту ---
def show_route(graph, start, goal):
    route = shortest_path(graph, start, goal)
    if route is None:
        print(f"{start} -> {goal}: доїхати цією мережею неможливо")
    else:
        rides = len(route) - 1
        print(f"{start} -> {goal}: " + " -> ".join(route)
              + f"  (поїздок: {rides}, пересадок: {rides - 1})")


# Тестові випадки
show_route(routes, "Площа Ринок", "Собор святого Юра")
show_route(routes, "Личаківський цвинтар", "Високий Замок")
show_route(routes, "Площа Ринок", "Стрийський парк")