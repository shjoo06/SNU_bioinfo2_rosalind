from collections import defaultdict, deque
import numpy as np
import sys

def parse_file(file):
    adj_list = defaultdict(dict)
    # In this problem, I think we can just assume first n nodes as an integer index are leaves

    with open(file, 'rt') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i == 0 : 
                num_leaves = int(line.strip())
            else: 
                source, target_and_weight = line.strip().split('->')
                target, weight = target_and_weight.split(':')
                source, target, weight = int(source), int(target), int(weight)
                adj_list[source][target] = weight
    
    return adj_list, num_leaves

def distance(adj_list, i, j):
    queue = deque([(i, 0)]) # initialize with (starting_node, distance_so_far)
    visited = set()

    while queue:
        current, dist = queue.popleft()
        if current == j:
            return dist

        for next_node, weight in adj_list[current].items():
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, dist + weight))
    
    raise ValueError(f"Could not find a path between {i} and {j}")
    return

def create_dist_matrix(adj_list, num_leaves):
    matrix = np.zeros((num_leaves, num_leaves), dtype=int)
    # calculate only upper triangle since matrix is symmetric
    for i in range(num_leaves):
        for j in range(i+1, num_leaves):
            matrix[i][j] = distance(adj_list, i, j)
            matrix[j][i] = matrix[i][j]
    return matrix

def main():
    adj_list, num_leaves = parse_file(sys.argv[1])
    dist_matrix = create_dist_matrix(adj_list, num_leaves)
    for row in dist_matrix:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    main()


