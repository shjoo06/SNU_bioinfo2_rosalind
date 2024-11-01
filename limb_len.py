import sys
import numpy as np

def parse_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        temp = []
        for i, line in enumerate(lines):
            if i==0:
                num_leaves = int(line.strip())
            elif i==1:
                j = int(line.strip())
            else:
                temp.extend([int(x) for x in line.strip().split()])
        dist_matrix = np.array(temp, dtype=int).reshape(num_leaves, num_leaves)
    return dist_matrix, j, num_leaves


def limb_length(dist_matrix, j, num_leaves):
    min_dist = float('inf')
    for i in range(num_leaves):
        if i == j:
            continue
        for k in range(num_leaves):
            if k == j:
                continue
            dist = (dist_matrix[i][j] + dist_matrix[j][k] - dist_matrix[i][k]) / 2
            if dist < min_dist:
                min_dist = dist
    return min_dist


def main():
    dist_matrix, j, num_leaves = parse_file(sys.argv[1])
    limblength_j = limb_length(dist_matrix, j, num_leaves)
    print(int(limblength_j))

if __name__ == "__main__": 
    main()
