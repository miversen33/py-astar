from collections import defaultdict
import random
def astar(start_node, goal_node, cost_method, heuristic_method, neighbor_method, depth_limit=None):

    def reconstruct_path(came_from, current_hash):
        path = [current_hash]
        for node in came_from.keys():
            next_node = hash_set[came_from[node]]
            path.insert(0, next_node)
        return path

    current_depth = -1
    start_hash = random.random()
    goal_hash  = random.random()
    hash_set = dict()
    hash_set[start_hash] = start_node
    hash_set[goal_hash] = goal_node
    open_set = [start_hash]
    came_from = dict()

    gscore = defaultdict(lambda: float('inf'))
    gscore[start_hash] = 0

    fscore = defaultdict(lambda: float('inf'))
    fscore[start_hash] = heuristic_method(start_node, goal_node)

    while len(open_set):
        current_depth += 1
        current_hash = None
        current_value = float('inf')
        for node_hash in open_set:
            if current_hash is None or fscore[node_hash] < current_value:
                current_hash = node_hash
                current_value = fscore[node_hash]

        if (depth_limit is not None and current_depth >= depth_limit) or (current_hash == goal_hash):
            return current_depth, reconstruct_path(came_from, current_hash)

        open_set.remove(current_hash)
        for neighbor in neighbor_method(hash_set[current_hash]):
            neighbor_hash = None
            if neighbor not in hash_set.values():
                neighbor_hash = random.random()
                hash_set[neighbor_hash] = neighbor
            else:
                for key,value in hash_set.items():
                    if value == neighbor:
                        neighbor_hash = key
                        break

            tentative_gscore = gscore[current_hash] + cost_method(hash_set[current_hash], neighbor)
            if tentative_gscore < gscore[neighbor_hash]:
                came_from[neighbor_hash] = current_hash
                gscore[neighbor_hash] = tentative_gscore
                fscore[neighbor_hash] = gscore[neighbor_hash] + heuristic_method(neighbor, goal_node)
                if neighbor_hash not in open_set:
                    open_set.append(neighbor_hash)